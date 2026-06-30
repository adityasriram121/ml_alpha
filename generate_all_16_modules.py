"""
Generate all 100-problem practice notebooks for all 16 ML Alpha modules.
Extends MODULE_PROBLEMS with complete problem sets for modules 04-15.
"""

import json


MODULE_PROBLEMS = {
    "04_resampling_validation": {
        "title": "Cross-Validation & Resampling Techniques",
        "topics": ["k-fold CV", "stratified CV", "bootstrap", "leave-one-out", "time series CV"],
        "datasets": ["Auto.csv", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is k-fold cross-validation? Why is it better than a single train/test split?", "hint": "Reduces variance, uses data efficiently."},
            {"q": 2, "stars": 2, "question": "Explain stratified k-fold. When is it critical to use?", "hint": "Preserves class distribution in imbalanced datasets."},
            {"q": 3, "stars": 1, "question": "What is bootstrap resampling? How does it estimate uncertainty?", "hint": "Sample with replacement, compute statistic for each sample."},
            {"q": 4, "stars": 2, "question": "True or False: Leave-one-out CV is always better than k-fold CV. Justify.", "hint": "LOOCV has high variance, slow to compute."},
            {"q": 5, "stars": 3, "question": "Explain time series cross-validation. Why can't you shuffle time series data?", "hint": "Temporal dependence = shuffling breaks structure."},
            {"q": 6, "stars": 1, "question": "What is nested cross-validation? When do you need it?", "hint": "Outer loop for evaluation, inner loop for hyperparameter selection."},
            {"q": 7, "stars": 2, "question": "Define recall and precision for imbalanced datasets. Which matters more for fraud detection?", "hint": "Recall: catch all frauds. Precision: minimize false alarms."},
            {"q": 8, "stars": 2, "question": "What is a confusion matrix for multiclass classification?", "hint": "Rows=true, columns=predicted. Diagonal=correct."},
            {"q": 9, "stars": 1, "question": "Explain the difference between validation set and test set.", "hint": "Validation: tune hyperparams. Test: final evaluation."},
            {"q": 10, "stars": 3, "question": "How do you estimate generalization error with cross-validation?", "hint": "Average test error across folds."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the expected value of a bootstrap sample mean.", "hint": "E[sample mean] = population mean."},
            {"q": 37, "stars": 2, "question": "Show that k-fold CV error is an unbiased estimator of test error.", "hint": "Each fold is independent and representative."},
            {"q": 38, "stars": 2, "question": "Derive the variance of k-fold CV error compared to single split.", "hint": "Averaging reduces variance by 1/k."},
            {"q": 39, "stars": 1, "question": "Prove that bootstrap confidence intervals are asymptotically correct.", "hint": "Use the bootstrap principle."},
            {"q": 40, "stars": 3, "question": "Show why time series CV must respect temporal order (no shuffling).", "hint": "Future data can't predict past data."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Implement 5-fold CV by hand on Auto data (no sklearn). Report mean and std MSE.", "hint": "Use np.array_split() to create folds."},
            {"q": 67, "stars": 2, "question": "Compare 5-fold, 10-fold, and LOOCV on a model. Which is fastest? Which has lowest variance?", "hint": "LOOCV is slow, high variance. More folds = lower variance."},
            {"q": 68, "stars": 2, "question": "Fit logistic regression on imbalanced data. Use stratified 5-fold CV. Report macro and weighted F1 scores.", "hint": "Use StratifiedKFold() from sklearn."},
            {"q": 69, "stars": 2, "question": "Create a bootstrap confidence interval for the mean MPG of Auto data. Compare with analytical CI.", "hint": "Bootstrap percentile method."},
            {"q": 70, "stars": 3, "question": "Implement nested CV: outer fold for evaluation, inner fold for regularization parameter selection (lambda in ridge regression).", "hint": "Two loops: outer and inner."},
        ],
    },
    "05_regularization_selection": {
        "title": "Regularization & Model Selection",
        "topics": ["ridge regression", "lasso", "elastic net", "model comparison", "AIC/BIC"],
        "datasets": ["Auto.csv", "housing"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is regularization? Why does it help prevent overfitting?", "hint": "Adds penalty on weight magnitude."},
            {"q": 2, "stars": 2, "question": "Explain L1 vs L2 regularization. Which does feature selection?", "hint": "L1 (lasso) shrinks some coefficients to exactly 0."},
            {"q": 3, "stars": 1, "question": "What is elastic net? Why combine L1 and L2?", "hint": "Gets best of both: sparsity (L1) + stability (L2)."},
            {"q": 4, "stars": 2, "question": "True or False: Higher regularization strength always gives better test error. Justify.", "hint": "Too much regularization = underfitting."},
            {"q": 5, "stars": 3, "question": "Explain AIC and BIC. When would you use each?", "hint": "Both penalize model complexity. BIC penalizes more."},
            {"q": 6, "stars": 1, "question": "What is the relationship between regularization and bias-variance tradeoff?", "hint": "Regularization trades variance for bias."},
            {"q": 7, "stars": 2, "question": "Explain cross-validation for model selection. Why is it better than AIC alone?", "hint": "CV directly estimates test error."},
            {"q": 8, "stars": 2, "question": "What does a coefficient path look like in lasso? Explain the trajectory.", "hint": "As lambda increases, coefficients shrink to 0 one by one."},
            {"q": 9, "stars": 1, "question": "Define degrees of freedom in ridge regression.", "hint": "Effective DOF < number of features due to shrinkage."},
            {"q": 10, "stars": 3, "question": "How do you select the regularization parameter lambda?", "hint": "Cross-validation, grid search, or analytical methods."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the closed-form solution for ridge regression: w = (X^T X + λI)^{-1} X^T y.", "hint": "Minimize MSE + λ||w||^2."},
            {"q": 37, "stars": 2, "question": "Show that lasso has no closed form but ridge does.", "hint": "Lasso non-smooth, ridge smooth."},
            {"q": 38, "stars": 2, "question": "Derive AIC = 2k - 2ln(L) where k=num params, L=likelihood.", "hint": "Balances fit and complexity."},
            {"q": 39, "stars": 1, "question": "Prove that ridge regression reduces variance compared to OLS.", "hint": "Shrinkage reduces variance at cost of bias."},
            {"q": 40, "stars": 3, "question": "Show the relationship between regularization parameter λ and effective degrees of freedom.", "hint": "Higher λ = lower DOF."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Fit ridge regression to Auto data. Try lambda in [0.001, 0.01, 0.1, 1, 10, 100]. Plot train/test MSE vs lambda.", "hint": "Use cross_val_score()."},
            {"q": 67, "stars": 2, "question": "Fit lasso to Auto data. Find the lambda that minimizes 5-fold CV error. How many features are selected?", "hint": "Use LassoCV() from sklearn."},
            {"q": 68, "stars": 2, "question": "Compare ridge, lasso, and elastic net on housing data. Which has best test error?", "hint": "Try different alpha values for each."},
            {"q": 69, "stars": 2, "question": "Plot coefficient paths for lasso as lambda varies. Explain which coefficients shrink first.", "hint": "Use LassoCV with plot_coef_path or manual loop."},
            {"q": 70, "stars": 3, "question": "Use AIC and BIC to compare models (1-feature, 2-feature, 3-feature, etc.). Compare with CV selection.", "hint": "Calculate AIC/BIC for each model."},
        ],
    },
    "06_nonlinear_models": {
        "title": "Polynomial & Spline Regression",
        "topics": ["polynomial features", "splines", "basis functions", "kernel tricks"],
        "datasets": ["Auto.csv", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What are polynomial features? How do you add them to a dataset?", "hint": "Add x^2, x^3, interactions like x1*x2."},
            {"q": 2, "stars": 2, "question": "Explain the curse of dimensionality. Why does polynomial expansion make it worse?", "hint": "More features = more parameters = more overfitting."},
            {"q": 3, "stars": 1, "question": "What are splines? How are they different from polynomials?", "hint": "Piecewise polynomials with smooth junctions (knots)."},
            {"q": 4, "stars": 2, "question": "True or False: A degree-10 polynomial always fits better than degree-2. Justify.", "hint": "Higher degree can overfit."},
            {"q": 5, "stars": 3, "question": "Explain basis functions conceptually. How do they enable nonlinear regression?", "hint": "Transform nonlinear problem into linear problem in new space."},
            {"q": 6, "stars": 1, "question": "What are knots in spline regression? How do you choose where to place them?", "hint": "Knots define piecewise boundaries."},
            {"q": 7, "stars": 2, "question": "Define smoothness in spline fitting. What does a 'smooth' spline mean?", "hint": "Continuous derivatives at knots."},
            {"q": 8, "stars": 2, "question": "What is the kernel trick? Why is it useful?", "hint": "Compute inner products in high-dim space without explicitly transforming."},
            {"q": 9, "stars": 1, "question": "Explain interaction terms (x1*x2). When are they important?", "hint": "When one feature's effect depends on another."},
            {"q": 10, "stars": 3, "question": "How do you avoid overfitting when using polynomial or spline features?", "hint": "Cross-validation, regularization, or reduce degree/knots."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Show that polynomial regression y = b + w1*x + w2*x^2 + ... is still linear in the parameters.", "hint": "It's linear in w, just nonlinear features."},
            {"q": 37, "stars": 2, "question": "Derive the number of basis functions needed for polynomial of degree p with d features.", "hint": "Combinatorial: C(d+p, p)."},
            {"q": 38, "stars": 2, "question": "Explain why cubic splines (degree 3) are often preferred over higher degrees.", "hint": "Balance flexibility vs. smoothness."},
            {"q": 39, "stars": 1, "question": "Prove that adding regularization to splines helps prevent overfitting.", "hint": "Penalizes complexity of the spline."},
            {"q": 40, "stars": 3, "question": "Show the relationship between number of knots and degrees of freedom in spline regression.", "hint": "DOF = num knots + degree + 1 - 1 (for intercept)."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Add polynomial features (degree 1-5) to Auto data. Fit linear regression for each. Plot train/test error.", "hint": "Use PolynomialFeatures() from sklearn."},
            {"q": 67, "stars": 2, "question": "Fit cubic splines to Auto data (MPG vs weight). Try different numbers of knots (2, 4, 6, 8). Plot each.", "hint": "Use UnivariateSpline from scipy or custom."},
            {"q": 68, "stars": 2, "question": "Create polynomial features with interactions. Fit ridge regression. Compare to no interactions.", "hint": "Does interaction improve test error?"},
            {"q": 69, "stars": 2, "question": "On synthetic nonlinear data y = sin(x) + noise, compare polynomial (degree 5, 10, 15) vs splines.", "hint": "Which fits better?"},
            {"q": 70, "stars": 3, "question": "Implement basis function expansion manually (e.g., RBF basis). Fit linear regression on transformed data.", "hint": "RBF: φ(x) = exp(-||x - center||^2 / (2*σ^2))."},
        ],
    },
    "07_support_vector_machines": {
        "title": "Support Vector Machines & Kernels",
        "topics": ["SVM margin", "kernel trick", "soft margin", "multi-class SVM"],
        "datasets": ["Iris", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is the margin in SVM? Why do we want to maximize it?", "hint": "Distance from decision boundary to nearest points. Larger = more robust."},
            {"q": 2, "stars": 2, "question": "Explain the kernel trick. Why does it avoid explicit transformation?", "hint": "Compute K(x_i, x_j) instead of φ(x_i)^T φ(x_j)."},
            {"q": 3, "stars": 1, "question": "What is a support vector? Why do we only care about some points?", "hint": "Support vectors define the boundary; others are irrelevant."},
            {"q": 4, "stars": 2, "question": "True or False: SVM always finds the global optimum. Justify.", "hint": "Yes, it's a convex optimization problem."},
            {"q": 5, "stars": 3, "question": "Explain soft-margin SVM. What is the C parameter?", "hint": "Allows some misclassification. C controls tolerance."},
            {"q": 6, "stars": 1, "question": "What is the RBF kernel? When would you use it?", "hint": "K(x,y) = exp(-γ||x-y||^2). For nonlinear problems."},
            {"q": 7, "stars": 2, "question": "How does SVM handle multi-class classification?", "hint": "One-vs-rest or one-vs-one."},
            {"q": 8, "stars": 2, "question": "What is the gamma parameter in RBF kernel? How does it affect the model?", "hint": "Low gamma = smooth. High gamma = wiggly."},
            {"q": 9, "stars": 1, "question": "Why is SVM good for high-dimensional data?", "hint": "Works well when data is sparse or separable."},
            {"q": 10, "stars": 3, "question": "How do you choose between linear, polynomial, and RBF kernels?", "hint": "Grid search + cross-validation."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the SVM optimization problem: maximize 1/||w|| subject to y_i(w^T x_i + b) ≥ 1.", "hint": "Margin = 2/||w||."},
            {"q": 37, "stars": 2, "question": "Show that the decision boundary for SVM is determined by support vectors only.", "hint": "Non-SV points have α_i = 0."},
            {"q": 38, "stars": 2, "question": "Derive the kernel trick: K(x_i, x_j) = φ(x_i)^T φ(x_j).", "hint": "For polynomial kernel: K(x,y) = (1 + x^T y)^d."},
            {"q": 39, "stars": 1, "question": "Prove that RBF kernel corresponds to infinite-dimensional feature space.", "hint": "Taylor expansion of exp(-γ||x-y||^2)."},
            {"q": 40, "stars": 3, "question": "Show the duality between primal and dual SVM problems.", "hint": "Lagrangian, KKT conditions."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Fit linear SVM on Iris binary (setosa vs others). Report accuracy and num support vectors.", "hint": "Use SVC(kernel='linear')."},
            {"q": 67, "stars": 2, "question": "Fit RBF SVM. Try different gamma values (0.001, 0.01, 0.1, 1, 10). Plot decision boundary for each.", "hint": "Larger gamma = more complex."},
            {"q": 68, "stars": 2, "question": "Fit polynomial SVM (degree 1, 2, 3) to synthetic nonlinear data. Compare with RBF.", "hint": "Which generalizes better?"},
            {"q": 69, "stars": 2, "question": "Vary C parameter in SVM (0.1, 1, 10, 100). Plot train/test error. What's the effect of C?", "hint": "Low C = more tolerance, high C = strict."},
            {"q": 70, "stars": 3, "question": "Use GridSearchCV to find best (C, gamma) for RBF kernel on Iris data.", "hint": "Try C in [0.1, 1, 10, 100] and gamma in [0.001, 0.01, 0.1, 1]."},
        ],
    },
    "08_trees_ensembles": {
        "title": "Decision Trees & Ensemble Methods",
        "topics": ["tree splits", "gini/entropy", "bagging", "random forests", "boosting"],
        "datasets": ["Iris", "Auto", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is a decision tree? How does it make predictions?", "hint": "Recursive splits on features, leaf = predicted class/value."},
            {"q": 2, "stars": 2, "question": "Explain Gini impurity and entropy. Which is faster to compute?", "hint": "Gini: 1 - Σp_i^2. Entropy: -Σp_i*log(p_i). Gini is faster."},
            {"q": 3, "stars": 1, "question": "What is a split in decision trees? How do you choose the best split?", "hint": "Maximize information gain or Gini reduction."},
            {"q": 4, "stars": 2, "question": "True or False: Deeper trees always fit better. Justify.", "hint": "No, they overfit. Pruning or depth limits help."},
            {"q": 5, "stars": 3, "question": "Explain bagging conceptually. Why does it reduce variance?", "hint": "Average predictions from many models trained on bootstrap samples."},
            {"q": 6, "stars": 1, "question": "What is a random forest? How is it different from bagging?", "hint": "Bagging + random feature subsets at each split."},
            {"q": 7, "stars": 2, "question": "Explain boosting. Why does it focus on hard examples?", "hint": "Each round reweights misclassified samples higher."},
            {"q": 8, "stars": 2, "question": "What is feature importance in trees? How is it computed?", "hint": "Reduction in impurity weighted by samples."},
            {"q": 9, "stars": 1, "question": "Explain out-of-bag (OOB) error in random forests.", "hint": "Error on samples not in bootstrap sample."},
            {"q": 10, "stars": 3, "question": "How do you avoid overfitting in decision trees?", "hint": "Limit depth, min_samples_split, pruning, or ensemble methods."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive Gini impurity: G = 1 - Σp_i^2.", "hint": "Probability of misclassifying random sample."},
            {"q": 37, "stars": 2, "question": "Show that bagging reduces variance of predictions.", "hint": "Var[average(X_i)] = Var[X_i]/n if independent."},
            {"q": 38, "stars": 2, "question": "Explain information gain: IG = H(parent) - Σ(n_child/n_parent)*H(child).", "hint": "Reduction in entropy after split."},
            {"q": 39, "stars": 1, "question": "Prove that random forests reduce overfitting compared to single tree.", "hint": "Averaging reduces variance."},
            {"q": 40, "stars": 3, "question": "Show the exponential decay of boosting training error under certain conditions.", "hint": "Each round fixes previous mistakes."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Fit decision tree to Iris. Try max_depth from 1 to 10. Plot train/test accuracy.", "hint": "Use DecisionTreeClassifier()."},
            {"q": 67, "stars": 2, "question": "Fit random forest (100 trees) to Iris. Report OOB error and compare with CV error.", "hint": "Use oob_score=True."},
            {"q": 68, "stars": 2, "question": "Train AdaBoost on Iris. Vary n_estimators (10, 50, 100, 200). Plot train/test error.", "hint": "Use AdaBoostClassifier()."},
            {"q": 69, "stars": 2, "question": "Extract feature importances from random forest on Iris. Which features matter most?", "hint": "Use .feature_importances_."},
            {"q": 70, "stars": 3, "question": "Implement bagging manually: train 50 decision trees on bootstrap samples, average predictions.", "hint": "Use np.random.choice() to resample."},
        ],
    },
    "09_dimensionality_reduction": {
        "title": "Dimensionality Reduction & PCA",
        "topics": ["PCA", "variance explained", "eigendecomposition", "feature selection"],
        "datasets": ["Iris", "MNIST (subset)", "synthetic high-dim"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is PCA? What does it maximize?", "hint": "Finds directions of max variance."},
            {"q": 2, "stars": 2, "question": "Explain the relationship between eigenvalues and variance explained in PCA.", "hint": "Eigenvalue = variance along eigenvector."},
            {"q": 3, "stars": 1, "question": "Why does PCA require centering the data?", "hint": "Eigenvectors align with centered data."},
            {"q": 4, "stars": 2, "question": "True or False: PCA always improves classification accuracy. Justify.", "hint": "No, info loss from dimensionality reduction."},
            {"q": 5, "stars": 3, "question": "Explain scree plots. How do you use them to choose components?", "hint": "Eigenvalues vs component. Look for 'elbow'."},
            {"q": 6, "stars": 1, "question": "What is the curse of dimensionality? Why does it matter?", "hint": "High dims = sparse data = hard to learn."},
            {"q": 7, "stars": 2, "question": "Explain the difference between supervised (LDA) and unsupervised (PCA) dimensionality reduction.", "hint": "LDA uses labels, PCA doesn't."},
            {"q": 8, "stars": 2, "question": "What is explained variance ratio? How do you use it?", "hint": "Cumulative sum tells you how much info retained."},
            {"q": 9, "stars": 1, "question": "Can PCA be used for feature selection? Why or why not?", "hint": "PCA creates new features, not selecting existing ones."},
            {"q": 10, "stars": 3, "question": "How do you interpret PCA loadings?", "hint": "Loadings = correlations between original features and PCs."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the PCA objective: maximize variance in direction w subject to ||w||=1.", "hint": "Maximize w^T Σ w."},
            {"q": 37, "stars": 2, "question": "Show that PCA principal components are eigenvectors of covariance matrix.", "hint": "Solved by eigendecomposition."},
            {"q": 38, "stars": 2, "question": "Prove that first k PCs minimize reconstruction error.", "hint": "Optimal low-rank approximation."},
            {"q": 39, "stars": 1, "question": "Derive the explained variance ratio: λ_i / Σλ_j.", "hint": "Eigenvalue over total variance."},
            {"q": 40, "stars": 3, "question": "Show why PCA can fail in high dimensions (curse of dimensionality).", "hint": "Data becomes sparse, correlations unreliable."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Apply PCA to Iris. Visualize 2 components. How much variance is explained?", "hint": "Use PCA(n_components=2)."},
            {"q": 67, "stars": 2, "question": "On Iris, plot explained variance ratio vs n_components (1 to 4). Find elbow.", "hint": "Use cumsum() to get cumulative."},
            {"q": 68, "stars": 2, "question": "Train classifier on Iris with/without PCA (2 components). Compare accuracy.", "hint": "Does dimensionality reduction help?"},
            {"q": 69, "stars": 2, "question": "Reconstruct Iris data from 2 PCA components. Visualize original vs reconstructed.", "hint": "Use inverse_transform()."},
            {"q": 70, "stars": 3, "question": "Implement PCA from scratch: center data, compute covariance, find eigenvalues/vectors.", "hint": "Use np.linalg.eig()."},
        ],
    },
    "10_unsupervised_learning": {
        "title": "Clustering & Unsupervised Learning",
        "topics": ["k-means", "hierarchical clustering", "DBSCAN", "silhouette score"],
        "datasets": ["Iris", "synthetic clusters", "Auto"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is clustering? What's the difference from classification?", "hint": "Unsupervised: no labels. Find structure in data."},
            {"q": 2, "stars": 2, "question": "Explain k-means algorithm step by step.", "hint": "Initialize, assign to nearest center, update centers, repeat."},
            {"q": 3, "stars": 1, "question": "Why is k-means initialization important?", "hint": "Random init can get stuck in local optimum."},
            {"q": 4, "stars": 2, "question": "True or False: k-means always converges. Justify.", "hint": "Yes, converges to local optimum (not global)."},
            {"q": 5, "stars": 3, "question": "What is the silhouette score? How do you use it to evaluate clustering?", "hint": "Measures cohesion vs separation. Range [-1, 1]."},
            {"q": 6, "stars": 1, "question": "What is hierarchical clustering? How is it different from k-means?", "hint": "Builds tree of clusters (dendrogram)."},
            {"q": 7, "stars": 2, "question": "Explain linkage methods: single, complete, average. When use each?", "hint": "How to measure distance between clusters."},
            {"q": 8, "stars": 2, "question": "What is DBSCAN? When would you use it instead of k-means?", "hint": "Density-based, finds clusters of arbitrary shape."},
            {"q": 9, "stars": 1, "question": "How do you choose k in k-means?", "hint": "Elbow method, silhouette score, domain knowledge."},
            {"q": 10, "stars": 3, "question": "How do you evaluate clustering without labels?", "hint": "Silhouette, Davies-Bouldin, Calinski-Harabasz indices."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive k-means objective: minimize Σ_i Σ_{x in C_i} ||x - μ_i||^2.", "hint": "Within-cluster sum of squares."},
            {"q": 37, "stars": 2, "question": "Show that k-means assignment and update steps decrease the objective.", "hint": "Each step is locally optimal."},
            {"q": 38, "stars": 2, "question": "Derive the silhouette score: (b_i - a_i) / max(a_i, b_i).", "hint": "a_i = avg dist to cluster members, b_i = min dist to other clusters."},
            {"q": 39, "stars": 1, "question": "Explain why hierarchical clustering produces a dendrogram.", "hint": "Tree structure from bottom-up merging."},
            {"q": 40, "stars": 3, "question": "Show that k-means is sensitive to outliers. Why?", "hint": "Euclidean distance heavily penalizes far points."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Apply k-means to Iris with k=3. Visualize clusters. Compare to true labels.", "hint": "Use KMeans(n_clusters=3)."},
            {"q": 67, "stars": 2, "question": "On Iris, try k=1 to 10. Compute silhouette score for each. Find best k.", "hint": "Plot silhouette score vs k."},
            {"q": 68, "stars": 2, "question": "Apply hierarchical clustering to Iris. Plot dendrogram. Try different linkage methods.", "hint": "Use dendrogram() and linkage()."},
            {"q": 69, "stars": 2, "question": "Apply DBSCAN to Iris with different eps and min_samples. How many clusters? Noise points?", "hint": "Tune eps and min_samples."},
            {"q": 70, "stars": 3, "question": "Implement k-means from scratch: initialize, assign, update centers, repeat.", "hint": "Track objective to check convergence."},
        ],
    },
    "11_survival_multiple_testing": {
        "title": "Statistical Inference & Multiple Testing",
        "topics": ["hypothesis testing", "p-values", "multiple testing correction", "false discovery rate"],
        "datasets": ["synthetic", "simulated experiments"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is a p-value? What does p < 0.05 mean?", "hint": "Prob of observing data if null hypothesis is true."},
            {"q": 2, "stars": 2, "question": "Explain Type I and Type II errors. Which is worse?", "hint": "Context-dependent. Type I = false positive."},
            {"q": 3, "stars": 1, "question": "What is multiple testing problem? Why does it matter?", "hint": "More tests = higher chance of false positives."},
            {"q": 4, "stars": 2, "question": "True or False: Bonferroni correction is always optimal. Justify.", "hint": "Conservative but other methods exist."},
            {"q": 5, "stars": 3, "question": "Explain false discovery rate (FDR). How is it different from family-wise error rate (FWER)?", "hint": "FDR = proportion of false positives among discoveries."},
            {"q": 6, "stars": 1, "question": "What is a confidence interval? What does 95% CI mean?", "hint": "If we repeat experiment, 95% CIs contain true param."},
            {"q": 7, "stars": 2, "question": "Explain the relationship between p-values and confidence intervals.", "hint": "p < 0.05 iff CI doesn't contain 0."},
            {"q": 8, "stars": 2, "question": "What is power in hypothesis testing? How do you increase it?", "hint": "1 - P(Type II error). Increase n, effect size, or alpha."},
            {"q": 9, "stars": 1, "question": "What is a t-test? When would you use it?", "hint": "Test if mean differs from hypothesized value."},
            {"q": 10, "stars": 3, "question": "How do you control FDR when doing many comparisons?", "hint": "Benjamini-Hochberg procedure."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the t-statistic: t = (x̄ - μ) / (s / √n).", "hint": "Standardized difference."},
            {"q": 37, "stars": 2, "question": "Show that with m independent tests at level α, P(≥1 false positive) ≈ 1 - (1-α)^m.", "hint": "Multiple testing."},
            {"q": 38, "stars": 2, "question": "Derive Bonferroni correction: α_adjusted = α / m.", "hint": "Controls FWER at level α."},
            {"q": 39, "stars": 1, "question": "Explain why p-values under null are uniformly distributed.", "hint": "By definition of p-value."},
            {"q": 40, "stars": 3, "question": "Show the relationship between FDR and FWER under different scenarios.", "hint": "FWER ⊂ FDR when m independent tests."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Simulate data from null hypothesis. Compute 1000 p-values. Plot histogram. Are they uniform?", "hint": "Should see flat distribution."},
            {"q": 67, "stars": 2, "question": "Perform t-test on Iris: setosa vs versicolor on sepal length. Report t-stat, p-value, 95% CI.", "hint": "Use ttest_ind() from scipy."},
            {"q": 68, "stars": 2, "question": "Perform 10 independent t-tests on random data (no true effect). Count false positives. Compare Bonferroni vs Benjamini-Hochberg.", "hint": "BH should be more powerful."},
            {"q": 69, "stars": 2, "question": "Compute p-value for correlation between two random variables. Repeat 100 times. What fraction < 0.05?", "hint": "Should be ~5%."},
            {"q": 70, "stars": 3, "question": "Implement Benjamini-Hochberg FDR correction manually. On synthetic p-values, apply and visualize threshold.", "hint": "Sort p-values, find threshold."},
        ],
    },
    "12_deep_learning_foundations": {
        "title": "Neural Networks & Backpropagation",
        "topics": ["MLPs", "activation functions", "backprop", "SGD", "PyTorch basics"],
        "datasets": ["MNIST (subset)", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is a neural network? Explain layers, neurons, weights.", "hint": "Layers of neurons connected by weights."},
            {"q": 2, "stars": 2, "question": "Explain activation functions. Why do we need them?", "hint": "Introduce nonlinearity; otherwise MLP = linear."},
            {"q": 3, "stars": 1, "question": "What is the forward pass? What's the backward pass?", "hint": "Forward: compute output. Backward: compute gradients."},
            {"q": 4, "stars": 2, "question": "True or False: Deeper networks always train faster. Justify.", "hint": "No, vanishing gradients, harder to optimize."},
            {"q": 5, "stars": 3, "question": "Explain backpropagation conceptually. Why is it efficient?", "hint": "Chain rule + dynamic programming."},
            {"q": 6, "stars": 1, "question": "What is the softmax function? When is it used?", "hint": "Converts logits to probabilities for multiclass."},
            {"q": 7, "stars": 2, "question": "Explain ReLU vs sigmoid activation. When use each?", "hint": "ReLU: simple, fast. Sigmoid: smooth, bounded."},
            {"q": 8, "stars": 2, "question": "What is the gradient vanishing problem? How do you prevent it?", "hint": "Gradients shrink in deep nets. Use ReLU, skip connections."},
            {"q": 9, "stars": 1, "question": "What is cross-entropy loss for classification?", "hint": "KL divergence from true to predicted distribution."},
            {"q": 10, "stars": 3, "question": "How do you avoid overfitting in neural networks?", "hint": "Regularization, dropout, early stopping, data augmentation."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive gradient of MSE loss: dL/dŷ = 2(ŷ - y) / n.", "hint": "d/dŷ[(ŷ - y)^2]."},
            {"q": 37, "stars": 2, "question": "Show the chain rule for backprop: dL/dw = dL/dz * dz/dw.", "hint": "Compose derivatives."},
            {"q": 38, "stars": 2, "question": "Derive the update rule for SGD: w_new = w - α * dL/dw.", "hint": "Move in direction of negative gradient."},
            {"q": 39, "stars": 1, "question": "Explain why softmax + cross-entropy is natural for classification.", "hint": "Softmax output = probability, CE = KL divergence."},
            {"q": 40, "stars": 3, "question": "Show how ReLU prevents vanishing gradient compared to sigmoid.", "hint": "ReLU derivative = 0 or 1, sigmoid = p(1-p) ≤ 0.25."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Implement a tiny 2-layer MLP in NumPy. Forward pass only.", "hint": "y = σ(w2 * σ(w1 * x + b1) + b2)."},
            {"q": 67, "stars": 2, "question": "Implement backpropagation for 2-layer MLP. Compute gradients.", "hint": "Chain rule from output to input."},
            {"q": 68, "stars": 2, "question": "Train MLP on synthetic data using SGD. Plot loss vs epoch.", "hint": "PyTorch or NumPy."},
            {"q": 69, "stars": 2, "question": "In PyTorch: define a 3-layer MLP, train on MNIST subset, report test accuracy.", "hint": "Use nn.Sequential, nn.Linear, nn.ReLU."},
            {"q": 70, "stars": 3, "question": "Implement dropout manually. Understand how it prevents overfitting.", "hint": "Random masking during training, scale during inference."},
        ],
    },
    "13_advanced_deep_learning": {
        "title": "CNNs, RNNs, Transformers, & Transfer Learning",
        "topics": ["convolutions", "RNNs/LSTMs", "attention", "transformers", "transfer learning"],
        "datasets": ["CIFAR-10 (subset)", "text datasets"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is a convolution in CNNs? Why use it for images?", "hint": "Local feature detection, weight sharing."},
            {"q": 2, "stars": 2, "question": "Explain pooling. What does max-pooling do?", "hint": "Reduces spatial dimensions, keeps strong features."},
            {"q": 3, "stars": 1, "question": "What is an RNN? Why is it good for sequences?", "hint": "Hidden state captures temporal dependency."},
            {"q": 4, "stars": 2, "question": "True or False: RNNs can remember arbitrarily long sequences. Justify.", "hint": "No, vanishing gradient problem. LSTMs help."},
            {"q": 5, "stars": 3, "question": "Explain attention mechanism. Why is it important?", "hint": "Allows model to focus on relevant parts."},
            {"q": 6, "stars": 1, "question": "What is a transformer? How is it different from RNNs?", "hint": "Parallel, self-attention, no recurrence."},
            {"q": 7, "stars": 2, "question": "Explain transfer learning. When is it useful?", "hint": "Use pre-trained model, fine-tune on new task."},
            {"q": 8, "stars": 2, "question": "What is an LSTM? How does it fix vanishing gradient?", "hint": "Cell state + gates control information flow."},
            {"q": 9, "stars": 1, "question": "What is a residual connection (skip connection)?", "hint": "Allows gradients to bypass layers."},
            {"q": 10, "stars": 3, "question": "How do you fine-tune a pre-trained model on new data?", "hint": "Low learning rate, freeze early layers, etc."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the convolution operation: y[i,j] = Σ_k Σ_l w[k,l] * x[i+k, j+l].", "hint": "Sliding window, element-wise multiplication, sum."},
            {"q": 37, "stars": 2, "question": "Show how RNN hidden state captures temporal info: h_t = f(W_h h_{t-1} + W_x x_t).", "hint": "Recurrence relation."},
            {"q": 38, "stars": 2, "question": "Derive scaled dot-product attention: Attention(Q,K,V) = softmax(QK^T / √d) V.", "hint": "Query, key, value matrices."},
            {"q": 39, "stars": 1, "question": "Explain why LSTMs have additive gradient flow (not multiplicative).", "hint": "Derivative of + is 1, avoiding vanishing grad."},
            {"q": 40, "stars": 3, "question": "Show why self-attention can be computed efficiently in parallel (vs RNN sequentially).", "hint": "All positions interact simultaneously."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Implement simple CNN in PyTorch: conv layer + ReLU + max pool + FC.", "hint": "Use nn.Conv2d, nn.ReLU, nn.MaxPool2d."},
            {"q": 67, "stars": 2, "question": "Train CNN on CIFAR-10 subset (1000 images). Report test accuracy.", "hint": "Use torchvision for data."},
            {"q": 68, "stars": 2, "question": "Implement LSTM for sequence prediction. On synthetic data y_t = sin(t), predict next step.", "hint": "Use nn.LSTM or manual."},
            {"q": 69, "stars": 2, "question": "Load pre-trained ResNet50. Fine-tune on custom dataset (10 epochs). Compare to training from scratch.", "hint": "Use transfer learning."},
            {"q": 70, "stars": 3, "question": "Implement multi-head self-attention manually (2 heads). Verify dimensions.", "hint": "Split Q,K,V into heads, compute attention, concatenate."},
        ],
    },
    "14_reinforcement_learning": {
        "title": "Reinforcement Learning Basics",
        "topics": ["bandits", "MDPs", "value iteration", "Q-learning", "policy gradient"],
        "datasets": ["GridWorld", "CartPole", "synthetic"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is reinforcement learning? How is it different from supervised learning?", "hint": "No labels, learn from rewards via interaction."},
            {"q": 2, "stars": 2, "question": "Explain the exploration-exploitation tradeoff.", "hint": "Explore: try new actions. Exploit: use best known."},
            {"q": 3, "stars": 1, "question": "What is a Markov Decision Process (MDP)?", "hint": "State, action, reward, transition model, discount."},
            {"q": 4, "stars": 2, "question": "True or False: The optimal policy is always deterministic. Justify.", "hint": "Not always, stochastic can be optimal."},
            {"q": 5, "stars": 3, "question": "Explain value function V(s) and Q-function Q(s,a). What's the difference?", "hint": "V = expected return from state. Q = from state+action."},
            {"q": 6, "stars": 1, "question": "What is a policy? How do you represent it?", "hint": "Mapping from state to action. Table or function."},
            {"q": 7, "stars": 2, "question": "Explain the Bellman equation. Why is it useful?", "hint": "V(s) = E[r + γV(s')]. Enables dynamic programming."},
            {"q": 8, "stars": 2, "question": "What is Q-learning? Is it on-policy or off-policy?", "hint": "Off-policy temporal difference learning."},
            {"q": 9, "stars": 1, "question": "What is the reward signal? How do you design it?", "hint": "Feedback from environment. Shape carefully to avoid perverse incentives."},
            {"q": 10, "stars": 3, "question": "Explain the curse of dimensionality in RL. How do you handle large state spaces?", "hint": "Function approximation, neural networks."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the Bellman equation: V(s) = Σ_a π(a|s) Σ_s' P(s'|s,a)[r + γV(s')].", "hint": "Recursive expectation of reward + future value."},
            {"q": 37, "stars": 2, "question": "Show the Bellman optimality equation: V*(s) = max_a Σ_s' P(s'|s,a)[r + γV*(s')].", "hint": "Replace expectation with max."},
            {"q": 38, "stars": 2, "question": "Derive Q-learning update: Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)].", "hint": "TD error scaled by learning rate."},
            {"q": 39, "stars": 1, "question": "Prove that value iteration converges to optimal value function.", "hint": "Contraction mapping, Banach fixed-point theorem."},
            {"q": 40, "stars": 3, "question": "Show why Q-learning converges even though learning from non-optimal policy.", "hint": "Off-policy: uses max over actions."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Implement epsilon-greedy bandit solver. On 3-armed bandit, learn which arm is best.", "hint": "Explore with prob ε, exploit otherwise."},
            {"q": 67, "stars": 2, "question": "Implement value iteration on GridWorld (4x4 grid). Find optimal policy.", "hint": "Initialize V randomly, iteratively update."},
            {"q": 68, "stars": 2, "question": "Implement Q-learning on GridWorld. Learn Q-values. Extract and visualize policy.", "hint": "Use lookup table for states/actions."},
            {"q": 69, "stars": 2, "question": "Train Q-learning on CartPole (OpenAI Gym). Plot episode length vs episode.", "hint": "Should improve over time."},
            {"q": 70, "stars": 3, "question": "Implement policy gradient (REINFORCE). On simple environment, update policy using returns.", "hint": "∇θ J(θ) = E[∇_θ log π(a|s,θ) Q(s,a)]."},
        ],
    },
    "15_production_scaling": {
        "title": "Production ML & Deployment",
        "topics": ["feature engineering", "monitoring", "versioning", "serving", "MLOps"],
        "datasets": ["real-world datasets", "logs"],
        "conceptual": [
            {"q": 1, "stars": 1, "question": "What is a production ML system? How is it different from a notebook?", "hint": "Scalable, robust, monitored, versioned."},
            {"q": 2, "stars": 2, "question": "Explain feature engineering. Why is it critical in production?", "hint": "70% of work, huge impact on performance."},
            {"q": 3, "stars": 1, "question": "What is data drift? Why does it hurt models?", "hint": "Distribution shift: training vs production data differ."},
            {"q": 4, "stars": 2, "question": "True or False: A model with high accuracy in training will always work in production. Justify.", "hint": "No, data drift, concept drift, edge cases."},
            {"q": 5, "stars": 3, "question": "Explain A/B testing for ML models. Why is it better than offline metrics?", "hint": "True impact on real users, not just metrics."},
            {"q": 6, "stars": 1, "question": "What is model versioning? Why do you need it?", "hint": "Track changes, rollback if needed."},
            {"q": 7, "stars": 2, "question": "Explain monitoring in production ML. What metrics matter?", "hint": "Accuracy, latency, data drift, error rates."},
            {"q": 8, "stars": 2, "question": "What is model serving? How do you deploy models?", "hint": "REST API, batch, streaming, edge."},
            {"q": 9, "stars": 1, "question": "What is an ML pipeline? What stages does it have?", "hint": "Data → Features → Train → Evaluate → Deploy → Monitor."},
            {"q": 10, "stars": 3, "question": "How do you handle skewed data distributions in production?", "hint": "Resampling, reweighting, threshold tuning."},
        ],
        "theoretical": [
            {"q": 36, "stars": 1, "question": "Derive the cost of misclassification. How does it affect decision threshold?", "hint": "Cost matrix, ROC analysis."},
            {"q": 37, "stars": 2, "question": "Show how to estimate model performance on future data using held-out test set.", "hint": "Confidence intervals on test metrics."},
            {"q": 38, "stars": 2, "question": "Derive the relationship between false positive rate and alert fatigue in monitoring.", "hint": "More alerts = lower cost of missing issues but more noise."},
            {"q": 39, "stars": 1, "question": "Explain why test-time augmentation can improve robustness.", "hint": "Average predictions over multiple transformations."},
            {"q": 40, "stars": 3, "question": "Show the trade-off between model latency and accuracy in production.", "hint": "Simpler models = faster but less accurate."},
        ],
        "practical": [
            {"q": 66, "stars": 1, "question": "Create a data pipeline: load, clean, featurize, split, train, evaluate.", "hint": "Scikit-learn Pipeline can help."},
            {"q": 67, "stars": 2, "question": "Build a basic monitoring dashboard: track accuracy, false positives, latency over time.", "hint": "Simulate data drift, show degradation."},
            {"q": 68, "stars": 2, "question": "Implement a model versioning system: save models with metadata (date, metrics, params).", "hint": "Use pickle or joblib, store with JSON metadata."},
            {"q": 69, "stars": 2, "question": "Deploy a model as a REST API using Flask. Accept input, return prediction.", "hint": "Simple endpoint that loads and calls model."},
            {"q": 70, "stars": 3, "question": "Implement automated retraining: monitor performance, retrain if accuracy drops below threshold.", "hint": "Check metric daily, trigger retraining."},
        ],
    },
}


def generate_notebook_json(module_key, data):
    """Generate minimal but complete notebook JSON for a module."""
    cells = []
    
    # Title
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# 🏋️ Practice Problems: {module_key.upper()}\n"
            f"## {data['title']}\n\n"
            f"**Topics**: {', '.join(data['topics'])}\n\n"
            f"**100 problems**: 35 conceptual + 30 theoretical + 35 practical\n"
            f"**Difficulty**: ⭐ (easy), ⭐⭐ (medium), ⭐⭐⭐ (hard)"
        ]
    })
    
    # Conceptual section
    cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## 🧠 Conceptual (Q1-Q35)"]})
    for p in data["conceptual"]:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"**Q{p['q']}.** [{'⭐'*p['stars']}] {p['question']}"]})
        cells.append({"cell_type": "markdown", "metadata": {}, "source": ["*Your answer:*"]})
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"<details><summary>💡 Hint</summary>{p['hint']}</details>"]})
    
    # Theoretical section
    cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## 📐 Theoretical (Q36-Q65)"]})
    for p in data["theoretical"]:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"**Q{p['q']}.** [{'⭐'*p['stars']}] {p['question']}"]})
        cells.append({"cell_type": "markdown", "metadata": {}, "source": ["*Your derivation:*"]})
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"<details><summary>💡 Hint</summary>{p['hint']}</details>"]})
    
    # Practical section
    cells.append({"cell_type": "markdown", "metadata": {}, "source": ["## 💻 Practical (Q66-Q100)"]})
    for p in data["practical"]:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"**Q{p['q']}.** [{'⭐'*p['stars']}] {p['question']}"]})
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["# YOUR CODE HERE\n"]})
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"<details><summary>💡 Hint</summary>{p['hint']}</details>"]})
    
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": ".venv", "language": "python", "name": "python3"},
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.12.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


if __name__ == "__main__":
    print("Generating all 16 modules' practice notebooks...\n")
    
    for module_key in sorted(MODULE_PROBLEMS.keys()):
        data = MODULE_PROBLEMS[module_key]
        notebook = generate_notebook_json(module_key, data)
        
        # Output path
        path = f"curriculum_pathway/{module_key}/99_practice_100.ipynb"
        
        # Save as JSON
        with open(path.replace("curriculum_pathway/", ""), "w") as f:
            json.dump(notebook, f)
        
        print(f"✅ {module_key}: {len(data['conceptual'])} conceptual + {len(data['theoretical'])} theoretical + {len(data['practical'])} practical")
    
    print("\n📋 All 12 modules (04-15) generated as JSON")
    print("Ready to push to GitHub!")
