# Shared Datasets

Centralized data directory for the ML Alpha sandbox. Previously, these files were duplicated across multiple curriculum sections.

## Files

| File | Description | Original Source |
|------|-------------|-----------------|
| `Auto.csv` | Auto MPG dataset (CSV format) | ISLP labs — was copied into 7 curriculum sections |
| `Auto.data` | Auto MPG dataset (whitespace-delimited) | ISLP labs — was copied into 7 curriculum sections |
| `imagenet_class_index.json` | ImageNet 1000-class label mapping | Was in `12_deep_learning_foundations/` |

## Usage in Notebooks

If a notebook references `Auto.csv` with a relative path like `pd.read_csv("Auto.csv")`, update it to:

```python
import os
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
# Or from a curriculum notebook:
pd.read_csv("../../data/Auto.csv")
```

## Additional Section-Specific Data

Some sections have their own unique datasets that remain in-place:
- `curriculum_pathway/01_foundations/datasets/` — housing data for the HOML3 end-to-end project
- `Projects/exoplanets/nasa_exoplanets.csv` — exoplanet project data
