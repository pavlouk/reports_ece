# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.naive_bayes import GaussianNB

TRAIN_FEATURES = [[0, 0], [0, 1], [1, 0], [1, 1]]
TEST_LABELS = [0, 1, 1, 1]

clf = GaussianNB()
clf.fit(TRAIN_FEATURES, TEST_LABELS)

TEST_FEATURES = [[0, 0], [0, 1]]
PREDICTIONS = clf.predict(TEST_FEATURES)
print("Predictions: ", PREDICTIONS)

from sklearn.metrics import accuracy_score

TEST_LABELS = [0, 1] #this leads to 100% accuracy
            #[1, 1] leads to 50% accuracy
score = accuracy_score(TEST_LABELS, PREDICTIONS)
print("Accuracy: ", score * 100, "%")