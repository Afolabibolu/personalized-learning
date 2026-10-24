# Neural Networks

## From biological to artificial neurons

In a biological neuron, the dendrites collect signals, the cell body processes them, and a strong enough signal travels down the axon to the next neuron. An **artificial neuron** copies this:

- **Inputs** x₁, x₂, … stand in for the dendrites.
- **Weights** w₁, w₂, … give the strength of each connection.
- A **summation** adds the weighted inputs and a **bias**: z = Σ wᵢxᵢ + b.
- An **activation function** decides the output, as the neuron's firing does.

A single artificial neuron is a **perceptron**. On its own it can only solve straight-line problems.

## The multilayer perceptron

A **multilayer perceptron (MLP)** is a feedforward network of fully connected neurons with non-linear activations. Information flows one way, from input to output.

- The **input layer** receives the raw data and does no computation.
- **Hidden layers** apply weights, biases and activations to learn complex patterns. With more than two hidden layers the network is called **deep**.
- The **output layer** produces the prediction: one neuron for binary classification, several for multi-class.

Weights and biases are learned during training. The bias shifts the activation and helps the network adjust its decision boundary.

## Activation functions

Activation functions add **non-linearity**, so the network can learn curves and complex shapes.

- **Sigmoid** squashes values into (0, 1), with 0.5 at z = 0. It reads as a probability.
- **Tanh** squashes values into (−1, 1) and is zero-centred, which makes it cleaner than sigmoid for deep networks.
- **ReLU** outputs 0 for negative inputs and passes positive inputs unchanged. It is the most popular choice because it is simple and fast.

**Output layer by task:**
- **Sigmoid** for binary classification, such as spam or not spam.
- **Softmax** for multi-class classification. It turns scores into probabilities that sum to 1, as in MNIST digit recognition.
- **Linear** for regression, such as a house price.

**Cost functions:** MSE for regression, binary cross-entropy for binary classification, and categorical cross-entropy for multi-class classification.

## How a network learns

1. **Forward pass:** inputs flow through the linear transformations and activations to a prediction p.
2. **Loss:** the cost function compares p with the true label y.
3. **Backward pass (backpropagation):** the **chain rule** carries the error back through the layers. It gives the gradient of the loss with respect to every weight and bias: how much each one contributed, and which way to change it.
4. **Update:** an **optimizer** such as stochastic gradient descent or Adam moves each weight against its gradient, scaled by the learning rate.

Training repeats over shuffled mini-batches until the loss stops falling (convergence).

**Hyperparameters to tune** include the learning rate, the number of hidden layers and neurons, the batch size, the number of epochs and the activation functions.

Source: My CSC 572 Note1.pdf (Neural Networks); ML Overview Slide_2025.pptx
