# Learning Categories

## Y ~ f(X)

Most learning tasks look for a function linking an output to inputs: **Y ~ f(X)**.

- **Y** goes by many names: dependent, outcome, output, explained, response, regressand, **target** or **label** variable.
- **X** is the independent, predictor, explanatory, regressor or input variable, the **features**, or a covariate.

## Supervised learning

In **supervised** learning the data include the output Y. A "supervisor" supplies the desired outputs for the training set, and the algorithm learns f.

**Predictive (regression) tasks** have a **metric** Y (interval or ratio). For example:

**Ŷ = 0.04 + 0.4x₁ + 4x₂ + 5.6x₃ + 2.3x₄**

Here each coefficient is the change in Ŷ for a one-unit change in its x, with the others fixed. Accuracy is judged by the **mean squared error, MSE = Σ(Y − Ŷ)²/n**.

**Classification tasks** have a **categorical** Y (nominal or ordinal), often coded {0, 1}:

- cancer diagnosis: 0 = no cancer, 1 = cancer;
- tumour: 0 = benign, 1 = malignant;
- email: 0 = not spam, 1 = spam;
- website: 0 = not phishing, 1 = phishing.

Supervised learning has two phases:

1. **Training**: historical data are passed to an ML algorithm to build a predictive model.
2. **Testing**: new data are passed to the model to give predictions.

## Unsupervised learning

In **unsupervised** learning there is **no output Y**, only f(X's). The algorithm looks for structure:

- **clusters** of similar cases, such as customer segments;
- **correlation or association** between variables.

The lecture groups these as correlation/cluster-based tasks, against the regression-based tasks of supervised learning.

## Other categories

- **Semi-supervised** learning uses a few labelled cases with many unlabelled ones.
- **Self-supervised** learning creates its own labels from the data, such as predicting the next word in a sentence.

The lecture also places **operations research** (optimisation) beside these categories.

## Choosing the category

Ask: is there a target? If not, the task is unsupervised. If there is, ask whether it is metric (prediction) or categorical (classification). The choice of metrics follows from this:

- MSE or MAE for prediction;
- accuracy, precision and recall for classification.

Computational statistics sits where **statistics, mathematics, machine learning and AI** meet.

Source: STA 122 Machine Learning and Computational Statistics, Part I (Akintande); General knowledge of STA 122 for semi-supervised and self-supervised learning and the interpretation of coefficients
