#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np

# splitting into train, test, x, & y
def prepare_data(df):
    df = pd.get_dummies(df, columns = ["country_name"]) 
    # establish x values (everything except Label)
    X = df.loc[:, df.columns != 'Label']
    # make label numerical and int
    df["Label"] = df["Label"].replace(['Benign','ddos'],[0,1])

    y = df["Label"]
    
    # create split (0.25)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    
    # transform into DMatrix 
    D_train = xgb.DMatrix(X_train, label=y_train)
    D_test = xgb.DMatrix(X_test, label=y_test)
    
    return D_train, D_test, y_test

def model(D_train):
    # set parameters
    param = {
        'eta': 0.3, 
        'max_depth': 3,  
        'objective': 'multi:softprob',  
        'num_class': 3} 
    
    # The number of training iterations
    steps = 20  
    
    # create and fit model
    model_1 = xgb.train(param, D_train, steps)
    
    # plot importance of predictors
    xgb.plot_importance(model_1)
    # adjust figure size
    # show plot
    plt.show()
    return model_1
    
def metrics(D_test, y_test, model_1):
    preds = model_1.predict(D_test)
    best_preds = np.asarray([np.argmax(line) for line in preds])

    print("Precision = {}".format(precision_score(y_test, best_preds, average='macro')))
    print("Recall = {}".format(recall_score(y_test, best_preds, average='macro')))
    print("Accuracy = {}".format(accuracy_score(y_test, best_preds)))

def cross_val(D_train):
    params = {"objective":"multi:softprob",'colsample_bytree': 0.3,'learning_rate': 0.1,
                'max_depth': 5, 'alpha': 10}

    cv_results = xgb.cv(dtrain=D_train, params=params, nfold=5, num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)

    print((cv_results["test-rmse-mean"]).tail(1))
