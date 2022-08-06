#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import dependencies 
import pandas as pd 
import requests 
import json
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn import preprocessing
from sklearn.metrics import precision_score, recall_score
import numpy as np
from tqdm.notebook import tqdm
import sys
from location_grabber import grab_location
from model import prepare_data, model, metrics




# read data 
def read_data(filename):
    data = pd.read_csv(filename)
    return data

def grab_unique_dst_ip(data):
    unique_df = pd.DataFrame(data['Dst IP'].unique())
    return unique_df

def merger(data, results_df):
    # merge location data df with the original dataset
    data = pd.merge(data, results_df, how= "outer", left_on = "Dst IP", right_on = "IPv4")
    return data
    


def main():
    data = read_data(sys.argv[1])
    unique_df = grab_unique_dst_ip(data)
    results = grab_location(unique_df)
    # turn list into dataframe
    results_df = pd.DataFrame(results)
    # save to a csv
    results_df.to_csv("results.csv")
    # turn list into dataframe
    results_df = pd.DataFrame(results)
    # save to a csv
    results_df.to_csv("results.csv")
    data = merger(data, results_df)
    # select only the columns we want in a new data frame
    df = data[["country_name", "Flow Duration", "Flow IAT Min", "Src Port", "Tot Fwd Pkts", "Init Bwd Win Byts", "Label"]]
    df.to_csv("final_merged.csv")
    df = df.dropna()
    D_train, D_test, y_test = prepare_data(df)
    model_1 = model(D_train)
    metrics(D_test, y_test, model_1)
    
    
if __name__ == "__main__":
    main()


