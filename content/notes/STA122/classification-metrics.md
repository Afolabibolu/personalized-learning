# Classification Metrics

## The confusion matrix

A **confusion matrix** compares predicted and actual classes:

| | Predicted positive | Predicted negative |
| --- | --- | --- |
| Actual positive | **TP** (true positive) | **FN** (false negative) |
| Actual negative | **FP** (false positive) | **TN** (true negative) |

Every metric comes from these four counts.

## The metrics

- **TPR, recall or sensitivity** = TP/(TP + FN): the share of actual positives found. 80 of 100 gives 0.8.
- **TNR or specificity** = TN/(TN + FP): the share of actual negatives found. 90 of 100 gives 0.9.
- **FPR** = FP/(FP + TN) = 1 − TNR: the false alarms. 10 of 100 gives 0.1.
- **FNR** = FN/(FN + TP) = 1 − TPR: the missed positives. 20 of 100 gives 0.2.
- **PPV or precision** = TP/(TP + FP): the share of positive predictions that are right. 40 of 50 gives 0.8.
- **NPV** = TN/(TN + FN): the share of negative predictions that are right. 55 of 60 gives about 0.92.
- **Accuracy** = (TP + TN)/(TP + TN + FP + FN). For TP = 40, TN = 50, FP = 10 and FN = 10, it is 90/110 ≈ **0.818**.
- **F1** = 2 × precision × recall/(precision + recall), the **harmonic mean** of precision and recall. Precision = recall = 0.8 gives F1 = 0.8.

## Practical example

Take 1000 patients (100 sick, 900 healthy), with TP = 80, FN = 20, FP = 50 and TN = 850.

- Recall = 0.80, specificity = 850/900 ≈ 0.944, FPR ≈ 0.056 and FNR = 0.20.
- Precision = 80/130 ≈ **0.615** and NPV = 850/870 ≈ 0.977.
- Accuracy = 930/1000 = **0.93**, and F1 = 2(0.615)(0.8)/1.415 ≈ **0.696**.

Accuracy looks high, but more than a third of the positive predictions are wrong. This is why accuracy can mislead on **imbalanced** data.

## Which metric?

| Metric | Priority | Use case |
| --- | --- | --- |
| Recall | minimise false negatives | medical diagnosis, safety checks |
| Precision | minimise false positives | spam filtering, legal decisions |
| F1 | balance both | imbalanced data (fraud, defects) |
| Accuracy | overall correctness | balanced classes (cats and dogs) |

Match the metric to the cost of each kind of error in the problem.

Source: STA 122 Module 4: Classification Metrics in Machine Learning (Akintande)
