# Exoplanet Mass Prediction: Step-by-Step Roadmap

This roadmap is designed following the **Tri-Step Loop** (Visual Scan -> Python Lab -> Deep Read) to guide your bottom-up implementation of the exoplanets project.

---

## Phase 1: Visual Scan & Data Cleaning (EDA)

Before building any models, we need to understand the shape, completeness, and distributions of our data.

- [ ] **1.1 Check Shape & Missing Values**
  - Print the counts of non-null values for each of our columns (`radius`, `orbital_period`, `discovery_year`, `discovery_method`, `distance`, `mass`).
  - *Observation:* Which features have the most missing values? How should we handle them (drop vs. impute)?
- [ ] **1.2 Visualise Feature Distributions**
  - Plot histograms for continuous features (`radius`, `orbital_period`, `distance`, `mass`).
  - *Observation:* Are the distributions highly skewed? Do we need log transformations (e.g., `log_period`)?
- [ ] **1.3 Class Balance for Discovery Method**
  - Plot a bar chart showing the frequency of each `discovery_method`.
  - *Observation:* Are some methods extremely rare? Should we group rare methods into an "Other" category?
- [ ] **1.4 Correlation Analysis**
  - Plot a correlation heatmap of the numerical features.
  - *Observation:* Which features correlate most strongly (positively or negatively) with our target, `mass`?

---

## Phase 2: Feature Engineering & Preprocessing (Python Lab)

Prepare the cleaned data to be fed into scikit-learn algorithms.

- [ ] **2.1 Handle Missing Values**
  - Drop rows where the target variable (`mass`) is missing.
  - For features with missing values, choose a strategy (e.g., median imputation for numerical features).
- [ ] **2.2 Encode Categorical Features**
  - Use One-Hot Encoding (`pd.get_dummies` or `OneHotEncoder`) on `discovery_method`.
- [ ] **2.3 Create Engineered Features**
  - Construct `mass_radius_ratio` (or `radius_to_distance` etc.).
  - Implement a `log_period` feature to stabilize the high variance in orbital periods.
- [ ] **2.4 Train-Test Split**
  - Separate features `X` and target `y`.
  - Split the data into 80% training and 20% testing sets using `train_test_split`.

---

## Phase 3: Model Training & Evaluation (Python Lab)

Implement, evaluate, and compare classical machine learning algorithms.

- [ ] **3.1 Linear Regression Baseline**
  - Train a `LinearRegression` model.
  - Evaluate training and test performance using RMSE and R^2 score.
- [ ] **3.2 Decision Tree Regressor**
  - Train a `DecisionTreeRegressor`.
  - Play with hyperparameters (e.g., `max_depth`) to see how it affects training vs. testing error (overfitting).
- [ ] **3.3 Random Forest Regressor**
  - Train a `RandomForestRegressor`.
  - Compare its performance against the single Decision Tree.
- [ ] **3.4 Model Comparison Table**
  - Build a table comparing the R^2 and RMSE of the three models on the test set.

---

## Phase 4: Socratic Concept Synthesis (Deep Read)

Deepen your understanding of the underlying mathematics and behavior of the models.

- [ ] **4.1 Evaluation Metrics Math**
  - Derive the relationship between MSE and RMSE.
  - Why is R^2 bounded above by 1.0, and what does a negative R^2 score mean?
- [ ] **4.2 The Bias-Variance Trade-Off**
  - Explain how changing `max_depth` in a Decision Tree shifts the model along the Bias-Variance curve.
- [ ] **4.3 Feature Importance**
  - Extract feature importances from the Random Forest model and map them to physical expectations.
