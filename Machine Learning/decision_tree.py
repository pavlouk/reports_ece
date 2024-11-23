# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

iris = datasets.load_iris()
print(iris.data)
print("Dataset shape: ", iris.data.shape,
      iris.target.shape)
clf = DecisionTreeClassifier()


scores = cross_val_score(clf, iris.data,
                         iris.target, cv=10)
print("Scores list: ", scores)
print("Accuracy: %0.2f (+/- %0.2f)"
      % (scores.mean(), scores.std() * 2))
