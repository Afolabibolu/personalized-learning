# Generalization and Model Evaluation

## Bias, variance and the trade-off

**Generalization** is a model's ability to predict well on new, unseen data.

- **High bias (underfitting):** the model is too simple and makes strong assumptions, such as a straight line for curved data. Accuracy is low on both training and test data. Train 60% and test 55% means underfitting.
- **High variance (overfitting):** the model is too complex and learns the noise. Accuracy is very high on training data and poor on test data. Train 98% and test 62% means overfitting. Train 92% and test 90% is a good fit.

As complexity grows, bias falls and variance rises. Total error = bias² + variance + irreducible error, and the best model sits at the bottom of the U-shaped total-error curve.

**Fixing underfitting:** add features, reduce regularization, use a more complex model, train longer. **Fixing overfitting:** get more data, remove irrelevant features, add **regularization** (which penalises complexity), use **dropout** in neural networks, reduce complexity, use **early stopping** and cross-validation.

## Splitting the data

- The **training set** teaches the model.
- The **validation (dev) set** tunes hyperparameters such as the learning rate or tree depth.
- The **test set** is used once, at the end, for an unbiased estimate.

Common splits are 70/15/15 or 80/10/10.

**k-fold cross-validation** suits small datasets. Split the data into k folds, often 5 or 10. Train on k − 1 folds and validate on the remaining one. Repeat until every fold has been the validation fold, then average the results. **Stratified** cross-validation keeps the class proportions in every fold, which matters for imbalanced data such as 97% legitimate and 3% fraud. Lesson 9 compares algorithms with 10-fold cross-validation and a fixed random seed.

## Classification metrics

A **confusion matrix** counts true positives (TP), true negatives (TN), false positives (FP, false alarms) and false negatives (FN, dangerous misses).

- **Accuracy** = (TP + TN) / total. It misleads on imbalanced data.
- **Precision** = TP / (TP + FP). Use it when false alarms are costly, as in spam filtering or recommendations.
- **Recall (sensitivity)** = TP / (TP + FN). Use it when misses are dangerous, as in cancer or fraud detection.
- **F1** is the harmonic mean of precision and recall, useful for imbalanced classes. **Specificity** is TN / (TN + FP).
- The **ROC curve and AUC** score separability: 0.5 is guessing and 1.0 is perfect. The **precision-recall curve** is better for rare positives.

**Example.** TP 80, TN 40, FN 20 and FP 10 give accuracy 0.80, precision 0.89, recall 0.80 and F1 0.845.

## Regression metrics

- **MAE:** the average absolute error.
- **MSE:** squares errors, so big mistakes weigh heavily.
- **RMSE:** the square root of MSE, back in the original units.
- **R²:** the share of variance explained. 1 is perfect, 0 is as good as predicting the average, and a negative value is worse than that.

Source: My CSC 572 Note1.pdf; Lesson 9 - Algorithm Comparison.pdf; ML Overview Slide_2025.pptx
