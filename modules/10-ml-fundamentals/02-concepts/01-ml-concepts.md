# ML Concepts: Features, Labels, Train/Test Split

ML is about finding patterns in data to make predictions. The fundamental loop: features → model → predictions → evaluate.

## Key Terms

- **Features (X)**: Input columns the model uses to predict
- **Labels (y)**: The target column you want to predict
- **Training set**: Data used to fit the model
- **Test set**: Held-out data used to evaluate the model
- **Overfitting**: Model memorizes training data but fails on new data

## Train/Test Split

```python
from sklearn.model_selection import train_test_split

# Prepare features and labels
X = df[["total", "items", "customer_tier"]]  # Features
y = df["will_reorder"]                        # Label

# Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

## Classification with Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
```

## The Confusion Matrix

```
                Predicted: No   Predicted: Yes
Actual: No         TN (85)          FP (15)
Actual: Yes        FN (10)          TP (90)
```

- **Accuracy**: (TP+TN) / Total — overall correctness
- **Precision**: TP / (TP+FP) — when we predict yes, how often are we right?
- **Recall**: TP / (TP+FN) — when it's actually yes, how often do we catch it?
- **F1 Score**: Harmonic mean of precision and recall

## When to Use Which Metric

- **Accuracy**: Balanced classes
- **Precision**: False positives are costly (e.g., flagging legitimate orders as fraud)
- **Recall**: False negatives are costly (e.g., missing actual fraud)
- **F1**: You care about both precision and recall