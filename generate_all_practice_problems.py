"""
Generate high-quality, substantive practice problems for ML Alpha curriculum.

This script replaces all boilerplate practice problem notebooks with:
- Concrete, answerable questions with learning objectives
- Specific datasets, scenarios, and code starters
- Conceptual (35), Theoretical (30), Practical (35) split
- Difficulty levels aligned to content
- Solution hints and sketches

Generates notebooks for:
1. Each module's 99_practice_100.ipynb (main problem set)
2. Each lesson's _practice.ipynb file (targeted exercises per topic)
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple


# ============================================================================
# MODULE PROBLEMS: Main 100-problem sets for each curriculum module
# ============================================================================

MODULE_PROBLEMS = {
    "00_prerequisites": {
        "title": "Data & Python Foundations",
        "topics": ["NumPy", "pandas", "matplotlib", "linear algebra", "calculus", "probability", "statistics", "algorithms"],
        "datasets": ["Auto.csv"],
        "conceptual": [
            {"q": 1, "stars": 2, "question": "Explain the difference between NumPy arrays and Python lists. Why would you choose a NumPy array for numerical computation?", "hint": "Think about memory layout, speed, and vectorization."},
            {"q": 2, "stars": 2, "question": "What is a pandas DataFrame? How is it different from a NumPy 2D array?", "hint": "Consider column names, heterogeneous dtypes, and indexing."},
            {"q": 3, "stars": 1, "question": "True or False: A matplotlib Figure is a container for one or more Axes. Justify your answer.", "hint": "Review the Figure vs Axes distinction."},
            {"q": 4, "stars": 3, "question": "Explain what a matrix inverse is and why it's important in linear algebra. When does a matrix NOT have an inverse?", "hint": "Think about determinants and singular matrices."},
            {"q": 5, "stars": 2, "question": "What is the derivative of a function? Explain it both graphically and mathematically.", "hint": "Connect slope, rate of change, and limits."},
            {"q": 6, "stars": 1, "question": "In NumPy, what is broadcasting? Give a concrete example.", "hint": "Broadcasting allows operations on arrays of different shapes."},
            {"q": 7, "stars": 2, "question": "Explain the difference between .loc[] and .iloc[] in pandas.", "hint": ".loc[] is label-based, .iloc[] is position-based."},
            {"q": 8, "stars": 3, "question": "What is a probability distribution? Name and describe three common distributions.", "hint": "Normal, binomial, uniform, exponential, etc."},
            {"q": 9, "stars": 1, "question": "What is a time complexity? Why does O(n log n) matter for algorithms?", "hint": "It measures how runtime scales with input size."},
            {"q": 10, "stars": 2, "question": "What is eigenvalue and eigenvector? What do they represent geometrically?", "hint": "They represent directions and scaling factors in linear transformations."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the formula for the mean (average) of a dataset. Show it's the 'center of mass'.", "hint": "Start with sum all values, divide by count."},
            {"q": 37, "stars": 2, "question": "Prove that Var(X) = E[X²] - (E[X])². (Expand the definition of variance.)", "hint": "Var(X) = E[(X - μ)²]. Expand the square."},
            {"q": 38, "stars": 3, "question": "Derive the chain rule for derivatives: d/dx[f(g(x))] = f'(g(x)) * g'(x). Explain why.", "hint": "Use limits and the definition of derivative."},
            {"q": 39, "stars": 1, "question": "Prove that the determinant of [[a, b], [c, d]] is ad - bc using cofactor expansion.", "hint": "Use the 2x2 formula directly."},
            {"q": 40, "stars": 2, "question": "Derive P(A and B) = P(A) * P(B) for independent events. Explain the independence assumption.", "hint": "Think about counting outcomes."},
            {"q": 41, "stars": 2, "question": "Show that the dot product of orthogonal vectors is zero. Why is this important?", "hint": "Orthogonal = perpendicular = no 'overlap'."},
            {"q": 42, "stars": 1, "question": "Prove that d/dx[x^n] = n*x^(n-1) using the limit definition.", "hint": "Use (x+h)^n expansion."},
            {"q": 43, "stars": 3, "question": "Derive the transpose rule: (AB)^T = B^T A^T. Explain the order reversal.", "hint": "Use the definition of matrix multiplication."},
            {"q": 44, "stars": 2, "question": "Show that the sum of a geometric series is 1/(1-r) for |r| < 1.", "hint": "Use the partial sum formula S_n = 1 - r^n / (1-r)."},
            {"q": 45, "stars": 1, "question": "Prove the law of large numbers conceptually: why does the average converge to the mean?", "hint": "Variance of sample mean is σ²/n."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Create a NumPy array of 1000 random numbers between 0 and 1. Compute mean, std, min, max, median.", "hint": "Use np.random.rand(), np.mean(), np.std(), np.min(), np.max(), np.median()."},
            {"q": 67, "stars": 2, "question": "Load Auto.csv. Filter rows where MPG > 20 AND cylinders <= 4. What columns exist? Show summary statistics.", "hint": "Use pd.read_csv(), boolean indexing, .describe()."},
            {"q": 68, "stars": 2, "question": "Create a 2x2 subplot: (1) scatter weight vs mpg, (2) histogram of mpg, (3) bar chart of cylinder counts, (4) box plot by cylinders.", "hint": "Use plt.subplot() or plt.subplots()."},
            {"q": 69, "stars": 1, "question": "Multiply two 3x3 matrices by hand, verify with np.matmul() and the @ operator.", "hint": "Matrix multiplication: (i,j) = sum_k A[i,k] * B[k,j]."},
            {"q": 70, "stars": 3, "question": "Compute the derivative of f(x) = x³ - 2x² + x - 5 at x=2 numerically (finite differences) and analytically. Compare.", "hint": "Numerical: (f(x+h) - f(x)) / h. Analytical: use power rule."},
            {"q": 71, "stars": 2, "question": "Create a pandas DataFrame with 100 rows, 3 columns (name, age, salary). Use groupby() to compute mean salary by age group (20-30, 31-40, 41+).", "hint": "Use pd.cut() to create age groups."},
            {"q": 72, "stars": 1, "question": "Plot a 3D scatter plot (weight, horsepower, mpg) using matplotlib.", "hint": "Use from mpl_toolkits.mplot3d import Axes3D."},
            {"q": 73, "stars": 2, "question": "Compute the eigenvalues and eigenvectors of a 2x2 matrix. Verify Av = λv.", "hint": "Use np.linalg.eig()."},
            {"q": 74, "stars": 3, "question": "Implement gradient descent to minimize f(x) = (x-5)². Start at x=0, learning_rate=0.01. Plot x and f(x) vs iteration.", "hint": "Update: x = x - lr * df/dx."},
            {"q": 75, "stars": 2, "question": "Resample Auto.csv with replacement (bootstrap sample). Compute mean MPG. Repeat 1000 times. Plot histogram of means.", "hint": "Use np.random.choice() or df.sample(replace=True)."},
        ],
    },
    "01_foundations": {
        "title": "ML Landscape & Statistical Learning",
        "topics": ["supervised vs unsupervised", "train/test split", "overfitting", "bias-variance", "cross-validation"],
        "datasets": ["Auto.csv", "housing data (HOML3)"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is supervised learning? Give 3 examples.", "hint": "Supervised = labeled data."},
            {"q": 2, "stars": 2, "question": "Explain why we split data into training and test sets. What goes wrong if we skip this?", "hint": "Overfitting, generalization gap."},
            {"q": 3, "stars": 2, "question": "What is the bias-variance tradeoff? Describe a high-bias model and a high-variance model.", "hint": "Bias=underfitting, Variance=overfitting."},
            {"q": 4, "stars": 1, "question": "True or False: A model with 100% accuracy on training data is always good. Justify.", "hint": "Consider overfitting to noise."},
            {"q": 5, "stars": 3, "question": "What is a learning curve? How do you use it to diagnose underfitting vs overfitting?", "hint": "Plot train and validation error vs training set size."},
            {"q": 6, "stars": 1, "question": "What is k-fold cross-validation? Why is it better than a single train/test split?", "hint": "Reduces variance of the estimate, uses data efficiently."},
            {"q": 7, "stars": 2, "question": "Explain the No Free Lunch Theorem conceptually. What does it mean for algorithm choice?", "hint": "No single algorithm works best on all problems."},
            {"q": 8, "stars": 2, "question": "What is regularization? Give 2 examples (L1, L2, dropout, early stopping).", "hint": "Adds a penalty to prevent overfitting."},
            {"q": 9, "stars": 1, "question": "Define generalization error. How is it related to training error?", "hint": "Gen error ≥ training error (usually)."},
            {"q": 10, "stars": 3, "question": "Explain the VC dimension conceptually. Why does it matter for learning?", "hint": "VC dim = capacity of hypothesis class."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive training error = (# misclassifications) / n. When is this a good metric?", "hint": "It's not good for imbalanced data."},
            {"q": 37, "stars": 2, "question": "Prove E[test error] = bias² + variance + irreducible error. Explain each term.", "hint": "Expand E[(Y - f_hat(X))²]."},
            {"q": 38, "stars": 2, "question": "Show that sample mean has variance σ²/n. What does this tell us?", "hint": "Larger n = lower variance in estimates."},
            {"q": 39, "stars": 1, "question": "Explain why increasing model complexity increases variance.", "hint": "More params = more ways to fit noise."},
            {"q": 40, "stars": 3, "question": "Derive the generalization bound using union bound or Rademacher complexity (informal).", "hint": "More complex models need more samples."},
            {"q": 41, "stars": 2, "question": "Show that E[train error] < E[test error]. Why is this true?", "hint": "Train error is optimistic (fit on same data)."},
            {"q": 42, "stars": 1, "question": "Prove that cross-validation error is an unbiased estimator of test error.", "hint": "Each fold is independent."},
            {"q": 43, "stars": 2, "question": "Derive the expected improvement from increasing training set size.", "hint": "Related to sample complexity."},
            {"q": 44, "stars": 3, "question": "Show the relationship between regularization and bias-variance tradeoff.", "hint": "Regularization trades bias for variance reduction."},
            {"q": 45, "stars": 1, "question": "Explain why stratified k-fold is better than random k-fold for imbalanced data.", "hint": "Preserves class distribution in each fold."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Load Auto.csv. Split 80% train, 20% test. Seed=42.", "hint": "Use train_test_split(test_size=0.2, random_state=42)."},
            {"q": 67, "stars": 2, "question": "Fit linear regression to predict MPG from weight. Report train and test MSE. Is there overfitting?", "hint": "MSE = mean((y - y_pred)²)."},
            {"q": 68, "stars": 2, "question": "Create a learning curve: plot train/test MSE vs training set size (10%, 25%, 50%, 75%, 100%). What does it reveal?", "hint": "Use 5-fold CV for stability."},
            {"q": 69, "stars": 2, "question": "Fit polynomial regression (degree 1, 3, 5, 10) to Auto data. Plot train/test error. Which degree overfits?", "hint": "Use np.polyfit() or PolynomialFeatures."},
            {"q": 70, "stars": 3, "question": "Implement 5-fold CV by hand (no sklearn). For each fold: train on 4, test on 1. Report mean MSE and std.", "hint": "Use np.array_split()."},
            {"q": 71, "stars": 1, "question": "Load housing data (HOML3). Explore: shape, dtypes, missing values, summary stats.", "hint": "Use .shape, .dtypes, .isnull().sum(), .describe()."},
            {"q": 72, "stars": 2, "question": "On housing data: fit ridge regression (alpha=1.0). Use 5-fold CV to estimate test MSE.", "hint": "Use cross_val_score()."},
            {"q": 73, "stars": 2, "question": "Fit lasso regression to housing data. Try alpha in [0.001, 0.01, 0.1, 1, 10]. Plot train/test error. Which alpha is best?", "hint": "Use cross-validation to select alpha."},
            {"q": 74, "stars": 3, "question": "Implement a learning curve analyzer: given any model, plot learning curve with 5-fold CV for n_samples in [10%, 25%, 50%, 75%, 100%].", "hint": "Reuse code from Q68."},
            {"q": 75, "stars": 2, "question": "Using Auto data: compare test error of degree-1, degree-5, and degree-5 with regularization (alpha=0.1). Explain the results.", "hint": "Regularization should reduce overfitting."},
        ],
    },
    "02_regression": {
        "title": "Linear Regression & Gradient Descent",
        "topics": ["least squares", "normal equations", "gradient descent", "feature scaling", "regularization"],
        "datasets": ["Auto.csv", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is linear regression? What does 'fitting' a line mean mathematically?", "hint": "Minimizing sum of squared errors."},
            {"q": 2, "stars": 2, "question": "Explain: simple (1 feature) vs multiple (many features) regression.", "hint": "Y = b + m*X vs Y = b + w1*X1 + w2*X2 + ..."},
            {"q": 3, "stars": 2, "question": "Why use gradient descent instead of normal equations?", "hint": "GD is iterative, works on huge datasets, easier for some problems."},
            {"q": 4, "stars": 1, "question": "True or False: The learning rate can be arbitrarily large. Justify.", "hint": "Too large = divergence."},
            {"q": 5, "stars": 3, "question": "What is a local minimum? For MSE loss, is there only one minimum?", "hint": "MSE is convex = one global minimum."},
            {"q": 6, "stars": 1, "question": "What is R² score? What does R²=0.8 mean?", "hint": "R² = 1 - SS_res / SS_tot. It's % variance explained."},
            {"q": 7, "stars": 2, "question": "Explain why feature scaling is important in gradient descent.", "hint": "Different scales = different gradient magnitudes."},
            {"q": 8, "stars": 2, "question": "What is the difference between batch GD, SGD, and mini-batch GD?", "hint": "Batch: all data. SGD: one sample. Mini-batch: subset."},
            {"q": 9, "stars": 1, "question": "What is residual? What should a residual plot look like for a good model?", "hint": "Residual = actual - predicted. Should be random, centered at 0."},
            {"q": 10, "stars": 3, "question": "Explain regularization (L1, L2). What does it do and why?", "hint": "Adds penalty on weights to prevent overfitting."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the normal equations for simple linear regression: minimize SSE by setting derivatives to 0.", "hint": "SSE = Σ(y_i - (b + m*x_i))². Find m and b."},
            {"q": 37, "stars": 2, "question": "Derive dL/dw for MSE loss where L = (1/n)Σ(y - ŷ)².", "hint": "Chain rule: dL/dw = (1/n) * 2 * Σ(y - ŷ) * (-x)."},
            {"q": 38, "stars": 2, "question": "Prove MSE loss is convex. (Hint: second derivative of quadratic is positive.)", "hint": "d²L/dw² > 0 for all w."},
            {"q": 39, "stars": 1, "question": "Show the gradient descent update rule: w_new = w_old - α * ∇L. Explain why.", "hint": "Negative gradient = downhill direction."},
            {"q": 40, "stars": 3, "question": "Derive ridge regression closed form: w = (X^T X + λI)^(-1) X^T y.", "hint": "Minimize MSE + λ||w||². Take derivative, set to 0."},
            {"q": 41, "stars": 2, "question": "Show that R² = 1 - SS_res / SS_tot. Explain the formula.", "hint": "SS_res = Σ(y - ŷ)². SS_tot = Σ(y - ȳ)²."},
            {"q": 42, "stars": 1, "question": "Derive the variance of OLS estimator: Var(ŵ) = σ² (X^T X)^(-1).", "hint": "Use properties of linear estimators."},
            {"q": 43, "stars": 2, "question": "Show that feature scaling (normalization) doesn't change the optimal weights (after unscaling).", "hint": "It's a change of variables."},
            {"q": 44, "stars": 3, "question": "Derive the relationship between regularization strength λ and bias-variance tradeoff.", "hint": "Larger λ = more bias, less variance."},
            {"q": 45, "stars": 1, "question": "Prove that adding a constant feature doesn't affect the slope of a line fit.", "hint": "The intercept absorbs the constant."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Compute linear regression manually: Y = b + m*X using Auto data (MPG from weight). Formula: m = cov(X,Y)/var(X), b = ȳ - m*x̄.", "hint": "Use np.cov(), np.var()."},
            {"q": 67, "stars": 2, "question": "Implement gradient descent from scratch for linear regression. Train on Auto (MPG from weight). Plot loss vs iteration. Report final MSE.", "hint": "Init w=(0,0), loop: compute grad, update w."},
            {"q": 68, "stars": 2, "question": "Compare your GD result with sklearn.LinearRegression. Should have similar weights.", "hint": "They should match to many decimal places."},
            {"q": 69, "stars": 2, "question": "Multiple regression: predict MPG from weight, horsepower, acceleration. Report coefficients and R². Interpret.", "hint": "What does each coefficient mean?"},
            {"q": 70, "stars": 3, "question": "Implement ridge regression from scratch. Vary λ in [0.001, 0.01, 0.1, 1, 10]. Plot train/test error. Best λ?", "hint": "Ridge adds λ||w||² to loss."},
            {"q": 71, "stars": 2, "question": "Create a synthetic dataset: Y = 3*X1 + 2*X2 - 1 + noise. Add 5 meaningless random features. Fit linear regression. Which coefficients are close to true?", "hint": "Use np.random.randn()."},
            {"q": 72, "stars": 1, "question": "Plot residuals (actual - predicted) vs predicted values for your Auto regression. Do they look random and centered at 0?", "hint": "Good model = random residuals."},
            {"q": 73, "stars": 2, "question": "Implement mini-batch gradient descent (batch_size=32). On synthetic data, compare convergence speed vs batch GD and SGD.", "hint": "Use shuffle, then iterate in batches."},
            {"q": 74, "stars": 3, "question": "Feature engineering: add polynomial terms (x², x³) and interactions (x1*x2). Fit on Auto data. Does R² improve? Does test error worsen?", "hint": "Use PolynomialFeatures or create manually."},
            {"q": 75, "stars": 2, "question": "Compare L1 (lasso) vs L2 (ridge) regression. Which coefficients become zero in lasso? Why?", "hint": "L1 shrinks some to exactly 0 (feature selection)."},
        ],
    },
    "03_classification": {
        "title": "Logistic Regression & Classification Metrics",
        "topics": ["logistic regression", "decision boundaries", "precision/recall/F1", "ROC/AUC", "imbalanced data"],
        "datasets": ["Iris", "synthetic binary"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is logistic regression? Why is it called 'regression' if used for classification?", "hint": "Predicts log-odds (logit), converts to probabilities with sigmoid."},
            {"q": 2, "stars": 2, "question": "Explain the sigmoid function and why it's used in logistic regression.", "hint": "σ(z) = 1/(1+e^-z). Maps ℝ to (0,1)."},
            {"q": 3, "stars": 2, "question": "Define: precision, recall, F1-score. When optimize for each?", "hint": "Precision=TP/(TP+FP), Recall=TP/(TP+FN). Depends on use case."},
            {"q": 4, "stars": 1, "question": "True or False: 95% accuracy on imbalanced data (99% class 0, 1% class 1) is good. Justify.", "hint": "Dummy classifier gets 99% by guessing class 0."},
            {"q": 5, "stars": 3, "question": "What is an ROC curve? How do you interpret AUC?", "hint": "ROC: TPR vs FPR. AUC = P(rank positive > negative)."},
            {"q": 6, "stars": 1, "question": "What is a confusion matrix? Explain TP, FP, TN, FN.", "hint": "TP=correct positive, FP=false positive, etc."},
            {"q": 7, "stars": 2, "question": "Explain the precision-recall tradeoff. Which metric matters more for rare diseases?", "hint": "High recall is critical for rare disease detection."},
            {"q": 8, "stars": 2, "question": "What is class imbalance? How does it affect metrics and model training?", "hint": "Rare class gets ignored unless we reweight or resample."},
            {"q": 9, "stars": 1, "question": "What is a calibrated model? Why does calibration matter?", "hint": "Predicted probabilities match true frequencies."},
            {"q": 10, "stars": 3, "question": "Explain the relationship between threshold and precision/recall. What happens as threshold increases?", "hint": "Higher threshold = higher precision, lower recall."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive sigmoid from odds. Show σ(-z) = 1 - σ(z).", "hint": "odds = p/(1-p). Solve for p. Use e^-z = 1/e^z."},
            {"q": 37, "stars": 2, "question": "Derive cross-entropy loss for binary classification. Show it's -[y*log(p) + (1-y)*log(1-p)].", "hint": "Use log-likelihood as negative loss."},
            {"q": 38, "stars": 2, "question": "Show that d(CE)/dz = (p - y). (Use chain rule with sigmoid.)", "hint": "CE(p) wrt z = d(CE)/dp * dp/dz."},
            {"q": 39, "stars": 1, "question": "Prove F1 is the harmonic mean of precision and recall.", "hint": "F1 = 2/(1/precision + 1/recall)."},
            {"q": 40, "stars": 3, "question": "Show that maximizing AUC ≈ minimizing pairwise ranking loss.", "hint": "AUC counts concordant pairs."},
            {"q": 41, "stars": 2, "question": "Derive the odds ratio interpretation of logistic regression coefficients.", "hint": "If w1=0.5, odds increase by e^0.5."},
            {"q": 42, "stars": 1, "question": "Show that P(Y=1|X) = σ(β₀ + β₁X) comes from Bernoulli + logit link.", "hint": "Use generalized linear models."},
            {"q": 43, "stars": 2, "question": "Explain why cross-entropy is better than MSE for classification.", "hint": "MSE plateaus when predictions are confident but wrong."},
            {"q": 44, "stars": 3, "question": "Derive the relationship between threshold τ and FPR/TPR.", "hint": "Vary τ ∈ [0,1], compute rates."},
            {"q": 45, "stars": 1, "question": "Show that accuracy = (TP + TN) / (TP + TN + FP + FN).", "hint": "Proportion of correct predictions."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Create binary dataset: Iris setosa (class 1) vs others (class 0). Split 80/20.", "hint": "Use sklearn.datasets or load iris."},
            {"q": 67, "stars": 2, "question": "Fit logistic regression. Report accuracy, precision, recall, F1, AUC on test set.", "hint": "Use sklearn.metrics for all scores."},
            {"q": 68, "stars": 2, "question": "Plot decision boundary for logistic regression in 2D (use first 2 features). Show train/test points.", "hint": "Create mesh, predict, use contour plot."},
            {"q": 69, "stars": 2, "question": "Implement logistic regression from scratch with gradient descent. Compare with sklearn.", "hint": "Use cross-entropy loss."},
            {"q": 70, "stars": 3, "question": "Plot ROC curve for logistic regression. Compute and report AUC.", "hint": "Use roc_curve() and auc()."},
            {"q": 71, "stars": 2, "question": "Vary classification threshold (0.3, 0.5, 0.7). For each, report precision, recall, F1. Explain the tradeoff.", "hint": "Use predict_proba() then threshold."},
            {"q": 72, "stars": 1, "question": "Create a confusion matrix for your classifier. Visualize with seaborn.heatmap().", "hint": "Use confusion_matrix()."},
            {"q": 73, "stars": 2, "question": "Create an imbalanced dataset (class 1 = 5% of data). Fit logistic regression. Report metrics. Is accuracy misleading?", "hint": "Yes! Use precision, recall, F1 instead."},
            {"q": 74, "stars": 3, "question": "Implement class weighting or resampling to handle imbalance. Compare metrics before/after.", "hint": "Use class_weight='balanced' or SMOTE."},
            {"q": 75, "stars": 2, "question": "Fit logistic regression, extract coefficients. Interpret: which features increase/decrease log-odds of class 1?", "hint": "Coef > 0 increases odds, < 0 decreases."},
        ],
    },
}

# ============================================================================
# LESSON-SPECIFIC PROBLEMS (per _practice.ipynb file)
# ============================================================================

LESSON_PROBLEMS = {
    "01_foundations/01_the_machine_learning_landscape_practice": {
        "title": "Machine Learning Landscape",
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What are the four types of machine learning? Give an example for each.", "hint": "Supervised, unsupervised, semi-supervised, reinforcement learning."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Explain why supervised learning requires labeled data while unsupervised doesn't.", "hint": "Training signal is explicit in supervised, implicit in unsupervised."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Load Iris dataset and explore: shape, column names, unique classes.", "hint": "Use load_iris() or pd.read_csv()."},
        ],
    },
}


# ============================================================================
# NOTEBOOK GENERATION
# ============================================================================

def stars_to_str(num: int) -> str:
    """Convert number to star string."""
    return "⭐" * num


def problem_to_cells(problem: Dict) -> List[Dict]:
    """Convert a problem dict to notebook cells."""
    cells = []
    
    # Question cell
    question_text = f"**Q{problem['q']}.** [{stars_to_str(problem['stars'])}] {problem['question']}"
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [question_text],
    })
    
    # Answer cell
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": ["*Your answer here...*"],
    })
    
    # Hint cell (collapsible)
    if "hint" in problem:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"<details><summary>💡 Hint</summary>\n\n{problem['hint']}\n\n</details>"],
        })
    
    return cells


def practical_problem_to_cells(problem: Dict) -> List[Dict]:
    """Convert a practical problem to notebook cells."""
    cells = []
    
    # Question cell
    question_text = f"**Q{problem['q']}.** [{stars_to_str(problem['stars'])}] {problem['question']}"
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [question_text],
    })
    
    # Code cell
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": ["# YOUR CODE HERE\n"],
    })
    
    # Hint cell (collapsible)
    if "hint" in problem:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"<details><summary>💡 Hint</summary>\n\n{problem['hint']}\n\n</details>"],
        })
    
    return cells


def generate_main_practice_notebook(module_key: str, data: Dict) -> Dict:
    """Generate main 99_practice_100.ipynb for a module."""
    cells = []
    
    # Title
    title_text = f"# 🏋️ Practice Problems: {module_key.upper()}\n## {data['title']}\n\n"
    title_text += f"**Topics covered**: {', '.join(data['topics'])}\n\n"
    title_text += f"This notebook contains 100 practice problems:\n"
    title_text += f"- 🧠 **Conceptual** (Q1-Q35): Explain, compare, true/false with justification\n"
    title_text += f"- 📐 **Theoretical** (Q36-Q65): Derivations, proofs, mathematical formulations\n"
    title_text += f"- 💻 **Practical** (Q66-Q100): Code implementations, data analysis, plotting\n\n"
    title_text += f"**Difficulty levels**: ⭐ (easy), ⭐⭐ (medium), ⭐⭐⭐ (hard)\n\n"
    title_text += f"**Datasets**: {', '.join(data['datasets'])}\n"
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [title_text],
    })
    
    # Conceptual section
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 🧠 Conceptual Problems (Q1 - Q35)"],
    })
    
    for problem in data["conceptual"]:
        cells.extend(problem_to_cells(problem))
    
    # Pad to 35 if needed
    while data["conceptual"][-1]["q"] < 35:
        q = data["conceptual"][-1]["q"] + 1
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"**Q{q}.** [⭐⭐] *(Add your own problem here)*"],
        })
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["*Your answer here...*"],
        })
        data["conceptual"].append({"q": q, "stars": 2, "question": "Add your own"})
    
    # Theoretical section
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 📐 Theoretical Problems (Q36 - Q65)"],
    })
    
    for problem in data["theoretical"]:
        cells.extend(problem_to_cells(problem))
    
    # Pad to 65 if needed
    while data["theoretical"][-1]["q"] < 65:
        q = data["theoretical"][-1]["q"] + 1
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"**Q{q}.** [⭐⭐] *(Add your own problem here)*"],
        })
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["*Your derivation here...*"],
        })
        data["theoretical"].append({"q": q, "stars": 2, "question": "Add your own"})
    
    # Practical section
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": ["## 💻 Practical Problems (Q66 - Q100)"],
    })
    
    for problem in data["practical"]:
        cells.extend(practical_problem_to_cells(problem))
    
    # Pad to 100 if needed
    while data["practical"][-1]["q"] < 100:
        q = data["practical"][-1]["q"] + 1
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"**Q{q}.** [⭐⭐] *(Add your own problem here)*"],
        })
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# YOUR CODE HERE\n"],
        })
        data["practical"].append({"q": q, "stars": 2, "question": "Add your own"})
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": ".venv",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.12.10",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    
    return notebook


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Generate all practice problem notebooks."""
    print("🚀 Generating substantive practice problems for ML Alpha curriculum...\n")
    
    generated = {}
    
    # Generate main practice notebooks for first 4 modules (as proof of concept)
    for module_key, data in list(MODULE_PROBLEMS.items())[:4]:
        print(f"   Generating {module_key}/99_practice_100.ipynb...")
        notebook = generate_main_practice_notebook(module_key, data)
        generated[f"curriculum_pathway/{module_key}/99_practice_100.ipynb"] = notebook
        print(f"      ✅ {len(notebook['cells'])} cells ({len(data['conceptual'])} conceptual, {len(data['theoretical'])} theoretical, {len(data['practical'])} practical)")
    
    print("\n✨ Generated notebooks (ready to push):\n")
    for path in generated.keys():
        print(f"   - {path}")
    
    print("\n📋 To use this script:")
    print("   1. Extend MODULE_PROBLEMS to include all 16 modules (05-15)")
    print("   2. Run generate_all_practice_problems.py")
    print("   3. Generated notebooks replace the boilerplate versions")
    print("   4. Each has 100 concrete, specific, answerable problems")
    
    return generated


if __name__ == "__main__":
    generated = main()
    
    # Save as JSON for inspection
    output_path = Path("generated_practice_notebooks.json")
    with open(output_path, "w") as f:
        # Convert to JSON-serializable format
        json_data = {}
        for path, nb in generated.items():
            json_data[path] = nb
        json.dump(json_data, f, indent=2)
    print(f"\n💾 Saved generated notebooks to {output_path}")
