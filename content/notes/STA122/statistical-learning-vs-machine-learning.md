# Statistical Learning versus Machine Learning

## Two approaches

**Statistical learning** is rooted in classical statistics. It estimates functions that describe how inputs relate to outputs, often assumes a form (such as linear), and values **interpretability** and **hypothesis testing**. It suits small to medium structured data. Examples:

- linear regression for test scores;
- logistic regression for the probability that a customer buys;
- ANOVA for group differences.

**Machine learning** is a subset of AI whose algorithms learn patterns **without explicit programming**, with **prediction accuracy** as the main focus. It handles large and unstructured data, often with non-parametric models. Examples:

- decision trees for loan default;
- SVMs for spam;
- neural networks for objects;
- recommendation systems.

## Key differences

| Feature | Statistical learning | Machine learning |
| --- | --- | --- |
| Goal | inference, understanding | prediction, performance |
| Model | parametric (linear, logistic) | flexible (trees, SVMs) |
| Interpretability | high | low to medium (black boxes) |
| Data size | small to medium | large, high-dimensional |
| Assumptions | linearity, normality | few |
| Output | coefficients, p-values, CIs | predictions, labels |

**Workflows**: statistical learning assumes a model form and evaluates it with p-values, R² and residual analysis. ML lets the algorithm find patterns and evaluates them with **cross-validation**, accuracy and ROC curves.

## Fitting and trade-offs

- An **underfitted** model (a flat line) is too simple.
- A **well-fitted** curve balances complexity.
- An **overfitted** model follows every point, noise included, and predicts new data badly.

Simple statistical models rarely overfit. Flexible ML models are prone to it unless **regularised**: Lasso and Ridge penalise large coefficients.

There is a **trade-off between interpretability and accuracy**. Linear models are easy to explain but may miss complex patterns. Neural networks are accurate but are black boxes. Decision trees sit in between.

## Together

Use both:

- **understand first** with statistical learning;
- **then predict** with ML when accuracy matters.

Examples:

- exam scores: linear regression on study time, then a random forest adding sleep and attendance;
- churn: logistic regression, then gradient boosting;
- disease: logistic regression on records, then deep learning on scans;
- stock trends: time-series regression, then recurrent neural networks.

When lives or rights are at stake, as in healthcare or loans, **interpretability** often matters more than a small gain in accuracy.

Source: STA 122 Module 2: Statistical Learning vs. Machine Learning (Akintande)
