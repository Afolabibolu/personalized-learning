# Decision Trees and Random Forests

## Decision trees

A **decision tree** predicts by asking a sequence of questions about the features. Each **internal node** tests one feature (for example "humidity > 70%?"), each **branch** is an outcome of the test, and each **leaf** gives the prediction: a class for classification, or a number for regression. Trees need no feature scaling and are easy to explain.

A tree is grown top-down and greedily (ID3, C4.5, CART). At each node the algorithm picks the split that makes the child nodes purest:

- **Entropy:** H = −Σ pᵢ log₂ pᵢ over the classes in the node. It is 0 for a pure node and 1 for a 50/50 split of two classes. **Information gain** is the parent's entropy minus the weighted entropy of the children.
- **Gini impurity:** 1 − Σ pᵢ², used by CART.
- For regression, the split that most reduces the variance (mean squared error) of the target.

Splitting stops when a node is pure or a limit is reached.

## Overfitting and pruning

A tree grown without limits keeps splitting until each leaf holds a few training examples. It then fits the training data almost perfectly but does badly on new data: **overfitting** (high variance). A very shallow tree is too simple and does badly on both: **underfitting** (high bias).

- **Pre-pruning** (early stopping) stops growth during training, using limits such as maximum depth, minimum samples to split a node, minimum samples per leaf or a minimum impurity decrease. It is cheap but can stop too early.
- **Post-pruning** grows the full tree, then removes branches that do not improve performance on validation data, for example by cost-complexity pruning. It is slower but usually generalises better, especially with enough data for validation.

## Random forests

An **ensemble** combines many models. **Bagging** (bootstrap aggregating) trains each model on a bootstrap sample, drawn from the training set with replacement, and aggregates their predictions. A **random forest** is bagging of decision trees plus **feature randomness**: each split considers only a random subset of the features, so the trees differ more from one another.

- **Classification:** majority vote of the trees (or the average of their class probabilities).
- **Regression:** the average of the trees' predictions.

Each deep tree has low bias but high variance. Averaging many trees that disagree **reduces the variance** without much increase in bias, which is how a random forest handles the bias–variance trade-off. Adding more trees makes predictions more stable and does not cause overfitting, but the gains level off while training and prediction cost keep rising. Random forests usually need **no pruning**, because the averaging controls variance. The examples left out of each tree's bootstrap sample give an **out-of-bag** error estimate.

**Strengths:** accurate, robust to noise and outliers, little preprocessing, feature importances. **Weaknesses:** harder to interpret than one tree, slower and larger in memory.

Source: general knowledge, following the 2023/24 CSC 572 paper (Questions 2 and 3); no lecture file in the folder covers decision trees
