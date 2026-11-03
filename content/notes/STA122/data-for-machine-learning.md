# Data for Machine Learning

## Statistics comes first

The lecture's "statistics injunction" is that ML rests on statistics: before choosing a model, know what kind of data you have.

**Categorical (qualitative) data** fall into categories:

- **nominal**: categories with no order. They are **binary** with two classes (spam or not, 0 or 1) or **non-binary** with more (blood group, state of origin);
- **ordinal**: ordered categories (cancer stage, class of degree, ratings).

**Metric (quantitative or measurement) data** are numbers:

- **interval**: equal steps but no true zero (temperature in °C);
- **ratio**: equal steps and a true zero (income, weight, rainfall in mm).

The measurement scale decides the task. A categorical target leads to **classification**, and a metric target to **prediction (regression)**.

## Modern data classes: TAP

Much modern data is **unstructured**, falling into three classes:

- **Text**, handled by natural language processing (NLP): machine translation, sentiment analysis, information retrieval, question answering;
- **Audio or speech**: speech recognition turns a spoken "hello" into digital form and text;
- **Pictures or images**: classifying cells in a medical image, recognising faces.

**Structured** data sit in tables of rows (cases) and columns (variables). Unstructured data must usually be converted into numbers (features) before a model can use them.

## Training, testing and validation

Learning has three stages:

- **Training** (the learning stage): the model learns patterns from historical data.
- **Testing**: the model is assessed on data it has not seen, to measure the knowledge gained so far.
- **Validation**: checking that the knowledge the model seems to have gained is true to the task, for example by tuning settings on a separate validation set or by cross-validation.

A common split is about 70–80% of the data for training and the rest for testing. A model scored only on its training data can look much better than it really is.

## Features

The inputs a model uses are called **features**, and building good ones from raw data is **feature engineering**: for example, turning a date into "day of the week", or a text into word counts. Data preparation, including cleaning, handling missing values and encoding categories as numbers, often takes most of the time in a project.

Source: STA 122 Machine Learning and Computational Statistics, Part I (Akintande); STA 122 Module 1: Introduction to Machine Learning (Dr O.J. Akintande); General knowledge of STA 122 for structured data, the training/test split, cross-validation and feature engineering
