# Homework 05 - Data Storage

This submission implements a reproducible storage layer for a small stock-price DataFrame. Run `homework05_data-storage_submission.ipynb` from this directory.

## Data Storage

### Folder structure

```text
homework05/
|-- data/
|   |-- raw/          # source-style CSV files
|   `-- processed/    # typed Parquet files
|-- .env.example      # safe configuration template
|-- .gitignore        # prevents .env from being committed
|-- README.md
`-- homework05_data-storage_submission.ipynb
```

### Formats used and why

- CSV is saved in `data/raw/` because it is portable, human-readable, and easy to inspect with many tools.
- Parquet is saved in `data/processed/` because it is compact, efficient to load, and preserves column types such as datetimes more reliably than CSV.

### Environment-driven paths

The notebook loads storage locations from `.env` with `python-dotenv`:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

Create the local file before running the notebook:

```bash
cp .env.example .env
```

The code uses `os.getenv(...)` to read the two variables, converts them to `pathlib.Path` objects, and creates missing directories with `mkdir(parents=True, exist_ok=True)`. Relative paths are interpreted from the directory where the notebook is run. `.env` is intentionally ignored by Git; only `.env.example` should be committed.

### Reading, writing, and validation

`write_df` and `read_df` inspect the filename suffix and route `.csv` files to pandas CSV methods and `.parquet`, `.pq`, or `.parq` files to pandas Parquet methods. `write_df` creates missing parent directories. Both utilities return clear errors for unsupported suffixes, missing files, or an unavailable Parquet engine.

After saving, the notebook reloads both files and checks:

- row and column shapes,
- column order,
- datetime type for `date`,
- text type for `ticker`,
- numeric type for `price`, and
- exact dtype agreement for the critical columns.

