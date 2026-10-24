# Feature Engineering

## What it is

Features are the inputs to an ML model. **Feature engineering** is the process of creating features from raw data or selecting the best features for a model.

## Discrete data

Discrete data is made of separate, countable values or categories:

- **count data:** for example, 30 students in a class
- **categorical data:** for example, gender
- **binary data:** for example, has a device, yes or no
- **textual data:** for example, a product review of "Good", "Bad" or "Excellent"

It is explored with summary statistics (mean, median, mode), bar charts, line charts over time and vocabulary comparisons between documents.

**Encoding discrete features:**

- **One-hot encoding:** turns each category into a binary vector. Red, Blue and Green become three 0/1 columns. In pandas: `pd.get_dummies`.
- **Label encoding:** gives each category a unique integer, for example Blue → 0, Green → 1, Red → 2.
- **Ordinal encoding:** gives numbers that keep a natural order, for example Poor 0, Fair 1, Good 2, Excellent 3. Use it only when the order is real. Colours have no order.

## Text similarity

- **Lexical similarity** compares the exact words or characters used. "I love machine-learning" and "I love deep-learning" are highly similar. Its methods are token-based (Jaccard, cosine on bag-of-words) or string-based (Levenshtein edit distance, n-gram overlap).
- **Semantic similarity** compares meaning. "He bought a car" and "He purchased an automobile" are highly similar despite different words. It uses embeddings: Word2Vec and GloVe for words, BERT and Sentence-BERT for sentences.

Uses include removing duplicates, recommendation, plagiarism checking and search.

## Continuous data

Continuous data, such as height, weight, BMI, age, distance, price and temperature, is measured rather than counted. It is explored with line charts (trends), box-and-whisker plots (spread and outliers), heatmaps and scatter plots (relationships).

**Creating continuous features:**

- **Min-max normalisation:** x′ = (x − x_min) / (x_max − x_min) rescales values to [0, 1] without changing their relationships. Ages 18 to 40 map from 0 to 1, so 30 becomes about 0.55. It stops large-range features from dominating.
- **Log transformation:** x′ = ln(x) reduces skew and compresses large values, for example income from 1,000 (6.91) to 100,000 (11.51).
- **Ratios:** divide one feature by another, such as rent per room.
- **Rolling windows:** statistics over a sliding window smooth noise and show trends. A 3-day rolling mean of sales 10, 12, 15, 20 is 12.33, then 15.67, with NaN for the first two days.

## Feature selection

Feature selection reduces the inputs to the relevant ones and removes noise. It prevents learning from noise, improves accuracy and cuts training time.

- **Unsupervised** methods need no labels: PCA, ICA, non-negative matrix factorisation.
- **Supervised** methods use the target. They are filter, wrapper and embedded methods.

Source: Feature_Engineering_in_ML.pdf; My CSC 572 Note1.pdf
