# Module 10: Verification Checklist

## Setup Verification

- [ ] `uv sync` completes without errors

```bash
cd modules/10-ml-fundamentals
uv sync
```

## Exercise Verification

- [ ] All ML tests pass

```bash
uv run pytest 03-exercises/ -v
```

Expected: 7 passed, accuracy >= 0.60

- [ ] Concepts example runs

```bash
uv run python 02-concepts/ml_pipeline_example.py
```

## Concept Verification

- [ ] Can split data into train/test sets with `train_test_split`
- [ ] Can create a Pipeline with preprocessing + classifier
- [ ] Can compute accuracy, precision, recall, F1
- [ ] Can read a classification report
- [ ] Understand what cross-validation measures

## Next Module Readiness

You are ready for Module 11 if you can:
- Prepare features and labels from a DataFrame
- Train and evaluate a classifier with scikit-learn
- Use a Pipeline to chain preprocessing and modeling
- Report model performance with proper metrics

---

**Completion:** When all boxes are checked, proceed to [Module 11](../11-applied-ai-patterns/README.md).