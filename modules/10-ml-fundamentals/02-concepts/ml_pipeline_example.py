"""Module 10: ML pipeline example — predict order priority."""

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# Generate synthetic order data
def generate_orders(n: int = 200) -> pd.DataFrame:
    import numpy as np
    np.random.seed(42)

    data = {
        "total": np.random.uniform(10, 500, n),
        "items": np.random.randint(1, 10, n),
        "customer_orders": np.random.randint(1, 50, n),
        "is_returning": np.random.choice([0, 1], n, p=[0.3, 0.7]),
    }

    # Synthetic rule: priority = 1 if total > 200 and items > 3, else 0,
    # with some noise
    noise = np.random.choice([0, 1], n, p=[0.85, 0.15])
    data["priority"] = (
        ((data["total"] > 200) & (data["items"] > 3)) | noise
    ).astype(int)

    return pd.DataFrame(data)


df = generate_orders()
X = df[["total", "items", "customer_orders", "is_returning"]]
y = df["priority"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000)),
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print("=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["normal", "priority"]))

scores = cross_val_score(pipeline, X, y, cv=5, scoring="accuracy")
print(f"Cross-val accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")