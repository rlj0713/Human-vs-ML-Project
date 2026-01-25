**Team Members:**  
- Mr J

**Dataset Used:**
Iris Classification Dataset

**Source:**  
[UCI Iris Data](https://archive.ics.uci.edu/dataset/53/iris)</br>
[Import ReadMe for Data](https://github.com/uci-ml-repo/ucimlrepo)

**Target Variable (What we are predicting):**  
Predicted Attribute: Class of Iris Plant
 - Setosa, Versicolour, or Virginica

**Features Considered:**  
- Sepal Length
- Petal Length
- Sepal Width
- Petal Width

**[Video Review](https://youtu.be/dQw4w9WgXcQ)**

## Getting Started

<img src="getting_started/plots/sepal_length_v_petal_length.png" alt="X vs Y – Iris Dataset" width="300">
<img src="getting_started/plots/sepal_width_v_petal_length.png" alt="X vs Y – Iris Dataset" width="300">
<img src="getting_started/plots/sepal_width_v_petal_width.png" alt="X vs Y – Iris Dataset" width="300">


## Human Algorithm

### Pseudo-Code
```text
The clearest difference is iris classification is visible when sepal width is compared to petal width, so the human-algorithm is:

    IF petal_width < 0.6:
        Predict Setosa
    ELSE IF petal_width < 1.6:
        Predict Versicolor
    ELSE:
        Predict Virginica

```

When examining the data and visualizations, we focused on petal width only, because it appears that this measurement has the most distinction between species.

The plots/tables suggested a possible threshold for petal width, and we considered values above or below 0.6 and 1.6 to see how they might relate to species.

From the summary tables and visualizations, it appeared that sepal width could influence classification, which led us to using this factor in our decision rules.

### Confusion Matrix

Accuracy: ?

| Actual \ Predicted | Class 1 | Class 2 | Class 3 |
|-------------------|---------|---------|---------|
| **Class 1**       |         |         |         |
| **Class 2**       |         |         |         |
| **Class 3**       |         |         |         |

One example where our algorithm worked well is when the inputs were ___, leading to a correct prediction of ___ because ___.

An example where the algorithm did not perform as expected is when the inputs were ___, resulting in a prediction of ___ instead of ___, which may have happened because ___.

These examples of success and failure highlight patterns in the data or limitations in our rules, such as ___.

<img width="315" height="334" alt="image" src="https://github.com/user-attachments/assets/23ee1e49-da76-47c2-97b8-c8fbcbef179c" />

## Machine Learning Model

We chose a value of k = ___ after comparing model performance across different values of k and observing that ___.

When analyzing the outputs and metrics, we noticed that changing k affected ___, which influenced our final choice.

Based on the results shown in the tables or visualizations, k = ___ best matched our goals for model performance because ___.

### Confusion Matrix

Accuracy: ?

| Actual \ Predicted | Class 1 | Class 2 | Class 3 |
|-------------------|---------|---------|---------|
| **Class 1**       |         |         |         |
| **Class 2**       |         |         |         |
| **Class 3**       |         |         |         |

The table/visualization shows a clear pattern where the model predicts ___ when ___, indicating a strong relationship between these features.

The confusion matrix reveals that the model most often confuses ___ with ___, suggesting these classes have similar feature values.

Compared to the human algorithm, the KNN model shows different behavior when ___, as seen in the ___ visualization.

<img width="315" height="334" alt="image" src="https://github.com/user-attachments/assets/199ae59d-3470-40c6-9669-60e62b211619" />
