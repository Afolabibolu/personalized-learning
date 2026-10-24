# Linear Regression and Gradient Descent

## Linear regression

Linear regression models the relationship between a continuous output y and one or more inputs X by fitting a straight line. With two inputs the line becomes a plane, and with more inputs a hyperplane. One input is **simple** linear regression; several inputs make it **multiple** linear regression.

The simple model is **y = b0 + b1·x**. Its coefficients are estimated from the training data:

- b1 = Σ(xᵢ − mean(x))(yᵢ − mean(y)) / Σ(xᵢ − mean(x))², which is the covariance divided by the variance.
- b0 = mean(y) − b1 · mean(x).

The Lesson 3 practical builds this from scratch in Python. It writes functions for the mean, variance and covariance, then the two coefficients, then makes predictions and computes the RMSE.

**Weights and bias.** Weights say how much each feature matters. The bias shifts the line up or down. In score = 5 × hours_studied + 2 × hours_slept + 10, the weights are 5 and 2 and the bias is 10. θ often stands for all the parameters together.

## Loss and cost

The **loss** measures the error on one example. The squared error is L = (yᵢ − ŷᵢ)². Squaring removes negative signs and makes large errors count more. The **cost** J(θ) averages the loss over the whole dataset, usually as the **mean squared error (MSE)**, sometimes with a factor of ½ for convenience when differentiating. Training means finding the parameters that minimise the cost.

## Gradient descent

Gradient descent is an optimisation algorithm that adjusts the parameters step by step in the direction that reduces the error fastest. Picture walking downhill at night by feeling the slope. The height is the cost, the slope is the gradient, and each step is a parameter update.

1. Initialise the weights and bias, randomly or to zero.
2. Set the learning rate η, for example 0.01.
3. Repeat until convergence or for a fixed number of epochs:
   - compute the predictions;
   - compute the gradient of the cost;
   - update each parameter against the gradient: **new weight = old weight − η × gradient**.

**Convergence** is reached when the cost stops changing much.

## Three strategies

- **Batch:** uses the whole dataset for each step. It is accurate and smooth, but slow on large data.
- **Stochastic (SGD):** updates after every single example. It is fast but noisy, and the noise can help it escape local minima.
- **Mini-batch:** updates on small batches, such as 32 or 64 examples. It is fast and stable, and almost every deep learning model uses it.

## The learning rate

- **Too small:** progress is slow and takes long to reach the minimum.
- **Too large:** the step **overshoots** the minimum and may bounce around it or diverge.
- **Zero:** the parameters never change.

The right rate reaches the minimum in reasonable time.

Source: Lesson 3_ Basic Linear Regression.pdf; ML Overview Slide_2025.pptx; My CSC 572 Note1.pdf
