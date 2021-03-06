# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 09:45 2018
Team Rose & Jack 

"""

import l_utils as utils
import l_plot as plot
import pandas as pd
from sklearn import tree, model_selection

train = pd.read_csv('../data/titanic3_train.csv', sep=';')
test = pd.read_csv('../data/titanic3_test.csv', sep=';')

print("\nFirst look at the Data")
plot.ts_mapplot(dataset=train, grid_rv='sex', grid_cv='pclass', grid_hue='survived', map_v='age')
plot.ts_surv_prop(dataset=train, xv='age', yv='survived', colv='sex', huev='sex')

print ("\nCleaning up some data")

utils.clean_data(train)
utils.clean_data(test)

print ("\nExtracting target and features")

print(train.shape)
target = train["survived"].values
features = train[["pclass", "sex", "age", "fare"]].values

decision_tree = tree.DecisionTreeClassifier(random_state = 1)
decision_tree = decision_tree.fit(features, target)

print(decision_tree.feature_importances_)
print(decision_tree.score(features, target))

print ("\nTry on test set")

test_features = test[["pclass", "sex", "age", "fare"]].values
prediction = decision_tree.predict(test_features)
utils.write_prediction(prediction, "../submissions/decision_tree.csv")
# Resultat -> 0.7576923076923077

print ("\nCorrect overfitting")

feature_names = ["pclass", "age", "sex", "fare", "sibsp", "parch", "embarked"]
features_two = train[feature_names].values
decision_tree_two = tree.DecisionTreeClassifier(
    max_depth = 3,
    min_samples_split = 2,
    random_state = 1)
decision_tree_two = decision_tree_two.fit(features_two, target)

print(decision_tree_two.feature_importances_)
print(decision_tree_two.score(features_two, target))
tree.export_graphviz(decision_tree_two, feature_names=feature_names, out_file="decision_tree_two.dot", rounded = True, proportion = False, precision = 2, filled = True)

scores = model_selection.cross_val_score(decision_tree_two, features_two, target, scoring='accuracy', cv=10)
print (scores)
print (scores.mean())

print ("\nWrite new predicition")

test_features_two = test[["pclass", "age", "sex", "fare", "sibsp", "parch", "embarked"]].values
prediction_two = decision_tree_two.predict(test_features_two)
utils.write_prediction(prediction_two, "../submissions/Rose_and_Jack_pre.csv")
# Resultat ->  0.7961538461538461
