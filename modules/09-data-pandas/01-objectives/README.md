# Module 9: Learning Objectives

By the end of this module, you will be able to:

1. **Create and manipulate DataFrames**
   - Load from CSV, dicts, lists of dicts
   - Inspect with `.head()`, `.info()`, `.describe()`
   - Select columns and rows

2. **Filter and transform data**
   - Boolean indexing and `.query()`
   - `.apply()`, `.map()`, and vectorized operations
   - Handle missing data with `.fillna()` and `.dropna()`

3. **Group and aggregate**
   - `.groupby()` for split-apply-combine
   - Multiple aggregations with `.agg()`
   - Pivot tables and cross-tabulations

4. **Merge and join datasets**
   - `.merge()` like SQL joins
   - `.concat()` for stacking
   - Join on indexes vs columns

## What This Module Does NOT Cover

- Time series analysis — optional advanced topic
- pandas with databases (SQL read/write) — out of scope
- Large dataset optimization (chunking, Dask) — out of scope
- Visualization (matplotlib, seaborn) — optional