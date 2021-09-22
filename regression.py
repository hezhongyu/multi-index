# -*- coding: utf-8 -*-

# @Time    : 2021/9/22 6:22
# @Author  : Zhongyu

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data_path = '../../data/multi-index/data_precessed.csv'
data = pd.read_csv(data_path)
print(data)
# df.iloc[:, ]


