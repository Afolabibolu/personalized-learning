# Introduction to Machine Learning

## What machine learning is

Machine learning (ML) is a branch of artificial intelligence that lets computers learn patterns from data and improve their performance over time without being explicitly programmed. Arthur Samuel (1959) called it "the field of study that gives computers the ability to learn without being explicitly programmed."

- **Traditional programming:** data and rules go in, output comes out.
- **Machine learning:** data and outputs go in, and the rules are learned.

Rule-based systems and typical chess engines are AI but not ML, because they do not learn from data. **Deep learning** is the part of ML that uses neural networks with many layers. **Generative AI** sits inside deep learning and creates new text, images or audio. GPT and Stable Diffusion are examples.

## Types of learning

- **Supervised learning** trains on examples with the correct answers (labels).
  - *Classification* predicts a category, such as spam or not spam.
  - *Regression* predicts a number, such as a house price.
- **Unsupervised learning** has no labels and finds hidden structure.
  - *Clustering* groups similar items, such as customer segments.
  - *Dimensionality reduction* simplifies data by reducing the number of features while keeping the important information.
- **Semi-supervised learning** uses a few labelled examples with many unlabelled ones, for example 500 labelled medical scans among 10,000.
- **Reinforcement learning:** an agent acts in an environment and receives rewards or penalties, learning a policy that maximises total reward. Self-driving cars and DeepMind's AlphaGo are examples.

## Key terms

- **Feature:** an input, independent variable, predictor or attribute.
- **Label (target):** the output, dependent variable or response.
- **Instance:** one sample, record or data point.
- **Model:** a mathematical representation trained to recognise patterns and make predictions.
- **Parameters (weights):** values the model learns during training.
- **Hyperparameters:** settings chosen before training to control it, such as the learning rate.
- **Loss function:** how wrong a prediction is. It is also called the cost, objective or error function.

## Applications and ethics

ML is used for fraud detection and algorithmic trading in finance, for disease-risk prediction and medical image analysis in healthcare, and for recommendations and spam detection on social media. Netflix, for example, recommends shows from your watch history. Its ethical challenges:

- **Bias:** models can reinforce human biases.
- **Privacy:** personal data must be protected.
- **Transparency:** many models are black boxes.
- **Jobs:** automation removes some jobs and creates others.

## Tools

The practicals use Python. Either install **Anaconda**, which includes NumPy, scikit-learn, Matplotlib and Jupyter notebooks, or install Python with **pip** and run `pip install --user numpy scipy matplotlib ipython jupyter pandas`. Python is chosen for its rich ecosystem of data science tools.

Source: Week1_Intro_to_ML_Lesson_Visuals.pptx; ML Overview Slide_2025.pptx; Lesson 1_ ML getting started.pdf; My CSC 572 Note1.pdf
