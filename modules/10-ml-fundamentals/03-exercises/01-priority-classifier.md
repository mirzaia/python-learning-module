# Exercise: Predict Order Priority from Features

## Scenario

Your warehouse wants to predict which orders will need priority handling based on total value, item count, and customer history. Build an ML pipeline that classifies orders as "priority" or "normal."

## Setup

```bash
cd modules/10-ml-fundamentals
uv sync
```

## Exercise 1: Generate and Prepare Data

Open `03-exercises/priority_classifier.py`. Complete `generate_training_data(n)` that creates synthetic order data with columns: total, items, customer_order_count, is_priority.

The synthetic rule (with noise): priority when `total > 200 and items > 3`.

## Exercise 2: Split and Train

Complete `train_model(X, y)` that:
1. Splits data into 80% train / 20% test with `random_state=42`
2. Creates a `Pipeline` with `StandardScaler` + `LogisticRegression`
3. Fits the pipeline on training data
4. Returns the pipeline and test data

## Exercise 3: Evaluate

Complete `evaluate_model(pipeline, X_test, y_test)` that:
1. Predicts on test data
2. Returns a dict with accuracy, precision, recall, and f1_score
3. All scores must be >= 0.60 for the model to be considered useful

## Verification

```bash
uv run pytest 03-exercises/ -v
```

Expected: all tests pass with accuracy >= 0.60.

## Bonus

Replace `LogisticRegression` with `RandomForestClassifier` and compare the metrics. Use `cross_val_score` for more robust evaluation.