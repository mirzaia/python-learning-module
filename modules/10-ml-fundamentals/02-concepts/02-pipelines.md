# scikit-learn Pipelines and Feature Engineering

Pipelines chain preprocessing and modeling into a single object. This prevents data leakage and makes your code cleaner.

## Why Pipelines?

Without pipelines, you might accidentally fit your scaler on the test data, leaking information:

```python
# DANGER: data leakage!
scaler = StandardScaler()
scaler.fit(X)  # Fits on ALL data including test
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

With pipelines, preprocessing is applied correctly:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

# Numeric features → scale
numeric_features = ["total", "items"]
numeric_transformer = StandardScaler()

# Categorical features → one-hot encode
categorical_features = ["customer_tier"]
categorical_transformer = OneHotEncoder()

# Combine transformers
preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features),
])

# Full pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000)),
])

# Safe: preprocessing only fits on train data
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

## Cross-Validation

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
print(f"CV F1 scores: {scores}")
print(f"Mean F1: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
```

## Feature Importance (Random Forest)

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# See which features matter most
importances = model.feature_importances_
for name, imp in zip(X.columns, importances):
    print(f"{name}: {imp:.3f}")
```