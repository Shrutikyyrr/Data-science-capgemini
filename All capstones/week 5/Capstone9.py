#Build a multi-agent customer support system that can classify, delegate, and resolve user queries.
#A company wants to automate its support system using AI agents.
from groq import Groq
import json

client = Groq(api_key="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")
#agent 1: classifier agent

def classifier_agent(query):

    prompt = f"""
You are a classifier agent.

Classify the query into one of:
- billing
- technical
- general

Respond ONLY in JSON:

{{
  "category": "billing/technical/general"
}}

Query: "{query}"
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    output = response.choices[0].message.content

    try:
        return json.loads(output)["category"]
    except:
        return "general"

# agent 2: billing agent

def billing_agent(query):

    prompt = f"""
You are a billing support agent.

Provide a helpful response for this query:

"{query}"
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return {
        "department": "Billing",
        "message": response.choices[0].message.content
    }
#agent 3 : technical agent

def technical_agent(query):

    prompt = f"""
You are a technical support agent.

Help the user with this issue:

"{query}"
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return {
        "department": "Technical Support",
        "message": response.choices[0].message.content
    }
# agent 4 : general agent

def general_agent(query):

    prompt = f"""
You are a customer support assistant.

Answer this general query:

"{query}"
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return {
        "department": "General Inquiry",
        "message": response.choices[0].message.content
    }

# agent 5 : reponse agent
def response_agent(query, result):

    return f"""
==============================
📥 Query: {query}

🏢 Department: {result['department']}

💬 Response:
{result['message']}
==============================
"""
#mcp orchestrator
def multi_agent_system(query):

    print("\n🧠 Received Query:", query)

    # Step 1: Classification (LLM)
    category = classifier_agent(query)
    print("🔍 Classified as:", category)

    # Step 2: Delegation
    if category == "billing":
        result = billing_agent(query)

    elif category == "technical":
        result = technical_agent(query)

    else:
        result = general_agent(query)

    print("📡 Routed to:", result["department"])

    # Step 3: Response formatting
    final_output = response_agent(query, result)

    return final_output

print("🚀 LLM Multi-Agent Support System Started (type 'exit')\n")

while True:

    user_input = input("Enter your query: ")

    if user_input.lower() == "exit":
        print("👋 Exiting...")
        break

    output = multi_agent_system(user_input)
    print(output)