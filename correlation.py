# -*- coding: utf-8 -*-

# @Time    : 2021/9/18 21:23
# @Author  : Zhongyu

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
import pandas as pd

data_path = '../../data/multi-index/data_precessed.csv'
data = pd.read_csv(data_path)
print(data)
# df.iloc[:, ]

# data = sns.load_dataset('iris')
# df = data.iloc[:, :4]  # 取前四列数据
# X = df['sepal_length']
# Y = df['petal_length']
# # result1 = np.corrcoef(X, Y)
# # result2 = np.corrcoef(df, rowvar=False)
# # result3 = ss.pearsonr(X, Y)
# # result4 = X.corr(Y)
# result5 = df.corr()

# print(result5)
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号
#
# figure, ax = plt.subplots(figsize=(12, 12))
# sns.heatmap(data.corr(), square=True, annot=True, ax=ax)
# plt.show()
