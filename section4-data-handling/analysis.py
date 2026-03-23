"""
Section 4: Data Handling + Analysis using Pandas
- Load CSV dataset
- Filtering, Grouping, Sorting
- 2 Insights
"""

import pandas as pd
import os

# ── Step 1: Generate sample CSV dataset ──────────────────────────────────────
os.makedirs("data", exist_ok=True)

raw = {
    "name":   [f"Student_{i}" for i in range(1, 101)],
    "age":    [18 + (i % 5) for i in range(100)],
    "course": (["AI", "ML", "Data Science", "Web Dev", "Cybersecurity"] * 20),
    "score":  [round(40 + (i * 0.61) % 60, 2) for i in range(100)],
    "passed": [1 if round(40 + (i * 0.61) % 60, 2) >= 50 else 0 for i in range(100)],
}
df_raw = pd.DataFrame(raw)
df_raw.to_csv("data/students.csv", index=False)
print("Dataset saved to data/students.csv\n")

# ── Step 2: Load dataset ──────────────────────────────────────────────────────
df = pd.read_csv("data/students.csv")
print("Shape:", df.shape)
print(df.head(), "\n")

# ── Step 3: Filtering ─────────────────────────────────────────────────────────
print("=" * 50)
print("FILTERING: Students who passed (score >= 50)")
print("=" * 50)
passed_df = df[df["passed"] == 1]
print(f"Total passed: {len(passed_df)} / {len(df)}")
print(passed_df[["name", "course", "score"]].head(10), "\n")

print("FILTERING: AI course students only")
ai_students = df[df["course"] == "AI"]
print(ai_students[["name", "age", "score"]].head(), "\n")

# ── Step 4: Grouping ──────────────────────────────────────────────────────────
print("=" * 50)
print("GROUPING: Average score by course")
print("=" * 50)
avg_by_course = df.groupby("course")["score"].mean().round(2).sort_values(ascending=False)
print(avg_by_course, "\n")

print("GROUPING: Count of students per course")
count_by_course = df.groupby("course")["name"].count()
print(count_by_course, "\n")

# ── Step 5: Sorting ───────────────────────────────────────────────────────────
print("=" * 50)
print("SORTING: Top 5 students by score")
print("=" * 50)
top5 = df.sort_values("score", ascending=False).head(5)
print(top5[["name", "course", "score"]], "\n")

print("SORTING: Bottom 5 students by score")
bottom5 = df.sort_values("score").head(5)
print(bottom5[["name", "course", "score"]], "\n")

# ── Step 6: Insights ──────────────────────────────────────────────────────────
print("=" * 50)
print("INSIGHT 1: Average score by course")
print("=" * 50)
print(avg_by_course)
print(f"\nTop performing course: {avg_by_course.idxmax()} ({avg_by_course.max():.2f})")
print(f"Lowest performing course: {avg_by_course.idxmin()} ({avg_by_course.min():.2f})\n")

print("=" * 50)
print("INSIGHT 2: Pass rate (%) by course")
print("=" * 50)
pass_rate = (df.groupby("course")["passed"].mean() * 100).round(2).sort_values(ascending=False)
print(pass_rate)
print(f"\nHighest pass rate: {pass_rate.idxmax()} ({pass_rate.max()}%)")
print(f"Lowest pass rate:  {pass_rate.idxmin()} ({pass_rate.min()}%)")
