# Logistic Regression

## What it is

Logistic regression is a supervised machine learning algorithm for **classification**. It predicts the probability that an instance belongs to a class. The course example predicts whether a user will click on an online ad (1) or not (0) from features such as age, area income, daily time on site and internet usage.

It is called regression because it extends linear regression, but it is used mainly for classification. The outcome must be categorical (yes or no, 0 or 1, true or false). Instead of exactly 0 or 1, the model gives a probability between 0 and 1. Instead of fitting a straight line, it fits an **S-shaped** logistic curve.

## Assumptions

1. **Independent observations:** no correlation between observations.
2. **Binary dependent variable:** only two values. For more than two classes, softmax is used.
3. **Linear relationship** between the independent variables and the **log-odds** of the dependent variable.
4. **No outliers** in the dataset.
5. **A large sample size.**

## The sigmoid function

First compute the linear combination z = w · X + b. Then pass it through the **sigmoid** (logistic) function:

**σ(z) = 1 / (1 + e^(−z))**

σ(z) tends to 1 as z → ∞ and to 0 as z → −∞, and it always stays between 0 and 1. A **threshold**, typically 0.5, turns the probability into a class: above it is class 1, below it is class 0. At z = 0 the output is exactly 0.5.

## Odds and log-odds

**Odds** are the ratio of something happening to it not happening, p / (1 − p). This differs from probability, which compares it with everything that could happen. A probability of 0.8 gives odds of 0.8 / 0.2 = 4. Logistic regression models the **log-odds (logit)**:

log(p / (1 − p)) = w · X + b

Solving for p gives back p = 1 / (1 + e^(−(w · X + b))), which is the sigmoid.

## Training

The parameters are estimated by **maximum likelihood estimation (MLE)**. The likelihood of the dataset is the product of each example's likelihood, assuming the examples are independent. Taking logs gives the log-likelihood, which is more stable numerically. Optimisers minimise, so we minimise the **negative log-likelihood**, known in ML as the **binary cross-entropy (log loss)**. The cost J(w, b) averages that loss over the m examples.

Training uses **gradient descent**:
1. Initialise w and b.
2. Compute the predictions.
3. Compute the loss and the cost.
4. Compute the gradients.
5. Update the parameters.
6. Repeat until convergence.

Advanced optimisers such as Adam can replace plain gradient descent. The pipeline is: features and binary labels go in, the model applies the sigmoid, the loss is binary cross-entropy, and the output is the w and b that best separate the classes.

The course assignment applies it to predicting loan defaults on the SBA loans dataset.

Source: Logistics Regression Explained.pdf; My CSC 572 Note1.pdf
