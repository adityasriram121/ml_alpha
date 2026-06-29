# ML Alpha Sandbox

A 12-month, course-style machine learning sandbox built around active discovery and math-code mappings.

## Quick Start

| Resource | Description |
|----------|-------------|
| [LESSON_INDEX.md](LESSON_INDEX.md) | Course portal — every week's lessons and notebooks |
| [guides/](guides/) | Onboarding: setup checklist, daily loop, 12-month map |
| [resources/RESOURCE_MANIFEST.md](resources/RESOURCE_MANIFEST.md) | All textbooks, repos, and courses used |
| [mystery_stack/](mystery_stack/open_mystery_stack.md) | Open bugs, intuitions, and unresolved curiosities |

## Directory Map

```
ml_alpha/
├── curriculum_pathway/      # 16 topic sections with notebooks and practice problems
│   ├── 00_prerequisites/    # NumPy, pandas, matplotlib, linear algebra, calculus, probability
│   ├── 01_foundations/      # ML landscape, statistical learning, end-to-end projects
│   ├── 02_regression/       # Linear regression, gradient descent, optimization
│   ├── 03_classification/   # Logistic regression, LDA/QDA/KNN, metrics
│   ├── 04_resampling_validation/
│   ├── 05_regularization_selection/
│   ├── 06_nonlinear_models/
│   ├── 07_support_vector_machines/
│   ├── 08_trees_ensembles/
│   ├── 09_dimensionality_reduction/
│   ├── 10_unsupervised_learning/
│   ├── 11_survival_multiple_testing/
│   ├── 12_deep_learning_foundations/
│   ├── 13_advanced_deep_learning/
│   ├── 14_reinforcement_learning/
│   └── 15_production_scaling/
├── data/                    # Shared datasets (Auto.csv, imagenet labels, etc.)
├── resources/               # Textbook PDFs, cloned repos, study guides
├── Projects/                # Independent projects (exoplanets, etc.)
├── capstones/               # Monthly capstone artifacts and reports
├── guides/                  # Onboarding docs, daily loop, 12-month roadmap
├── mystery_stack/           # Open Mystery Stack for unresolved questions
└── docker/                  # Docker environment for Jupyter
```

## 2-Day Cycle Loop

1. **Concept Intake**: Read, derive mathematical formulas on paper, run visualization plot.
2. **Concept Build**: Implement algorithm from scratch in NumPy, compare to library module, assert matches.

## Practice Problems

Every curriculum section contains a `practice_100.ipynb` notebook with 100 problems:
- 🧠 **Conceptual** (~35): Explain, compare, true/false with justification
- 📐 **Theoretical** (~30): Derivations, proofs, mathematical formulations
- 💻 **Practical** (~35): Code implementations, data analysis, plotting
