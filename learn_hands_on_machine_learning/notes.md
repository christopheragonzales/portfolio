# Notes

## Table of Contents
[End-to-End Machine Learning Project](#end-to-end-machine-learning-project)

## End-to-End Machine Learning Project
- Root Mean Square Error (RSME)
    - $RMSE(X, h) = \sqrt{\frac{1}{m} \sum_{i=1}^m (h(x^i) - y^i)^2}$ where:
        - *m* is the number of instances in the dataset you are measuring the RSME on.
        - $x^i$ is a vector of all feature values (excluding the label) of the *i<sup>th<sup>* instnace in the dataset and $y^i$ is its label(the desired output value for that instance).
        - **X** is a matrix containing all the feature values (excluding labels) of all instances in the dataset. There is one row per instance and the *i<sup>th<sup>* row is equal to the transpose of $x^i$, noted $(x^i)^T3$.
        - *h* is your system's prediction function, called a *hypothesis*. When your system is given an instance's feature vector $x^i$, it outputs a predicted value $\hat{y}^i = h(x^i)$ for that instance.
    - RSME is the generally preferred performance measure for regression tasks.
- Mean Absolute Error (MAE)
    - $MAE(X,h) = \frac{1}{m} \sum_{i=1}^m|h(x^i) - y^i|$
    - Used when there are many outliers
- 
