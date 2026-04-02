#Build a multi-step intelligent advisor system using agent workflows.
#💼 Problem Statement
#Students need guidance on career paths based on their skills.
#Your system should:
#Analyze student profile
#Suggest career roles
#Generate learning roadmap
from groq import Groq
import json

client = Groq(api_key="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")

#domain detection

def detect_domain(user_input):
    text = user_input.lower()

    if any(word in text for word in ["html", "css", "javascript", "react"]):
        return "web development"
    elif any(word in text for word in ["python", "statistics", "data", "pandas"]):
        return "data science"
    elif any(word in text for word in ["network", "security", "cyber"]):
        return "cybersecurity"
    else:
        return "general"

#agent 1 :profile analyzer

def profile_analyzer(user_input):

    domain = detect_domain(user_input)

    prompt = f"""
Extract structured info.

Input: "{user_input}"

Return JSON:
{{
  "skills": [],
  "level": "beginner/intermediate",
  "domain": "{domain}"
}}
"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {"skills": [], "level": "beginner", "domain": domain}

#agent 2 :career agent

def career_agent(state):

    domain = state["domain"]

    domain_roles = {
        "web development": ["Frontend Developer", "Web Developer"],
        "data science": ["Data Analyst", "Data Scientist"],
        "cybersecurity": ["Security Analyst", "Ethical Hacker"],
        "general": ["Software Engineer"]
    }

    state["roles"] = domain_roles.get(domain, ["Software Engineer"])
    return state

#agent 3 : skill gap agent

def skill_gap_agent(state):

    domain = state["domain"]

    domain_gaps = {
        "web development": ["JavaScript", "React", "APIs"],
        "data science": ["SQL", "Machine Learning", "Data Visualization"],
        "cybersecurity": ["Linux", "Networking Tools", "Ethical Hacking"],
        "general": ["Programming Fundamentals"]
    }

    state["gaps"] = domain_gaps.get(domain, [])
    return state

#agent 4 : learning path agent

def learning_path_agent(state):

    level = state["level"]
    gaps = state["gaps"]

    roadmap = []

    if level == "beginner":
        roadmap.append("Start with basics of the domain")

    for skill in gaps:
        roadmap.append(f"Learn {skill}")

    roadmap.append("Build real-world projects")
    roadmap.append("Apply for internships/jobs")

    state["roadmap"] = roadmap
    return state

# mcp orchestrator

def career_system(user_input):

    print("\n🧠 Input:", user_input)

    state = profile_analyzer(user_input)
    print("📊 Profile:", state)

    state = career_agent(state)
    print("🎯 Roles:", state["roles"])

    state = skill_gap_agent(state)
    print("⚠️ Gaps:", state["gaps"])

    state = learning_path_agent(state)

    return f"""

🎯 Roles: {state['roles']}

⚠️ Skill Gaps: {state['gaps']}

📚 Roadmap:
{chr(10).join(['- ' + step for step in state['roadmap']])}

"""

print("🚀 Career Advisor Started (type 'exit')\n")

while True:
    user_input = input("Enter profile: ")

    if user_input.lower() == "exit":
        break

    print(career_system(user_input))