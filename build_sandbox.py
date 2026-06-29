from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

# Paths configured for your Windows workspace
WORKSPACE_ROOT = Path(__file__).resolve().parent
OLD_SANDBOX_WIN = "C:\\Users\\adisr\\ml-dl-sandbox"
NEW_SANDBOX_WIN = "C:\\Users\\adisr\\OneDrive\\Documents\\ml\\ml_alpha"

OLD_SANDBOX = Path(OLD_SANDBOX_WIN)
SANDBOX_ROOT = Path(NEW_SANDBOX_WIN)

RESOURCES = [
    {
        "name": "ISLP",
        "kind": "textbook",
        "url": "https://www.statlearning.com/",
        "status": "Official free PDF/download page; use as the statistical spine.",
        "weeks": "1-26, 40-43",
    },
    {
        "name": "ISLP Labs",
        "kind": "repo",
        "url": "https://github.com/intro-stat-learning/ISLP_labs",
        "status": "Official lab notebooks; shallow clone if Git is available.",
        "weeks": "1-26, 40-43",
    },
    {
        "name": "Hands-On ML 3 Notebooks",
        "kind": "repo",
        "url": "https://github.com/ageron/handson-ml3",
        "status": "Official companion notebooks for the book; Apache-2.0 code repo.",
        "weeks": "1-22, 27-34, 40-43, 48",
    },
    {
        "name": "INRIA scikit-learn MOOC",
        "kind": "course/repo",
        "url": "https://inria.github.io/scikit-learn-mooc/",
        "status": "Public course with notebooks and exercises.",
        "weeks": "4, 8, 12, 14-22",
    },
    {
        "name": "ML From Scratch",
        "kind": "repo",
        "url": "https://github.com/eriklindernoren/ML-From-Scratch",
        "status": "MIT-licensed NumPy reference implementations.",
        "weeks": "5-22, 44-47",
    },
    {
        "name": "Raschka Machine Learning Book Code",
        "kind": "repo",
        "url": "https://github.com/rasbt/machine-learning-book",
        "status": "MIT-licensed companion code for scikit-learn and PyTorch.",
        "weeks": "3-22, 31-34, 44-47",
    },
    {
        "name": "Mathematics for Machine Learning",
        "kind": "textbook",
        "url": "https://mml-book.github.io/",
        "status": "Official open companion site and PDF.",
        "weeks": "1-17, 23-26, 40",
    },
    {
        "name": "MIT 18.06 Linear Algebra",
        "kind": "course",
        "url": "https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/",
        "status": "Official MIT OCW course.",
        "weeks": "1-2, 5-7, 15-17, 40",
    },
    {
        "name": "MIT 18.05 Probability and Statistics",
        "kind": "course",
        "url": "https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/",
        "status": "Official MIT OCW course.",
        "weeks": "3, 9-13, 42-43",
    },
    {
        "name": "The Elements of Statistical Learning",
        "kind": "textbook",
        "url": "https://link.springer.com/book/10.1007/978-0-387-84858-7",
        "status": "Deeper reference; use selectively after ISLP.",
        "weeks": "18-22, 40-43",
    },
    {
        "name": "Dive into Deep Learning",
        "kind": "book/repo",
        "url": "https://d2l.ai/",
        "status": "Interactive deep learning book with runnable notebooks.",
        "weeks": "23-34",
    },
    {
        "name": "D2L GitHub",
        "kind": "repo",
        "url": "https://github.com/d2l-ai/d2l-en",
        "status": "Source notebooks and book code.",
        "weeks": "23-34",
    },
    {
        "name": "Deep Learning Book",
        "kind": "textbook",
        "url": "https://www.deeplearningbook.org/",
        "status": "Official online version; use as theory reference.",
        "weeks": "23-26, 31-34",
    },
    {
        "name": "PyTorch Tutorials",
        "kind": "repo",
        "url": "https://github.com/pytorch/tutorials",
        "status": "Official PyTorch tutorial source.",
        "weeks": "23-34, 44-47",
    },
    {
        "name": "PyTorch Examples",
        "kind": "repo",
        "url": "https://github.com/pytorch/examples",
        "status": "Official curated examples across vision, text, and RL.",
        "weeks": "27-34, 44-47",
    },
    {
        "name": "fast.ai Course",
        "kind": "course",
        "url": "https://course.fast.ai/",
        "status": "Practical deep learning course.",
        "weeks": "27-34",
    },
    {
        "name": "fastbook",
        "kind": "repo",
        "url": "https://github.com/fastai/fastbook",
        "status": "Jupyter notebooks for the fast.ai book; mind repo license notes.",
        "weeks": "27-34",
    },
    {
        "name": "micrograd",
        "kind": "repo",
        "url": "https://github.com/karpathy/micrograd",
        "status": "Tiny educational autograd engine.",
        "weeks": "23-26",
    },
    {
        "name": "makemore",
        "kind": "repo",
        "url": "https://github.com/karpathy/makemore",
        "status": "Educational character-level language model.",
        "weeks": "31-34",
    },
    {
        "name": "nanochat",
        "kind": "repo",
        "url": "https://github.com/karpathy/nanochat",
        "status": "Minimal LLM training harness; use CPU-scale demos locally.",
        "weeks": "34, 49-50",
    },
    {
        "name": "nanoGPT",
        "kind": "repo",
        "url": "https://github.com/karpathy/nanoGPT",
        "status": "Historical GPT reference; nanochat is the preferred active path.",
        "weeks": "34",
    },
    {
        "name": "Hugging Face Course",
        "kind": "course/repo",
        "url": "https://huggingface.co/course",
        "status": "Official Transformers course.",
        "weeks": "31-39",
    },
    {
        "name": "Hugging Face Notebooks",
        "kind": "repo",
        "url": "https://github.com/huggingface/notebooks",
        "status": "Official notebooks using Hugging Face libraries.",
        "weeks": "31-39",
    },
    {
        "name": "Stanford CS231n",
        "kind": "course",
        "url": "https://cs231n.stanford.edu/",
        "status": "Computer vision lectures and assignment descriptions.",
        "weeks": "27-30, 35-36",
    },
    {
        "name": "Stanford CS224n",
        "kind": "course",
        "url": "https://web.stanford.edu/class/cs224n/",
        "status": "NLP with deep learning lectures and project structure.",
        "weeks": "31-34, 35, 37",
    },
    {
        "name": "Sutton and Barto RL",
        "kind": "textbook",
        "url": "https://mitpress.mit.edu/9780262039246/reinforcement-learning/",
        "status": "MIT Press open access page for RL foundations.",
        "weeks": "44-47",
    },
    {
        "name": "OpenAI Spinning Up",
        "kind": "repo/course",
        "url": "https://github.com/openai/spinningup",
        "status": "Educational deep RL resource.",
        "weeks": "47",
    },
    {
        "name": "CleanRL",
        "kind": "repo",
        "url": "https://github.com/vwxyzjn/cleanrl",
        "status": "Single-file deep RL implementations; use for comparison.",
        "weeks": "47",
    },
    {
        "name": "Made With ML",
        "kind": "repo/course",
        "url": "https://github.com/GokuMohandas/Made-With-ML",
        "status": "Production ML course and code.",
        "weeks": "48-52",
    },
    {
        "name": "ProbML",
        "kind": "book/repo",
        "url": "https://github.com/probml/pml-book",
        "status": "Probabilistic ML book materials and code references.",
        "weeks": "42-43",
    },
]

REPO_CLONES = [
    ("islp_labs", "https://github.com/intro-stat-learning/ISLP_labs.git"),
    ("handson-ml3", "https://github.com/ageron/handson-ml3.git"),
    ("scikit-learn-mooc", "https://github.com/INRIA/scikit-learn-mooc.git"),
    ("ml-from-scratch", "https://github.com/eriklindernoren/ML-From-Scratch.git"),
    ("raschka-machine-learning-book", "https://github.com/rasbt/machine-learning-book.git"),
    ("d2l-en", "https://github.com/d2l-ai/d2l-en.git"),
    ("pytorch-tutorials", "https://github.com/pytorch/tutorials.git"),
    ("pytorch-examples", "https://github.com/pytorch/examples.git"),
    ("fastbook", "https://github.com/fastai/fastbook.git"),
    ("micrograd", "https://github.com/karpathy/micrograd.git"),
    ("makemore", "https://github.com/karpathy/makemore.git"),
    ("nanochat", "https://github.com/karpathy/nanochat.git"),
    ("nanoGPT_historical", "https://github.com/karpathy/nanoGPT.git"),
    ("huggingface-course", "https://github.com/huggingface/course.git"),
    ("huggingface-notebooks", "https://github.com/huggingface/notebooks.git"),
    ("spinningup", "https://github.com/openai/spinningup.git"),
    ("cleanrl", "https://github.com/vwxyzjn/cleanrl.git"),
    ("made-with-ml", "https://github.com/GokuMohandas/Made-With-ML.git"),
    ("probml-book", "https://github.com/probml/pml-book.git"),
]

WEEKS = [
    (1, 1, "orientation_python_data_stack", "Course orientation, Python workflow, and ML mental model", ["ISLP Ch. 1", "Hands-On ML Ch. 1 notebook", "MML Ch. 2 vectors and matrices"], "EDA launch notebook"),
    (2, 1, "numpy_pandas_matplotlib", "NumPy arrays, pandas data frames, matplotlib plots", ["ISLP Ch. 2 lab", "Hands-On ML Ch. 2 notebook", "MIT 18.06 vectors overview"], "Data stack drills"),
    (3, 1, "eda_data_cleaning_baselines", "Exploratory analysis, cleaning, and baselines", ["ISLP Ch. 2", "Hands-On ML Ch. 2", "MIT 18.05 probability preview"], "EDA mini-project"),
    (4, 1, "train_test_generalization", "Train/test thinking, loss, metrics, and generalization", ["ISLP Ch. 2 statistical learning framing", "INRIA scikit-learn MOOC introduction", "Hands-On ML project checklist"], "Generalization note"),
    (5, 2, "simple_linear_regression", "Simple linear regression and least squares", ["ISLP Ch. 3.1-3.2", "Hands-On ML Ch. 4 linear regression", "MML least squares"], "NumPy simple regression"),
    (6, 2, "multiple_regression_design_matrices", "Multiple regression and design matrices", ["ISLP Ch. 3.3", "ISLP Ch. 3 lab", "MIT 18.06 column spaces"], "Design matrix lab"),
    (7, 2, "gradient_descent_normal_equations", "Gradient descent, normal equations, and optimization intuition", ["Hands-On ML Ch. 4 gradient descent", "MML derivatives and gradients", "Raschka Ch. 2"], "Gradient descent implementation"),
    (8, 2, "regression_diagnostics_capstone", "Regression diagnostics, interpretation, leakage, and capstone", ["ISLP Ch. 3 remaining sections", "INRIA model evaluation", "Hands-On ML Ch. 2 review"], "Regression benchmark report"),
    (9, 3, "classification_framing", "Classification framing, decision boundaries, and metrics", ["ISLP Ch. 4.1-4.2", "Hands-On ML Ch. 3 classification", "MIT 18.05 conditional probability"], "Classifier metric notebook"),
    (10, 3, "logistic_regression", "Logistic regression, odds, sigmoid, and cross entropy", ["ISLP Ch. 4 logistic regression", "Hands-On ML Ch. 4 logistic regression", "MML logistic regression notes"], "Logistic regression from scratch"),
    (11, 3, "lda_qda_knn", "LDA, QDA, nearest neighbors, and bias-variance intuition", ["ISLP Ch. 4 LDA/QDA/KNN", "ISLP Ch. 4 lab", "MIT 18.05 Bayes rule"], "KNN and Gaussian classifier lab"),
    (12, 3, "resampling_cv_bootstrap", "Cross-validation, bootstrap, and honest evaluation", ["ISLP Ch. 5", "INRIA cross-validation", "Hands-On ML model validation"], "Resampling toolkit"),
    (13, 3, "synthesis_classification_project", "Synthesis week: classification benchmark project", ["ISLP Ch. 4-5 review", "Hands-On ML Ch. 3 review", "Raschka evaluation chapter"], "Classification capstone"),
    (14, 4, "model_selection_subset_methods", "Subset selection, model comparison, and validation strategy", ["ISLP Ch. 6.1", "INRIA model selection", "ESL model selection reference"], "Model selection grid"),
    (15, 4, "ridge_lasso_regularization", "Ridge, lasso, shrinkage, and coefficient paths", ["ISLP Ch. 6.2", "Hands-On ML regularized models", "MML optimization review"], "Ridge/lasso from scratch"),
    (16, 4, "feature_engineering_nonlinearity", "Polynomial features, splines, and nonlinear feature maps", ["ISLP Ch. 7", "INRIA feature engineering", "Hands-On ML preprocessing"], "Feature transform lab"),
    (17, 4, "pipelines_regularization_capstone", "Pipelines, preprocessing, and regularized model capstone", ["ISLP Ch. 6-7 review", "INRIA pipelines", "Hands-On ML Ch. 4 review"], "Regularization capstone"),
    (18, 5, "decision_trees", "Decision trees, impurity, splits, and interpretability", ["ISLP Ch. 8.1", "Hands-On ML Ch. 6", "ML From Scratch decision tree"], "Decision tree implementation"),
    (19, 5, "bagging_random_forests", "Bagging, random forests, and variance reduction", ["ISLP Ch. 8.2", "Hands-On ML Ch. 7", "ESL tree ensembles reference"], "Random forest benchmark"),
    (20, 5, "boosting_gradient_boosting", "Boosting, additive models, and staged learning", ["ISLP Ch. 8 boosting", "Hands-On ML ensembles", "Raschka ensembles"], "Boosting notebook"),
    (21, 5, "support_vector_machines", "Support vector machines, margins, and kernels", ["ISLP Ch. 9", "Hands-On ML Ch. 5", "ESL SVM reference"], "SVM margin lab"),
    (22, 5, "classical_ml_capstone", "Classical ML capstone across regression and classification", ["ISLP Ch. 1-9 review", "Hands-On ML Ch. 1-7 review", "INRIA MOOC review"], "Classical ML portfolio project"),
    (23, 6, "neural_networks_intro", "Neural networks, MLPs, activations, and representation", ["ISLP Ch. 10 introduction", "D2L MLP chapter", "Hands-On ML Ch. 10"], "Tiny MLP notebook"),
    (24, 6, "pytorch_tensors_autograd", "PyTorch tensors, modules, autograd, and training loops", ["PyTorch beginner tutorials", "D2L automatic differentiation", "Hands-On ML neural net setup"], "PyTorch basics lab"),
    (25, 6, "backprop_micrograd", "Backpropagation, computation graphs, and micrograd", ["micrograd repo", "Deep Learning Book Ch. 6", "D2L backprop sections"], "Tiny autograd engine"),
    (26, 6, "synthesis_neural_network_capstone", "Synthesis week: MLP from scratch and PyTorch benchmark", ["ISLP Ch. 10 lab", "micrograd review", "PyTorch tutorial review"], "Neural network capstone"),
    (27, 7, "cnn_basics", "Convolutions, pooling, and image tensors", ["D2L CNN chapter", "PyTorch vision tutorials", "fastbook MNIST basics"], "CNN from scratch pieces"),
    (28, 7, "modern_cnns_resnet", "Modern CNNs, residual connections, and augmentation", ["D2L ResNet chapter", "fastbook ResNet chapters", "CS231n CNN notes"], "ResNet transfer lab"),
    (29, 7, "image_classification_transfer", "Transfer learning, evaluation, and dataset discipline", ["fast.ai vision lessons", "PyTorch examples vision", "Hands-On ML CNN notebook"], "Image classifier capstone"),
    (30, 7, "vision_debugging_ablations", "Vision debugging, ablations, errors, and explainability", ["CS231n assignment descriptions", "D2L training tricks", "PyTorch examples"], "Vision ablation report"),
    (31, 8, "text_preprocessing_embeddings", "Tokenization, embeddings, and text datasets", ["Hugging Face Course Ch. 1-2", "CS224n introduction", "D2L NLP preprocessing"], "Embedding notebook"),
    (32, 8, "sequence_models_rnn_lstm", "RNNs, LSTMs, and sequence modeling", ["D2L RNN chapters", "Hands-On ML sequence notebook", "Raschka sequence chapter"], "Sequence model lab"),
    (33, 8, "attention_transformers", "Attention, transformers, and self-attention math", ["CS224n attention lectures", "Hugging Face Course transformers", "D2L attention chapter"], "Attention from scratch"),
    (34, 8, "llm_mini_build", "Character models and small LLM training pipeline", ["makemore repo", "nanochat repo", "nanoGPT historical reference"], "Character model mini-build"),
    (35, 9, "specialization_planning", "Choose a specialization and define a dataset/question", ["CS231n project guidance", "CS224n project guidance", "Hugging Face task guides"], "Specialization proposal"),
    (36, 9, "cv_specialization_track", "Computer vision specialization track", ["CS231n assignments", "PyTorch vision examples", "D2L computer vision"], "CV track build"),
    (37, 9, "nlp_specialization_track", "NLP specialization track", ["CS224n notes", "Hugging Face notebooks", "makemore review"], "NLP track build"),
    (38, 9, "audio_timeseries_multimodal_track", "Audio, time-series, or multimodal specialization track", ["PyTorch examples", "Hugging Face notebooks", "D2L sequence/vision review"], "Domain experiment"),
    (39, 9, "synthesis_specialization_capstone", "Synthesis week: specialization mini-capstone", ["Selected specialization resources", "Made With ML experiment notes", "PyTorch examples"], "Mini-capstone report"),
    (40, 10, "pca_dimensionality_reduction", "PCA, projections, eigenspaces, and compression", ["ISLP Ch. 12 PCA", "Hands-On ML dimensionality reduction", "MML eigenvectors"], "PCA from scratch"),
    (41, 10, "clustering_unsupervised_learning", "Clustering, unsupervised learning, and representation", ["ISLP Ch. 12 clustering", "Hands-On ML clustering", "ESL clustering reference"], "Clustering lab"),
    (42, 10, "probabilistic_view", "Probabilistic modeling view of ML", ["ProbML intro chapters", "MIT 18.05 likelihood notes", "ESL statistical decision theory"], "Likelihood notebook"),
    (43, 10, "multiple_testing_inference", "Multiple testing, false discovery, and inference humility", ["ISLP Ch. 13", "MIT 18.05 hypothesis testing", "ProbML uncertainty reference"], "Multiple testing lab"),
    (44, 11, "bandits", "Bandits, exploration, exploitation, and incremental learning", ["Sutton and Barto Ch. 2", "ML From Scratch RL references", "PyTorch examples RL overview"], "Bandit implementation"),
    (45, 11, "mdps_dynamic_programming", "MDPs, Bellman equations, policy/value iteration", ["Sutton and Barto Ch. 3-4", "Spinning Up RL intro", "MML Markov chain review"], "Gridworld DP"),
    (46, 11, "monte_carlo_td_q_learning", "Monte Carlo, temporal difference learning, Sarsa, Q-learning", ["Sutton and Barto Ch. 5-6", "CleanRL DQN overview", "PyTorch RL examples"], "Tabular Q-learning"),
    (47, 11, "deep_rl_cleanrl", "Deep RL bridge, PPO/DQN anatomy, and reproducibility", ["OpenAI Spinning Up", "CleanRL docs/repo", "PyTorch examples RL"], "CleanRL comparison"),
    (48, 12, "production_ml_foundations", "Production ML foundations, testing, tracking, and packaging", ["Made With ML foundations", "Hands-On ML deployment notebook", "scikit-learn production checklist"], "Production checklist"),
    (49, 12, "final_capstone_design", "Final capstone design, data pipeline, and experiment plan", ["Made With ML design/develop", "Selected domain resources", "nanochat optional reference"], "Capstone proposal"),
    (50, 12, "final_capstone_modeling", "Final capstone modeling, ablations, and benchmarks", ["Made With ML training/tuning", "Selected model resources", "PyTorch/Hugging Face docs"], "Capstone experiment suite"),
    (51, 12, "final_capstone_delivery", "Final capstone delivery, serving, README, and portfolio polish", ["Made With ML deployment", "Portfolio README examples", "Experiment tracking notes"], "Capstone delivery"),
    (52, 12, "final_synthesis_portfolio", "Synthesis week: year-end retrospective and portfolio map", ["All roadmap review", "Open Mystery Stack review", "Made With ML iteration notes"], "Portfolio retrospective"),
]

# The 2-Day Concept Cycle Daily Specs (3 concepts per week + 1 synthesis review day)
DAY_SPECS = [
    ("day_01", "Concept A: Intake, Math, & Exploration", "concept_a_math"),
    ("day_02", "Concept A: From-Scratch & Framework Build", "concept_a_build"),
    ("day_03", "Concept B: Intake, Math, & Exploration", "concept_b_math"),
    ("day_04", "Concept B: From-Scratch & Framework Build", "concept_b_build"),
    ("day_05", "Concept C: Intake, Math, & Exploration", "concept_c_math"),
    ("day_06", "Concept C: From-Scratch & Framework Build", "concept_c_build"),
    ("day_07", "Weekly Review, Math Synthesis, & Mystery Stack Cleanup", "weekly_review"),
]

# Hand-Curated Mathematical Specifications Database
MATH_DATABASE = {
    2: { # NumPy & Linear Algebra Week
        "a": {
            "title": "Matrix-Vector Projections",
            "equation": r"\mathbf{y} = \mathbf{X}\mathbf{w}",
            "explanation": "Projects N data samples of D dimensions onto a continuous prediction vector.",
            "derivation": [
                r"For a single instance: $\hat{y}_i = \sum_{j=1}^D X_{ij} w_j = \mathbf{x}_i^T \mathbf{w}$",
                r"To compute all predictions simultaneously, stack instances row-wise into matrix $\mathbf{X}$:",
                r"$\mathbf{\hat{y}} = \mathbf{X}\mathbf{w}$"
            ],
            "shapes": {"X": "(N, D)", "w": "(D, 1)", "y_pred": "(N, 1)"},
            "numpy_code": "y_pred = X @ w",
            "plot_code": """# Visualize projection
rng = np.random.default_rng(42)
X_demo = rng.uniform(-2, 2, (50, 1))
w_demo = np.array([[1.5]])
y_demo = X_demo @ w_demo + rng.normal(0, 0.3, (50, 1))
plt.scatter(X_demo, y_demo, color='royalblue', label='Data')
plt.plot(X_demo, X_demo @ w_demo, color='crimson', label='Projected Line (y = Xw)')
plt.legend()
plt.title("Matrix-Vector Projection (D=1)")
plt.show()"""
        },
        "b": {
            "title": "Mean Squared Error (MSE)",
            "equation": r"L(w) = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2",
            "explanation": "Measures average squared vertical distance from predictions to observations.",
            "derivation": [
                r"Let error residual be: $e_i = y_i - \hat{y}_i$",
                r"Square individual residuals: $e_i^2 = (y_i - \hat{y}_i)^2$",
                r"Sum and normalize over all N samples: $L(w) = \frac{1}{N} \sum_{i=1}^N e_i^2$"
            ],
            "shapes": {"errors": "(N, 1)", "loss": "Scalar"},
            "numpy_code": "loss = np.mean((y - y_pred) ** 2)",
            "plot_code": """# Loss curve vs parameter weight
rng = np.random.default_rng(42)
X_demo = rng.uniform(-2, 2, (50, 1))
y_demo = X_demo * 1.5 + rng.normal(0, 0.3, (50, 1))
w_grid = np.linspace(-2, 5, 100)
losses = [np.mean((y_demo - X_demo * wg)**2) for wg in w_grid]
plt.plot(w_grid, losses, color='darkviolet', lw=2)
plt.axvline(1.5, color='forestgreen', linestyle='--', label='Optimal w (1.5)')
plt.xlabel('Weight w')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.title("MSE Loss Curve (Convex Profile)")
plt.show()"""
        },
        "c": {
            "title": "Gradient of MSE",
            "equation": r"\nabla_w L = -\frac{2}{N}\mathbf{X}^T(\mathbf{y} - \mathbf{X}\mathbf{w})",
            "explanation": "Calculates partial derivatives for each weight to find direction of steepest descent.",
            "derivation": [
                r"Let $L = \frac{1}{N} \sum (y_i - \mathbf{x}_i^T\mathbf{w})^2$",
                r"Apply Chain Rule: Let $u_i = y_i - \mathbf{x}_i^T\mathbf{w}$ so $L = \frac{1}{N}\sum u_i^2$",
                r"$\frac{\partial L}{\partial \mathbf{w}} = \frac{1}{N}\sum 2 u_i \frac{\partial u_i}{\partial \mathbf{w}}$",
                r"Since $\frac{\partial u_i}{\partial \mathbf{w}} = -\mathbf{x}_i$, we obtain:",
                r"$\frac{\partial L}{\partial \mathbf{w}} = -\frac{2}{N}\sum \mathbf{x}_i(y_i - \mathbf{x}_i^T\mathbf{w}) = -\frac{2}{N}\mathbf{X}^T(\mathbf{y} - \mathbf{X}\mathbf{w})$"
            ],
            "shapes": {"gradient": "(D, 1)"},
            "numpy_code": "dw = -2/N * X.T @ (y - (X @ w))",
            "plot_code": """# Visualize gradients on loss curve
rng = np.random.default_rng(42)
X_demo = rng.uniform(-2, 2, (50, 1))
y_demo = X_demo * 1.5 + rng.normal(0, 0.3, (50, 1))
w_grid = np.linspace(-2, 5, 100)
losses = [np.mean((y_demo - X_demo * wg)**2) for wg in w_grid]
w_val = 0.0
dw_val = -2/len(X_demo) * np.sum(X_demo * (y_demo - X_demo * w_val))
loss_w = np.mean((y_demo - X_demo * w_val)**2)
slope_x = np.linspace(-0.5, 0.5, 10) + w_val
slope_y = dw_val * (slope_x - w_val) + loss_w
plt.plot(w_grid, losses, color='grey')
plt.plot(slope_x, slope_y, 'r--', label=f'Tangent (slope={dw_val:.2f})')
plt.scatter([w_val], [loss_w], color='red')
plt.xlabel('w')
plt.ylabel('Loss')
plt.legend()
plt.show()"""
        }
    },
    5: { # Simple Linear Regression Week
        "a": {
            "title": "Closed-Form OLS Slope",
            "equation": r"w_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}",
            "explanation": "Derived by taking partial derivatives of RSS with respect to slope and setting them to zero.",
            "derivation": [
                r"Objective: Minimize RSS = $\sum (y_i - (w_0 + w_1 x_i))^2$",
                r"Take derivative wrt $w_0$: $\frac{\partial RSS}{\partial w_0} = -2\sum (y_i - w_0 - w_1 x_i) = 0 \implies w_0 = \bar{y} - w_1 \bar{x}$",
                r"Substitute $w_0$ back and take derivative wrt $w_1$: $\frac{\partial RSS}{\partial w_1} = -2\sum x_i(y_i - \bar{y} + w_1\bar{x} - w_1 x_i) = 0$",
                r"Solving for $w_1$ yields the covariance/variance ratio: $w_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$"
            ],
            "shapes": {"w_1": "Scalar", "w_0": "Scalar"},
            "numpy_code": "w1 = np.sum((x - mx) * (y - my)) / np.sum((x - mx) ** 2)",
            "plot_code": """# Closed-form regression fit
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.8, 6.2, 8.1, 9.9])
mx, my = np.mean(x), np.mean(y)
w1 = np.sum((x - mx) * (y - my)) / np.sum((x - mx) ** 2)
w0 = my - w1 * mx
plt.scatter(x, y, color='blue')
plt.plot(x, w0 + w1 * x, color='orange', label=f'y = {w0:.2f} + {w1:.2f}x')
plt.legend()
plt.title("OLS Regression Closed Form fit")
plt.show()"""
        },
        "b": {
            "title": "Residual Sum of Squares (RSS)",
            "equation": r"RSS = \sum_{i=1}^N (y_i - \hat{y}_i)^2",
            "explanation": "Calculates total vertical distance variance between estimated line and target points.",
            "derivation": [
                r"Let residuals be $e_i = y_i - (w_0 + w_1 x_i)$",
                r"Sum squared residuals: $RSS = \sum e_i^2$"
            ],
            "shapes": {"residuals": "(N,)", "RSS": "Scalar"},
            "numpy_code": "rss = np.sum((y - (w0 + w1 * x)) ** 2)",
            "plot_code": """# Show vertical residuals
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.8, 6.2, 8.1, 9.9])
w1 = 1.97
w0 = 0.11
y_pred = w0 + w1 * x
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='orange')
for xi, yi, ypi in zip(x, y, y_pred):
    plt.plot([xi, xi], [yi, ypi], 'r--')
plt.title("Visualizing Vertical Residuals (RSS)")
plt.show()"""
        },
        "c": {
            "title": "Coefficient of Determination ($R^2$)",
            "equation": r"R^2 = 1 - \frac{RSS}{TSS}",
            "explanation": "Represents the proportion of variance in the dependent variable that is predictable from the independent variable.",
            "derivation": [
                r"Residual Sum of Squares: $RSS = \sum (y_i - \hat{y}_i)^2$",
                r"Total Sum of Squares (variance from mean baseline): $TSS = \sum (y_i - \bar{y})^2$",
                r"Proportion of explained variance: $R^2 = 1 - \frac{RSS}{TSS}$"
            ],
            "shapes": {"TSS": "Scalar", "R2": "Scalar"},
            "numpy_code": "r2 = 1 - (rss / np.sum((y - np.mean(y)) ** 2))",
            "plot_code": """# R^2 calculation output
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.8, 6.2, 8.1, 9.9])
y_pred = 0.11 + 1.97 * x
tss = np.sum((y - np.mean(y))**2)
rss = np.sum((y - y_pred)**2)
r2 = 1 - (rss / tss)
print(f"TSS: {tss:.3f}, RSS: {rss:.3f}, R^2: {r2:.4f}")"""
        }
    }
}


def get_theme(week_num: int) -> str:
    if week_num in [1, 2, 3, 4]:
        return "Foundations"
    elif week_num in [5, 6, 7, 8]:
        return "Regression"
    elif week_num in [9, 10, 11, 12, 13]:
        return "Classification"
    elif week_num in [14, 15, 16, 17]:
        return "Regularization"
    elif week_num in [18, 19, 20, 21, 22]:
        return "Trees & SVMs"
    elif week_num in [23, 24, 25, 26]:
        return "Neural Nets"
    elif week_num in [27, 28, 29, 30]:
        return "Computer Vision"
    elif week_num in [31, 32, 33, 34]:
        return "NLP & Transformers"
    elif week_num in [35, 36, 37, 38, 39]:
        return "Specialization"
    elif week_num in [40, 41, 42, 43]:
        return "Unsupervised"
    elif week_num in [44, 45, 46, 47]:
        return "Reinforcement Learning"
    else:
        return "Production"


def get_math_spec(week_num: int, concept_letter: str, topic: str) -> dict:
    """Retrieves math spec from database, or generates a structured fallback based on the week's theme."""
    if week_num in MATH_DATABASE and concept_letter in MATH_DATABASE[week_num]:
        return MATH_DATABASE[week_num][concept_letter]
    
    theme = get_theme(week_num)
    
    # Mathematical fallbacks matching themes
    if theme == "Regression":
        if concept_letter == "a":
            return {
                "title": f"Linear Projection mapping ({topic})",
                "equation": r"\mathbf{y} = \mathbf{X}\mathbf{w}",
                "explanation": "Calculus/Linear algebra mapping mapping multidimensional input space to target variable.",
                "derivation": [r"Model: $y_i = \sum_{j} X_{ij} w_j + b$", r"Vectorized format: $\mathbf{y} = \mathbf{X}\mathbf{w} + b$"],
                "shapes": {"X": "(N, D)", "w": "(D, 1)", "y": "(N, 1)"},
                "numpy_code": "y_pred = X @ w + b",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Linear Projection Space'); plt.show()"
            }
        elif concept_letter == "b":
            return {
                "title": "Optimization objective (MSE Loss)",
                "equation": r"\mathcal{L} = \frac{1}{N}\sum_i (y_i - \hat{y}_i)^2",
                "explanation": "Euclidean metrics comparing target spaces and projections.",
                "derivation": [r"Difference: $e = y - \hat{y}$", r"Average square norms: $\mathcal{L} = \frac{1}{N} e^T e$"],
                "shapes": {"loss": "Scalar"},
                "numpy_code": "loss = np.mean((y - y_pred)**2)",
                "plot_code": "plt.plot([0, 1], [1, 0]); plt.title('MSE convex loss landscape'); plt.show()"
            }
        else:
            return {
                "title": "Gradient Step Update",
                "equation": r"\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla \mathcal{L}",
                "explanation": "We update weights in direction opposite to gradient vector.",
                "derivation": [r"Let $\nabla \mathcal{L}$ be the vector of partial derivatives.", r"Step update: $w_{new} = w_{old} - \eta \frac{\partial \mathcal{L}}{\partial w}$"],
                "shapes": {"gradient": "(D, 1)"},
                "numpy_code": "w = w - eta * dw",
                "plot_code": "plt.plot([0, 1], [0.5, 0.5]); plt.title('Optimizer Step Descent'); plt.show()"
            }
            
    elif theme == "Classification":
        if concept_letter == "a":
            return {
                "title": "Sigmoid Activation Function",
                "equation": r"\sigma(z) = \frac{1}{1 + e^{-z}}",
                "explanation": "Squeezes continuous real coordinate outputs into a probability interval [0, 1].",
                "derivation": [r"Let $z = \mathbf{x}^T\mathbf{w}$", r"Probability bounds limit function: $\lim_{z \to \infty} \sigma(z) = 1$", r"$\lim_{z \to -\infty} \sigma(z) = 0$"],
                "shapes": {"z": "(N, 1)", "prob": "(N, 1)"},
                "numpy_code": "p = 1 / (1 + np.exp(-z))",
                "plot_code": "z = np.linspace(-6, 6, 100); plt.plot(z, 1/(1+np.exp(-z))); plt.title('Sigmoid Function'); plt.show()"
            }
        elif concept_letter == "b":
            return {
                "title": "Binary Cross-Entropy Loss",
                "equation": r"L = -\frac{1}{N}\sum [y_i \log(p_i) + (1 - y_i)\log(1 - p_i)]",
                "explanation": "Derived from maximum likelihood estimation of Bernoulli random trials.",
                "derivation": [r"Likelihood: $P(y|p) = p^y (1-p)^{1-y}$", r"Log Likelihood: $\log P = y\log p + (1-y)\log(1-p)$", r"Minimize Negative Log Likelihood: $L = - \log P$"],
                "shapes": {"loss": "Scalar"},
                "numpy_code": "loss = -np.mean(y * np.log(p) + (1-y) * np.log(1-p))",
                "plot_code": "plt.plot([0.1, 0.9], [1.0, 0.1]); plt.title('Binary Cross Entropy Profile'); plt.show()"
            }
        else:
            return {
                "title": "Gradient of Binary Cross-Entropy",
                "equation": r"\frac{\partial L}{\partial \mathbf{w}} = \frac{1}{N}\mathbf{X}^T(\mathbf{p} - \mathbf{y})",
                "explanation": "The gradient matrix calculation for logistic parameter spaces.",
                "derivation": [r"Apply chain rule of $\frac{\partial L}{\partial p_i}$ and $\frac{\partial p_i}{\partial z_i}$ and $\frac{\partial z_i}{\partial w_j}$", r"Simplifies down to target subtraction: $\frac{\partial L}{\partial \mathbf{w}} = \frac{1}{N}\mathbf{X}^T(\mathbf{p} - \mathbf{y})$"],
                "shapes": {"grad": "(D, 1)"},
                "numpy_code": "dw = 1/N * X.T @ (p - y)",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Log loss optimization update vector'); plt.show()"
            }
            
    elif theme == "Neural Nets":
        if concept_letter == "a":
            return {
                "title": "Affine Node Mapping",
                "equation": r"\mathbf{z}^{[l]} = \mathbf{a}^{[l-1]}\mathbf{W}^{[l]} + \mathbf{b}^{[l]}",
                "explanation": "Standard linear projections inside feedforward hidden layers.",
                "derivation": [r"Multiply activation vector mapping by weights, add bias offset."],
                "shapes": {"a_prev": "(N, D_in)", "W": "(D_in, D_out)", "z": "(N, D_out)"},
                "numpy_code": "z = a_prev @ W + b",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Hidden Layer Transform Map'); plt.show()"
            }
        elif concept_letter == "b":
            return {
                "title": "Rectified Linear Activation (ReLU)",
                "equation": r"a = \max(0, z)",
                "explanation": "Nonlinear activation threshold function generating sparse activations.",
                "derivation": [r"If $z > 0$, slope is $1$. If $z \le 0$, slope is $0$."],
                "shapes": {"a": "(N, D)"},
                "numpy_code": "a = np.maximum(0, z)",
                "plot_code": "z = np.linspace(-3,3,100); plt.plot(z, np.maximum(0,z)); plt.title('ReLU activation'); plt.show()"
            }
        else:
            return {
                "title": "Backpropagation Node Jacobian",
                "equation": r"\delta^{[l]} = (\delta^{[l+1]}\mathbf{W}^{[l+1]T}) \odot \sigma'(z^{[l]})",
                "explanation": "Calculates local error components propagating backward using chain rule matrices.",
                "derivation": [r"Local gradient is product of downstream error and local activation slope."],
                "shapes": {"delta": "(N, D)"},
                "numpy_code": "delta = (delta_next @ W_next.T) * (z > 0)",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Backpropagation updates paths'); plt.show()"
            }
            
    elif theme == "NLP & Transformers":
        if concept_letter == "a":
            return {
                "title": "Scaled Dot-Product Attention",
                "equation": r"\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
                "explanation": "Measures similarity scores between Queries and Keys, weighting Value vectors.",
                "derivation": [r"Compute similarity matrix: $S = QK^T$", r"Scale by square root of dimensions to stabilize variance: $S_{scaled} = \frac{S}{\sqrt{d_k}}$", r"Normalize using softmax and multiply by $V$."],
                "shapes": {"Q": "(Seq, D_k)", "K": "(Seq, D_k)", "V": "(Seq, D_v)", "Attention": "(Seq, D_v)"},
                "numpy_code": "scores = softmax(Q @ K.T / np.sqrt(dk)) \n attn = scores @ V",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Attention weights matrix'); plt.show()"
            }
        elif concept_letter == "b":
            return {
                "title": "Softmax Vector Normalization",
                "equation": r"\text{softmax}(z_i) = \frac{e^{z_i}}{\sum e^{z_j}}",
                "explanation": "Exponentiates logits and normalizes them into probability values.",
                "derivation": [r"Map elements to non-negative range: $e^{z_i}$", r"Divide by partition function sum to enforce probability constraints."],
                "shapes": {"z": "(Seq, Seq)"},
                "numpy_code": "exp_z = np.exp(z - np.max(z, axis=-1, keepdims=True))\nprobs = exp_z / np.sum(exp_z, axis=-1, keepdims=True)",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Softmax distribution plot'); plt.show()"
            }
        else:
            return {
                "title": "Multi-Head Attention Projection Split",
                "equation": r"\text{MHA}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O",
                "explanation": "Calculates attention spaces concurrently on separate linear projection heads.",
                "derivation": [r"Project input sequence space into multiple smaller channels.", r"Run attention parallel, stack representations back together."],
                "shapes": {"MultiHead": "(Seq, D_model)"},
                "numpy_code": "heads = [attention(Q_i, K_i, V_i) for Q_i, K_i, V_i in zip(Qs, Ks, Vs)]",
                "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Multihead representation assembly'); plt.show()"
            }
            
    # Default Fallback for Foundations or undefined areas
    else:
        return {
            "title": f"Linear Projection Space ({topic})",
            "equation": r"\mathbf{y} = \mathbf{X}\mathbf{w}",
            "explanation": "Linear projection mappings between vector spaces.",
            "derivation": [r"Mapping target space dimensions: $\mathbf{y} = \mathbf{X}\mathbf{w}$"],
            "shapes": {"X": "(N, D)", "w": "(D, 1)"},
            "numpy_code": "y_pred = X @ w",
            "plot_code": "plt.plot([0, 1], [0, 1]); plt.title('Vector spaces projection map'); plt.show()"
        }


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def rel_link(path: Path) -> str:
    return path.as_posix()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def notebook_math_day(path: Path, title: str, topic: str, concept_data: dict, resources: list[str]) -> None:
    """Generates the Math and Exploration Notebook for Days 1, 3, 5."""
    deriv_md = "\\n".join([f"{i+1}. {step}" for i, step in enumerate(concept_data["derivation"])])
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    f"Topic: {topic}\n",
                    "\n",
                    f"### 📍 Core Mathematical Equation\n",
                    f"$$\n{concept_data['equation']}\n$$\n",
                    "\n",
                    "### 💡 Intuition & Concept Explanation\n",
                    f"{concept_data['explanation']}\n",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📝 Step-by-Step Mathematical Derivation\n",
                    deriv_md,
                    "\n",
                    "### 🧮 Math-to-Code Dimensions Mapping (Rosetta Stone)\n",
                    "| Math Notation | Matrix Dimensions | NumPy Variable | Description |\n",
                    "| :--- | :--- | :--- | :--- |\n",
                    *[f"| ${k}$ | `{v}` | `{k}` | Parameter of optimization |\n" for k, v in concept_data["shapes"].items()],
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Starter cell: Plot the visual behavior of the concept\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "\n",
                    "rng = np.random.default_rng(42)\n",
                    "\n",
                    "# Vectorized implementation:\n",
                    f"# {concept_data['numpy_code']}\n",
                    "\n",
                    concept_data["plot_code"]
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## ❓ Socratic Prompts\n",
                    "- *How does the rate of change (derivative) behave at extreme values?*\n",
                    "- *If you change the learning rate parameters, how does the optimization trajectory shift?*\n",
                    "\n",
                    "## 🧠 Open Mystery Stack\n",
                    "- What still feels muddy mathematically?\n",
                    "- Add at least one intuition block or confusion to `99_open_mystery_stack/open_mystery_stack.md`.\n",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ml_alpha)",
                "language": "python",
                "name": "ml_alpha",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(nb, indent=2), encoding="utf-8")


def notebook_build_day(path: Path, title: str, topic: str, concept_data: dict, resources: list[str]) -> None:
    """Generates the Coding and Build Notebook for Days 2, 4, 6."""
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    f"Topic: {topic}\n",
                    "\n",
                    "## 🎯 Build Objective\n",
                    f"We will implement the vectorized math we analyzed yesterday from scratch using only NumPy. Then, we will benchmark it against the target library framework to verify correctness.\n",
                    "\n",
                    "### Target Equation to Implement:\n",
                    f"$$\n{concept_data['equation']}\n$$\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 1. Implement From-Scratch (NumPy Only)\n",
                    "class FromScratchModel:\n",
                    "    def __init__(self):\n",
                    "        self.w = None\n",
                    "        self.b = 0\n",
                    "\n",
                    "    def fit(self, X, y):\n",
                    "        # Add your from-scratch vector parameter update loop here\n",
                    "        pass\n",
                    "\n",
                    "    def predict(self, X):\n",
                    "        # Implement: prediction mapping\n",
                    "        pass\n",
                    "\n",
                    "# Sanity check assertions\n",
                    "X_test = np.random.randn(10, 2)\n",
                    "# assert predictions shape match targets!"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# 2. Framework Comparison\n",
                    "# Compare your model prediction outputs to standard scikit-learn or PyTorch modules\n",
                    "print('Benchmark and match predictions validation runs...')"
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📊 Benchmarking & Reflection\n",
                    "- Compare execution rtimes.\n",
                    "- Record one case where the framework makes optimization assumptions you didn't include from scratch.\n",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ml_alpha)",
                "language": "python",
                "name": "ml_alpha",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(nb, indent=2), encoding="utf-8")


def notebook_review_day(path: Path, title: str, topic: str, resources: list[str]) -> None:
    """Generates the Review Notebook for Day 7."""
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    f"Topic: {topic}\n",
                    "\n",
                    "Use this notebook to review the math and code implemented during the past week.\n",
                    "\n",
                    "## 💡 Weekly Feynman Check\n",
                    "Write out explanations of the three concepts covered this week in your own words:\n",
                    "1. **Concept A**\n",
                    "2. **Concept B**\n",
                    "3. **Concept C**\n",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🧹 Open Mystery Stack Cleanup\n",
                    "- Review the entries you wrote in your `open_mystery_stack.md` this week.\n",
                    "- Try to answer one query by testing parameters in code below, or mark it to move into next week's deep work blocks.\n"
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Use this cell to run small diagnostic experiments to resolve open questions."
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ml_alpha)",
                "language": "python",
                "name": "ml_alpha",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(nb, indent=2), encoding="utf-8")


def day_card(
    week_num: int,
    month_num: int,
    week_slug: str,
    day_num: int,
    day_title: str,
    notebook_name: str,
    topic: str,
    resources: list[str],
    deliverable: str,
) -> str:
    notebook_path = f"notebooks/day_{day_num:02d}_{notebook_name}.ipynb"
    
    if day_num in [1, 3, 5]:
        build_focus = "Focus: Mathematical foundations, LaTeX derivation on paper, and running the visual plot parameters."
        done_when = "You can explain the mathematical partial derivatives in 3 sentences, and you've run the concept plot."
    elif day_num in [2, 4, 6]:
        build_focus = "Focus: From-scratch class model implementation in NumPy, framework equivalent comparison, and assertion validation checks."
        done_when = "Your NumPy implementation matches the predictions of the library framework exactly, and all assert checks pass."
    else:
        build_focus = "Focus: Feynman checks, clean up of study notes, and cataloguing unresolved questions in the Open Mystery Stack."
        done_when = "Weekly review notebook is fully written out and the Open Mystery Stack table is updated."

    reading = resources[min(day_num - 1, len(resources) - 1)]
    extra_reading = resources[-1]
    
    return f"""# Week {week_num:02d} Day {day_num}: {day_title}

Month: {month_num:02d}
Topic: {topic}

## Reading
- Primary: {reading}
- Cross-check: {extra_reading}

## Execution Guide
- {build_focus}

## Notebook Worksheet
- Open and execute: [{notebook_path}]({notebook_path})

## Done When
- {done_when}
- You logged at least one curiosity or confusion in `99_open_mystery_stack/open_mystery_stack.md`.

## Deliverable Thread
This day contributes to: {deliverable}
"""


def week_plan(
    week_num: int,
    month_num: int,
    week_slug: str,
    topic: str,
    resources: list[str],
    deliverable: str,
) -> str:
    return f"""# Week {week_num:02d}: {topic}

Month: {month_num:02d}

## Concept Goal
Build math intuition first, then make it executable. By the end of this week, you should have mathematically derived and built from scratch three distinct core concepts.

## Required Resources
{chr(10).join(f"- {item}" for item in resources)}

## 2-Day Math-Weaved Concept Cycle
- **Days 1-2:** Concept A (Math exploration -> From-scratch/framework build)
- **Days 3-4:** Concept B (Math exploration -> From-scratch/framework build)
- **Days 5-6:** Concept C (Math exploration -> From-scratch/framework build)
- **Day 7:** Weekly review, Feynman synthesis, and Open Mystery Stack check.

## Weekly Deliverable
{deliverable}

## Daily Lessons Links
{chr(10).join(f"- [Day {i}: {title}](day_{i:02d}.md)" for i, (_, title, _) in enumerate(DAY_SPECS, 1))}
- [Socratic prompts](socratic_prompts.md)
- [Implementation task](implementation_task.md)
- [Review](review.md)
"""


def implementation_task(week_num: int, topic: str, deliverable: str) -> str:
    return f"""# Week {week_num:02d} Implementation Task

Topic: {topic}

## Stage 1: From Scratch (Days 2, 4, 6)
- Code the derived equations in clean python.
- Use NumPy only. Define output matrix shapes on paper before coding.

## Stage 2: Framework Comparison
- Import library equivalent (scikit-learn or PyTorch).
- Assert model outputs match within numerical thresholds: `np.allclose(atol=1e-5)`.

## Stage 3: Writeup
- Benchmark runtime and document structural assumptions.

Final deliverable: {deliverable}
"""


def review_file(week_num: int, topic: str) -> str:
    return f"""# Week {week_num:02d} Review

Topic: {topic}

## Completion Checklist
- [ ] I derived the math on paper for Concept A, B, and C.
- [ ] I implemented Concept A, B, and C from scratch in NumPy.
- [ ] I verified code correctness against library frameworks.
- [ ] I completed the Feynman check in the review notebook.
"""


def socratic_file(week_num: int, topic: str) -> str:
    return f"""# Week {week_num:02d} Socratic Prompts

Topic: {topic}

1. What problem does this math solve before we write code?
2. Which dimension shapes must align during matrix multiplications?
3. In which direction must weights shift if gradient calculations evaluate negative?
"""


def create_archives_and_roots() -> str:
    SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
    archive_note = "No old sandbox was found."
    if OLD_SANDBOX.exists() and not (OLD_SANDBOX / "README.md").read_text(encoding="utf-8", errors="ignore").startswith("# Old Sandbox Pointer"):
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_path = OLD_SANDBOX.with_name(f"ml-dl-sandbox_archive_{stamp}")
        shutil.move(str(OLD_SANDBOX), str(archive_path))
        OLD_SANDBOX.mkdir(parents=True, exist_ok=True)
        write(
            OLD_SANDBOX / "README.md",
            f"""# Old Sandbox Pointer

The old sandbox was archived here:

`{archive_path.as_posix()}`

The new canonical ML Alpha sandbox is:

`{NEW_SANDBOX_WIN}`

Start at:

`{NEW_SANDBOX_WIN}\\LESSON_INDEX.md`
""",
        )
        archive_note = f"Archived old sandbox to {archive_path.as_posix()}."
    elif OLD_SANDBOX.exists():
        archive_note = "Old sandbox pointer already exists; archive step skipped."
    return archive_note


def write_root_files(archive_note: str) -> None:
    write(
        SANDBOX_ROOT / "README.md",
        f"""# ML Alpha Sandbox

This is a 12-month, course-style machine learning sandbox built around active discovery and math-code mappings.

Start here:

- [LESSON_INDEX.md](LESSON_INDEX.md)
- [00_start_here/HOW_TO_USE_THIS_SANDBOX.md](00_start_here/HOW_TO_USE_THIS_SANDBOX.md)
- [RESOURCE_MANIFEST.md](RESOURCE_MANIFEST.md)
- [99_open_mystery_stack/open_mystery_stack.md](99_open_mystery_stack/open_mystery_stack.md)

2-Day Cycle Loop:
1. Concept Intake: Read, derive mathematical formulas on paper, run visualization plot.
2. Concept Build: Implement algorithm from scratch in NumPy, compare to library module, assert matches.

Archive note: {archive_note}
""",
    )
    write(
        SANDBOX_ROOT / ".gitignore",
        """.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
runs/
wandb/
mlruns/
data/raw/
data/downloads/
01_resources/repos/*/.git/
""",
    )
    write(
        SANDBOX_ROOT / "requirements.txt",
        """# === Core Data Science Stack ===
numpy
pandas
matplotlib
seaborn
scipy
scikit-learn
statsmodels
plotly
ipywidgets

# === Deep Learning & Orchestration ===
# NOTE: To utilize your Zephyrus G14 RTX GPU, install PyTorch explicitly using:
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
torch
torchvision
torchaudio
tqdm

# === Dev & Notebook environments ===
jupyterlab
notebook
ipykernel
requests
beautifulsoup4
mlflow
pytest
black
ruff
""",
    )
    write(
        SANDBOX_ROOT / "setup_windows.ps1",
        """# Run from PowerShell after installing Python and Git if they are not already available.
Set-Location -LiteralPath $PSScriptRoot
py -3.12 -m venv .venv
.\\.venv\\Scripts\\python.exe -m pip install --upgrade pip
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
.\\.venv\\Scripts\\python.exe -m ipykernel install --user --name ml_alpha --display-name "Python 3 (ml_alpha)"
Write-Host "Setup complete. Run .\\launch_jupyter.ps1 to open JupyterLab."
""",
    )
    write(
        SANDBOX_ROOT / "install_windows_tools.ps1",
        """# Optional helper. Run PowerShell normally; winget may ask for permission outside Codex.
winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements
winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
Write-Host "Restart PowerShell after installation, then run setup_windows.ps1."
""",
    )
    write(
        SANDBOX_ROOT / "launch_jupyter.ps1",
        """Set-Location -LiteralPath $PSScriptRoot
.\\.venv\\Scripts\\jupyter-lab.exe
""",
    )
    write(
        SANDBOX_ROOT / "clone_open_resources.ps1",
        "\n".join(
            [
                'Set-Location -LiteralPath "$PSScriptRoot\\01_resources\\repos"',
                "$repos = @(",
                *[f'  @{{Name="{name}"; Url="{url}"}},' for name, url in REPO_CLONES],
                ")",
                "foreach ($repo in $repos) {",
                "  if (-not (Test-Path -LiteralPath $repo.Name)) {",
                "    git clone --depth 1 $repo.Url $repo.Name",
                "  }",
                "}",
            ]
        ),
    )
    write(
        SANDBOX_ROOT / "00_start_here" / "HOW_TO_USE_THIS_SANDBOX.md",
        """# How To Use This Sandbox

Open `LESSON_INDEX.md`, choose the current week, then complete the daily card.

Active Learning Loop:
- Day A: Math, derivation, and visual plotting.
- Day B: NumPy build, framework benchmarks, and prediction validations.
""",
    )
    write(
        SANDBOX_ROOT / "00_start_here" / "DAILY_LOOP.md",
        """# Daily Loop

1. Visual scan: inspect figures, code, or outputs first.
2. Read: focus on the assigned section only.
3. Math worksheets: complete derivations and visual checks.
4. From-scratch: build the algorithm in NumPy.
5. Verification: run assert tests against frameworks.
""",
    )
    write(
        SANDBOX_ROOT / "00_start_here" / "SETUP_CHECKLIST.md",
        """# Setup Checklist

- [ ] Install real Windows Python 3.12.
- [ ] Install Git for Windows.
- [ ] Run `setup_windows.ps1`.
- [ ] Run `clone_open_resources.ps1` after Git is available.
- [ ] Open JupyterLab with `launch_jupyter.ps1`.
- [ ] Open Month 1 Week 1 Day 1.
""",
    )
    write(
        SANDBOX_ROOT / "99_open_mystery_stack" / "open_mystery_stack.md",
        """# Open Mystery Stack

Use this file to externalize bugs, intuitions, confusions, and architectural curiosities.

| Date | Week | Type | Mystery | Next smallest experiment | Status |
|---|---:|---|---|---|---|
| YYYY-MM-DD | 1 | intuition | Why does this model generalize? | Compare train/test loss on a toy dataset. | open |
""",
    )


def resource_manifest() -> str:
    rows = [
        "# Resource Manifest",
        "",
        "Only download or clone open/legal materials. For paid books, keep official links and use any official companion code repo separately.",
        "",
        "| Resource | Kind | URL | Status | Woven Weeks |",
        "|---|---|---|---|---|",
    ]
    for r in RESOURCES:
        rows.append(f"| {r['name']} | {r['kind']} | {r['url']} | {r['status']} | {r['weeks']} |")
    rows.extend(
        [
            "",
            "## Clone Plan",
            "",
            "Run `clone_open_resources.ps1` after Git for Windows is installed. Repos are shallow-cloned into `01_resources/repos/`.",
            "",
        ]
    )
    for name, url in REPO_CLONES:
        rows.append(f"- `{name}`: {url}")
    return "\n".join(rows) + "\n"


def lesson_index() -> str:
    lines = [
        "# Lesson Index",
        "",
        "This is the course portal. Each week has seven daily lesson cards, notebooks, prompts, implementation tasks, and a review.",
        "",
        "Weekly rhythm: three 2-day concept cycles (math + build) plus one synthesis review day.",
        "",
    ]
    current_month = None
    for week_num, month_num, week_slug, topic, _resources, deliverable in WEEKS:
        if month_num != current_month:
            current_month = month_num
            lines.append(f"## Month {month_num:02d}")
        folder = Path("02_curriculum") / f"month_{month_num:02d}" / f"week_{week_num:02d}_{week_slug}"
        lines.append(f"- [Week {week_num:02d}: {topic}]({rel_link(folder / 'week_plan.md')}) - {deliverable}")
    return "\n".join(lines) + "\n"


def twelve_month_map() -> str:
    month_titles = {
        1: "Data and Python foundations",
        2: "Linear regression and optimization",
        3: "Classification and resampling",
        4: "Regularization and feature engineering",
        5: "Trees, ensembles, SVMs, and classical ML capstone",
        6: "Neural networks, PyTorch, autograd, and backprop",
        7: "Computer vision",
        8: "NLP and transformers",
        9: "Specialization track",
        10: "Unsupervised and probabilistic learning",
        11: "Reinforcement learning",
        12: "Production ML and portfolio capstone",
    }
    lines = ["# 12-Month Map", ""]
    for month in range(1, 13):
        lines.append(f"## Month {month:02d}: {month_titles[month]}")
        for week in [w for w in WEEKS if w[1] == month]:
            lines.append(f"- Week {week[0]:02d}: {week[3]} - {week[5]}")
        lines.append("")
    return "\n".join(lines)


def build_curriculum() -> None:
    for week_num, month_num, week_slug, topic, resources, deliverable in WEEKS:
        folder = SANDBOX_ROOT / "02_curriculum" / f"month_{month_num:02d}" / f"week_{week_num:02d}_{week_slug}"
        write(folder / "week_plan.md", week_plan(week_num, month_num, week_slug, topic, resources, deliverable))
        write(folder / "socratic_prompts.md", socratic_file(week_num, topic))
        write(folder / "implementation_task.md", implementation_task(week_num, topic, deliverable))
        write(folder / "review.md", review_file(week_num, topic))
        
        # Populate Day Cards & Notebooks
        for day_num, (_day_id, day_title, notebook_name) in enumerate(DAY_SPECS, 1):
            write(
                folder / f"day_{day_num:02d}.md",
                day_card(week_num, month_num, week_slug, day_num, day_title, notebook_name, topic, resources, deliverable),
            )
            
            nb_path = folder / "notebooks" / f"day_{day_num:02d}_{notebook_name}.ipynb"
            
            # Map Day Num to Math Spec
            if day_num == 1:
                spec = get_math_spec(week_num, "a", topic)
                notebook_math_day(nb_path, f"Week {week_num:02d} - Concept A: {spec['title']}", topic, spec, resources)
            elif day_num == 2:
                spec = get_math_spec(week_num, "a", topic)
                notebook_build_day(nb_path, f"Week {week_num:02d} - Build A: {spec['title']}", topic, spec, resources)
            elif day_num == 3:
                spec = get_math_spec(week_num, "b", topic)
                notebook_math_day(nb_path, f"Week {week_num:02d} - Concept B: {spec['title']}", topic, spec, resources)
            elif day_num == 4:
                spec = get_math_spec(week_num, "b", topic)
                notebook_build_day(nb_path, f"Week {week_num:02d} - Build B: {spec['title']}", topic, spec, resources)
            elif day_num == 5:
                spec = get_math_spec(week_num, "c", topic)
                notebook_math_day(nb_path, f"Week {week_num:02d} - Concept C: {spec['title']}", topic, spec, resources)
            elif day_num == 6:
                spec = get_math_spec(week_num, "c", topic)
                notebook_build_day(nb_path, f"Week {week_num:02d} - Build C: {spec['title']}", topic, spec, resources)
            elif day_num == 7:
                notebook_review_day(nb_path, f"Week {week_num:02d} - Weekly Synthesis & Feynman Review", topic, resources)
                
        scratch = SANDBOX_ROOT / "03_from_scratch" / f"week_{week_num:02d}_{week_slug}"
        framework = SANDBOX_ROOT / "04_frameworks" / f"week_{week_num:02d}_{week_slug}"
        write(scratch / "README.md", f"# Week {week_num:02d} From-Scratch Work\n\nTopic: {topic}\n\nUse this folder for NumPy or low-level implementations.\n")
        write(framework / "README.md", f"# Week {week_num:02d} Framework Work\n\nTopic: {topic}\n\nUse this folder for scikit-learn, PyTorch, Hugging Face, or CleanRL comparisons.\n")
        
    for month in range(1, 13):
        write(
            SANDBOX_ROOT / "05_capstones" / f"month_{month:02d}" / "README.md",
            f"# Month {month:02d} Capstone Notes\n\nCollect benchmarks, reports, artifacts, and screenshots for this month.\n",
        )


def write_resource_dirs() -> None:
    write(SANDBOX_ROOT / "RESOURCE_MANIFEST.md", resource_manifest())
    write(SANDBOX_ROOT / "01_resources" / "RESOURCE_MANIFEST.md", resource_manifest())
    write(
        SANDBOX_ROOT / "01_resources" / "README.md",
        """# Resources

This folder stores links, legal/open downloads, and shallow-cloned code repositories.

- `books/`: official PDF links or legally open PDFs only.
- `courses/`: course notes, reading maps, and links.
- `repos/`: shallow clones from `clone_open_resources.ps1`.
- `papers/`: papers used by capstones and specialization weeks.
""",
    )
    for sub in ["books", "courses", "repos", "papers", "datasets"]:
        (SANDBOX_ROOT / "01_resources" / sub).mkdir(parents=True, exist_ok=True)


def main() -> None:
    archive_note = create_archives_and_roots()
    write_root_files(archive_note)
    write_resource_dirs()
    write(SANDBOX_ROOT / "LESSON_INDEX.md", lesson_index())
    write(SANDBOX_ROOT / "00_start_here" / "12_MONTH_MAP.md", twelve_month_map())
    build_curriculum()
    print(f"Built sandbox at {SANDBOX_ROOT}")
    print(archive_note)


if __name__ == "__main__":
    main()
