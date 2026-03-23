"""
Section 5: Visualization + Probability
- Bar chart: average score by course
- Line chart: score trend across students
- Probability: P(pass) calculation + explanation
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# ── Generate dataset ──────────────────────────────────────────────────────────
data = {
    "name":   [f"Student_{i}" for i in range(1, 101)],
    "age":    [18 + (i % 5) for i in range(100)],
    "course": (["AI", "ML", "Data Science", "Web Dev", "Cybersecurity"] * 20),
    "score":  [round(40 + (i * 0.61) % 60, 2) for i in range(100)],
    "passed": [1 if round(40 + (i * 0.61) % 60, 2) >= 50 else 0 for i in range(100)],
}
df = pd.DataFrame(data)

# ── Chart 1: Bar Chart – Average Score by Course ──────────────────────────────
avg_by_course = df.groupby("course")["score"].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
bars = plt.bar(avg_by_course.index, avg_by_course.values, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"])
plt.title("Average Score by Course", fontsize=14, fontweight="bold")
plt.xlabel("Course")
plt.ylabel("Average Score")
plt.ylim(0, 100)
for bar, val in zip(bars, avg_by_course.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{val:.1f}", ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("charts/bar_chart.png", dpi=150)
plt.close()
print("Bar chart saved → charts/bar_chart.png")

# ── Chart 2: Line Chart – Score Trend ────────────────────────────────────────
sorted_scores = df.sort_values("score")["score"].reset_index(drop=True)

plt.figure(figsize=(11, 4))
plt.plot(sorted_scores.index, sorted_scores.values, color="darkorange", linewidth=1.5, label="Score")
plt.axhline(y=50, color="red", linestyle="--", linewidth=1, label="Pass threshold (50)")
plt.fill_between(sorted_scores.index, sorted_scores.values, 50,
                 where=(sorted_scores.values >= 50), alpha=0.15, color="green", label="Passed zone")
plt.fill_between(sorted_scores.index, sorted_scores.values, 50,
                 where=(sorted_scores.values < 50), alpha=0.15, color="red", label="Failed zone")
plt.title("Student Score Trend (Sorted)", fontsize=14, fontweight="bold")
plt.xlabel("Student Index")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("charts/line_chart.png", dpi=150)
plt.close()
print("Line chart saved → charts/line_chart.png")

# ── Probability Calculation ───────────────────────────────────────────────────
total = len(df)
passed = df["passed"].sum()
failed = total - passed
p_pass = passed / total
p_fail = failed / total

print("\n" + "=" * 50)
print("PROBABILITY ANALYSIS")
print("=" * 50)
print(f"Total students  : {total}")
print(f"Passed          : {passed}")
print(f"Failed          : {failed}")
print(f"\nP(pass)  = {passed}/{total} = {p_pass:.4f} = {p_pass*100:.1f}%")
print(f"P(fail)  = {failed}/{total} = {p_fail:.4f} = {p_fail*100:.1f}%")
print(f"\nInterpretation:")
print(f"  If a student is picked at random from this dataset,")
print(f"  there is a {p_pass*100:.1f}% chance they passed the course.")
print(f"  This means roughly {int(p_pass*10)} out of every 10 students pass.")
print(f"\nContext: A pass rate of {p_pass*100:.1f}% suggests the course is")
if p_pass >= 0.7:
    print("  relatively easy — most students are clearing the threshold.")
elif p_pass >= 0.5:
    print("  moderately difficult — about half the students pass.")
else:
    print("  quite challenging — fewer than half the students pass.")
