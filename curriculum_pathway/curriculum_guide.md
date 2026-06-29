# Conceptual Machine Learning Pathway: Lesson-by-Lesson Study Guide

Welcome to your structured Machine Learning learning path! The notebooks are now organized into nested subfolders in [curriculum_pathway](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway). 

This guide maps **every individual lesson (notebook)** directly to the required readings in **Introduction to Statistical Learning (ISLP)** and **Hands-on Machine Learning (HOML3)**.

---

## 🗺️ Reorganized Lesson-by-Lesson Map

### 📁 [00_prerequisites/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/00_prerequisites)
*Focus on tool setup, vector transposes, and basic gradients.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Matrix transposes, multiplications, vector derivatives, and Socratic checkpoints.
* **Lesson 01:** `01_tools_numpy.ipynb`
  * 📖 **Reading**: None. Review core NumPy multidimensional arrays.
* **Lesson 02:** `02_tools_pandas.ipynb`
  * 📖 **Reading**: None. Review data loading, series, and DataFrame aggregations.
* **Lesson 03:** `03_tools_matplotlib.ipynb`
  * 📖 **Reading**: None. Focus on scatter plots, line plots, and subplots.
* **Lesson 04:** `04_math_linear_algebra.ipynb`
  * 📖 **Reading**: Standard textbook Linear Algebra review (vector products, transposes, matrix inversion).
* **Lesson 05:** `05_math_differential_calculus.ipynb`
  * 📖 **Reading**: Basic calculus review (partial derivatives, function minimization). Reference **HOML3 Appendix B** (Autodiff theory).
* **Lesson 06 (Jon Krohn Linear Algebra I):** `06_krohn_intro_to_linear_algebra.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Linear Algebra I*. Focus on vectors, matrices, systems of linear equations, tensor operations, and norms.
* **Lesson 07 (Jon Krohn Linear Algebra II):** `07_krohn_linear_algebra_ii.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Linear Algebra II*. Focus on eigendecomposition, singular value decomposition (SVD), and Principal Component Analysis (PCA).
* **Lesson 08 (Jon Krohn Calculus I):** `08_krohn_calculus_i.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Calculus I*. Focus on limits, derivatives, rules of differentiation, and the chain rule.
* **Lesson 09 (Jon Krohn Calculus II):** `09_krohn_calculus_ii.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Calculus II*. Focus on partial derivatives, gradients, backpropagation gradients, and Hessians.
* **Lesson 10 (Jon Krohn Probability):** `10_krohn_probability.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Probability*. Focus on probability theory, Bayes' theorem, probability distributions, information theory, and entropy.
* **Lesson 11 (Jon Krohn Statistics):** `11_krohn_statistics.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Statistics*. Focus on descriptive statistics, central limit theorem, hypothesis testing (t-tests, ANOVA), and Pearson correlation.
* **Lesson 12 (Jon Krohn CS & Algorithms):** `12_krohn_algos_and_data_structures.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations Chapter/Video: *Computer Science & Algorithms*. Focus on Big O notation, data structures (arrays, trees, graphs), sorting, searching, and optimization.

---

### 📁 [01_foundations/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/01_foundations)
*Statistical learning frameworks, bias-variance tradeoff, and full pipeline engineering.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — ML pipelines, scaling transformers, data leakage, and bias-variance balance.
* **Lesson 01:** `01_the_machine_learning_landscape.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 1**: *The Machine Learning Landscape*.
* **Lesson 02:** `02_statistical_learning-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 2**: *Statistical Learning* (Sections 2.1 - 2.2). Focus on estimating $f$, parametric vs. non-parametric methods, and the bias-variance tradeoff.
* **Lesson 03:** `03_end_to_end_machine_learning_project.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 2**: *End-to-End Machine Learning Project*.
* **Lesson 04:** `04_ml-project-checklist.md`
  * 📖 **Reading**: **HOML3 Appendix A**: *Machine Learning Project Checklist*.

---

### 📁 [02_regression/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/02_regression)
*Fitting linear curves and understanding numerical optimization.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Normal Equation derivation, Gradient Descent parameter updates, learning curves, and complexity comparisons.
* **Lesson 01:** `01_linear_regression-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 3**: *Linear Regression*. Focus on coefficient estimation, hypothesis testing ($p$-values, $F$-statistic), and multiple linear regression.
* **Lesson 02:** `02_training_linear_models.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 4**: *Training Models* (sections on Linear Regression, Gradient Descent, Polynomial Regression, and Learning Curves).
* **Lesson 03:** `03_extra_gradient_descent_comparison.ipynb`
  * 📖 **Reading**: Re-read **HOML3 Chapter 4**: *Gradient Descent* sections comparing Batch, Stochastic, and Mini-batch GD.
* **Lesson 04:** `04_extra_autodiff.ipynb`
  * 📖 **Reading**: **HOML3 Appendix B**: *Automatic Differentiation* (forward-mode vs. reverse-mode autodiff mathematics).
* **Lesson 05 (💻 Active Coding Practice):** `05_practice_linear_regression_from_scratch.ipynb`
  * 📖 **Reading**: Synthesize formulas from **ISLP Chapter 3** and **HOML3 Chapter 4** to write gradient descent and the Normal Equation from scratch.
* **Lesson 06 (Jon Krohn Optimization):** `06_krohn_optimization.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Optimization*. Focus on objective functions, local/global minima, convex optimization, and gradient-based learning.
* **Lesson 07 (Jon Krohn Single-Point Gradient):** `07_krohn_single_point_regression_gradient.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Single-Point Regression Gradient*. Simple visualization of calculating parameter updates on a single data point.
* **Lesson 08 (Jon Krohn Batch Regression Gradient):** `08_krohn_batch_regression_gradient.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Batch Regression Gradient*. Extending single-point gradient calculus to batch linear regression optimization.
* **Lesson 09 (Jon Krohn GD from Scratch):** `09_krohn_gradient_descent_from_scratch.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Gradient Descent from Scratch*. Hands-on implementation of parameter updates and visualization.
* **Lesson 10 (Jon Krohn SGD from Scratch):** `10_krohn_sgd_from_scratch.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Stochastic Gradient Descent from Scratch*. Implementing SGD and mini-batch gradient descent.

---

### 📁 [03_classification/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/03_classification)
*Probability boundaries, log-odds, and performance metrics.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Log-odds logits, sigmoid activation function mapping, confusion matrices, ROC/AUC.
* **Lesson 01:** `01_classification-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 4**: *Classification* (Sections 4.1 - 4.3). Focus on Logistic Regression log-odds, LDA, QDA, Naive Bayes, and KNN.
* **Lesson 02:** `02_classification.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 3**: *Classification*. Focus on confusion matrices, Precision, Recall, and the ROC curve.
* **Lesson 03 (💻 Active Coding Practice):** `03_practice_classification_and_metrics.ipynb`
  * 📖 **Reading**: Review metric formulas in **HOML3 Chapter 3** to build custom precision, recall, and ROC evaluations.

---

### 📁 [04_resampling_validation/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/04_resampling_validation)
*Validating model generalizations.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — LOOCV variance, K-Fold cross-validation loops, and bootstrap sampling.
* **Lesson 01:** `01_resample-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 5**: *Resampling Methods* (Sections 5.1 - 5.2). Focus on validation sets, K-Fold CV, LOOCV, and the Bootstrap.

---

### 📁 [05_regularization_selection/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/05_regularization_selection)
*Controlling model capacity with weight shrinkage.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Lasso (L1) vs Ridge (L2) mathematical formulas, geometric boundary shapes, and Elastic Net regularizers.
* **Lesson 01:** `01_variable_selection-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 6**: *Linear Model Selection and Regularization*. Focus on subset selection, Ridge Regression (L2 regularization), and Lasso (L1 regularization).
* **Lesson 02 (💻 Active Coding Practice):** `02_practice_regularization_and_resampling.ipynb`
  * 📖 **Reading**: Synthesize **ISLP Chapter 6** and **HOML3 Chapter 4** (Regularized Linear Models section) to implement L1/L2 penalties and CV loops from scratch.

---

### 📁 [06_nonlinear_models/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/06_nonlinear_models)
*Expanding beyond straight lines.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Natural/smoothing splines, knots, step constraints, and Generalized Additive Models (GAMs).
* **Lesson 01:** `01_nonlinear-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 7**: *Moving Beyond Linearity*. Focus on polynomial regression, cubic/natural splines, smoothing splines, and GAMs.

---

### 📁 [07_svm/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/07_svm)
*Optimal margins and high-dimensional kernels.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Hard/soft margins, hinge loss optimization, primal/dual forms, and RBF kernel structures.
* **Lesson 01:** `01_svm-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 9**: *Support Vector Machines*. Focus on support vector classifiers and kernel extensions.
* **Lesson 02:** `02_support_vector_machines.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 5**: *Support Vector Machines*. Focus on hinge loss, soft margins ($C$), and dual formulations.

---

### 📁 [08_trees_ensembles/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/08_trees_ensembles)
*Splitting boundaries and aggregating estimators.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Gini impurity vs Entropy mathematical formulas, bagging vs boosting, Random Forest feature subsetting.
* **Lesson 01:** `01_decision_trees.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 6**: *Decision Trees*. Focus on CART algorithm and Gini impurity.
* **Lesson 02:** `02_bagging_boosting-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 8**: *Tree-Based Methods*. Focus on bagging, Random Forests, and Boosting.
* **Lesson 03:** `03_ensemble_learning_and_random_forests.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 7**: *Ensemble Learning and Random Forests*. Focus on voting classifiers, bagging/pasting, AdaBoost, and Gradient Boosting.

---

### 📁 [09_dimensionality_reduction/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/09_dimensionality_reduction)
*Projecting and manifold embedding.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Singular Value Decomposition (SVD), principal components projection, explained variance ratio calculation.
* **Lesson 01:** `01_dimensionality_reduction.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 8**: *Dimensionality Reduction*. Focus on PCA (projection, principal components, explained variance), Kernel PCA, and LLE.

---

### 📁 [10_unsupervised_learning/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/10_unsupervised_learning)
*Grouping datasets without targets.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — K-Means inertia minimization, centroid updates, DBSCAN parameters, linkages.
* **Lesson 01:** `01_unsupervised-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 12**: *Unsupervised Learning* (Sections 12.1 - 12.4). Focus on K-means and Hierarchical clustering.
* **Lesson 02:** `02_unsupervisedervised_learning.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 9**: *Unsupervised Learning Techniques*. Focus on K-means centroid updates, DBSCAN, and Gaussian Mixture Models (GMMs).

---

### 📁 [11_survival_multiple_testing/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/11_survival_multiple_testing)
*Time-to-event curves and significance thresholds.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Right censoring, Kaplan-Meier equations, Cox proportional hazards, FWER (Bonferroni) vs FDR (Benjamini-Hochberg).
* **Lesson 01:** `01_survival-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 11**: *Survival Analysis*. Focus on Kaplan-Meier estimators and Cox proportional hazards.
* **Lesson 02:** `02_multiple-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 13**: *Multiple Testing*. Focus on control metrics (FWER, FDR) and p-value adjustments.

---

### 📁 [12_deep_learning_foundations/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/12_deep_learning_foundations)
*Building feedforward networks, activations, and tf.data pipelines.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — MLP linear/activation forward layers, ReLU vs Sigmoid activation partial derivatives, gradient update logic.
* **Lesson 01:** `01_deep_learning-lab.ipynb`
  * 📖 **Reading**: **ISLP Chapter 10**: *Deep Learning* (MLP and activation sections).
* **Lesson 02:** `02_neural_nets_with_keras.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 10**: *Introduction to Artificial Neural Networks with Keras*. Focus on perceptrons, MLPs, Sequential API, and Subclassing API.
* **Lesson 03:** `03_training_deep_neural_networks.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 11**: *Training Deep Neural Networks*. Focus on vanishing gradients, He initialization, ELU/Swish activations, Batch Normalization, and optimizers (RMSprop, Adam).
* **Lesson 04:** `04_custom_models_and_training_with_tensorflow.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 12**: *Custom Models and Training with TensorFlow*. Focus on Tensors, custom loss functions, custom layers, and writing training loops with GradientTape.
* **Lesson 05:** `05_loading_and_preprocessing_data.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 13**: *Loading and Preprocessing Data with TensorFlow*. Focus on tf.data API, dataset transformations, TFRecord, and feature columns.
* **Lesson 06:** `06_extra_ann_architectures.ipynb`
  * 📖 **Reading**: Review advanced MLP optimization and custom subclassing pipelines.
* **Lesson 07 (💻 Active Coding Practice):** `07_practice_numpy_mlp_backpropagation.ipynb`
  * 📖 **Reading**: Synthesize **ISLP Chapter 10** and **HOML3 Chapter 10** backpropagation matrix mathematics to code neural network gradients entirely in NumPy.
* **Lesson 08 (Jon Krohn Artificial Neurons):** `08_krohn_artificial_neurons.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Artificial Neurons*. Focus on Sigmoid, Tanh, and ReLU activations in a single neuron.
* **Lesson 09 (Jon Krohn Learning Rate Scheduling):** `09_krohn_learning_rate_scheduling.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Learning Rate Scheduling*. Practical study of learning rate decay and adaptive scheduling techniques.
* **Lesson 10 (Jon Krohn PyTorch Regression):** `10_krohn_regression_in_pytorch.ipynb`
  * 📖 **Reading**: Jon Krohn ML Foundations: *Regression in PyTorch*. Building your first PyTorch models to perform regression, linking back to earlier concepts in PyTorch.

---

### 📁 [13_advanced_deep_learning/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/13_advanced_deep_learning)
*Convolutions, sequences, attention transformers, and generative modeling.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Convolution receptive sharing, LSTM/GRU memory gates, Query-Key-Value self-attention math, generative models (Autoencoders, GANs, Diffusion).
* **Lesson 01:** `01_deep_computer_vision_with_cnns.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 14**: *Deep Computer Vision Using Convolutional Neural Networks*. Focus on convolutional layers, padding, pooling, and residual architectures (ResNet).
* **Lesson 02:** `02_processing_sequences_using_rnns_and_cnns.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 15**: *Processing Sequences Using RNNs and CNNs*. Focus on recurrent cells, LSTMs, GRUs, and 1D CNN seq processors.
* **Lesson 03:** `03_nlp_with_rnns_and_attention.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 16**: *Natural Language Processing with RNNs and Attention*. Focus on encoder-decoder models, self-attention mechanisms, and the Transformer architecture.
* **Lesson 04:** `04_autoencoders_gans_and_diffusion_models.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 17**: *Autoencoders, GANs, and Diffusion Models*. Focus on generative modeling.

---

### 📁 [14_reinforcement_learning/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/14_reinforcement_learning)
*Optimal policies in dynamic environments.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Bellman optimality equations, Q-table updates, exploration vs exploitation balance.
* **Lesson 01:** `01_reinforcement_learning.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 18**: *Reinforcement Learning*. Focus on Markov Decision Processes, policy gradients, and Q-Learning.

---

### 📁 [15_production_scaling/](file:///c:/Users/adisr/OneDrive/Documents/ml/ml_alpha/curriculum_pathway/15_production_scaling)
*Model serving, serialization, and latency.*
* **Lesson 00 (📖 Crash Course Study Notes):** `00_crash_course_notes.ipynb` — Latency vs throughput metrics, TF Serving structures, model quantization.
* **Lesson 01:** `01_training_and_deploying_at_scale.ipynb`
  * 📖 **Reading**: **HOML3 Chapter 19**: *Training and Deploying TensorFlow Models at Scale*. Focus on TF Serving, Vertex AI pipelines, and TFLite.
