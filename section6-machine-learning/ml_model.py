"""
Section 6: Machine Learning – Student Performance Prediction
- Classification (passed/failed)
- Models: Logistic Regression, KNN, Decision Tree
- Pipeline + StandardScaler (Bonus)
- Evaluation: Accuracy, Classification Report
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── Step 1: Generate / Load dataset ──────────────────────────────────────────
data = {
    "name":   [f"Student_{i}" for i in range(1, 101)],
    "age":    [18 + (i % 5) for i in range(100)],
    "course": (["AI", "ML", "Data Science", "Web Dev", "Cybersecurity"] * 20),
    "score":  [round(40 + (i * 0.61) % 60, 2) for i in range(100)],
    "passed": [1 if round(40 + (i * 0.61) % 60, 2) >= 50 else 0 for i in range(100)],
}
df = pd.DataFrame(data)
print(f"Dataset: {len(df)} rows | Pass: {df['passed'].sum()} | Fail: {(df['passed']==0).sum()}\n")

# ── Step 2: Preprocessing ─────────────────────────────────────────────────────
le = LabelEncoder()
df["course_enc"] = le.fit_transform(df["course"])

X = df[["age", "score", "course_enc"]]
y = df["passed"]

# ── Step 3: Train-Test Split ──────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train size: {len(X_train)} | Test size: {len(X_test)}\n")

# ── Step 4: Define models (all in pipelines with scaling) ────────────────────
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(random_state=42))
    ]),
    "KNN (k=5)": Pipeline([
        ("scaler", StandardScaler()),
        ("model", KNeighborsClassifier(n_neighbors=5))
    ]),
    "Decision Tree": Pipeline([
        ("scaler", StandardScaler()),
        ("model", DecisionTreeClassifier(max_depth=4, random_state=42))
    ]),
}

# ── Step 5: Train + Evaluate all models ──────────────────────────────────────
best_model_name = None
best_accuracy = 0
best_pipeline = None

for model_name, pipeline in models.items():
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("=" * 55)
    print(f"MODEL: {model_name}")
    print("=" * 55)
    print(f"Accuracy : {acc:.4f} ({acc*100:.1f}%)")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Fail", "Pass"]))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print()

    if acc > best_accuracy:
        best_accuracy = acc
        best_model_name = model_name
        best_pipeline = pipeline

# ── Step 6: Best model summary ───────────────────────────────────────────────
print("=" * 55)
print(f"BEST MODEL: {best_model_name} — Accuracy: {best_accuracy*100:.1f}%")
print("=" * 55)

# ── Step 7: Sample predictions ───────────────────────────────────────────────
print("\nSample Predictions using best model:")
samples = [
    [20, 55, le.transform(["AI"])[0]],       # should pass
    [22, 42, le.transform(["ML"])[0]],        # should fail
    [19, 78, le.transform(["Data Science"])[0]],  # should pass
]
for s in samples:
    pred = best_pipeline.predict([s])[0]
    prob = best_pipeline.predict_proba([s])[0]
    course_name = le.inverse_transform([s[2]])[0]
    print(f"  age={s[0]}, score={s[1]}, course={course_name} "
          f"→ {'PASS ✓' if pred == 1 else 'FAIL ✗'} "
          f"(confidence: {max(prob)*100:.1f}%)")
