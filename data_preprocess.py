# -*- coding: utf-8 -*-

# @Time    : 2021/9/20 21:56
# @Author  : Zhongyu

import csv
import numpy as np

data_path = '../../data/multi-index/data_715.csv'
data = ([['性别', '年龄', '收缩压', '舒张压', '血氧饱和度', '血糖', '呼吸率', '心率', '心电图结论', 'PR间期', 'QRS间期',
          'QRS电轴', 'QT', 'QTc']])
with open(data_path, encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        if row[0] in ['483934', '480720']:
            continue
        gender = 1 if row[1] == '男' else 0
        age = int(row[2])
        s_pressure = float(row[3].split('/')[0])
        d_pressure = float(row[3].split('/')[1])
        oxygen = float(row[4])
        glucose = float(row[5])
        res_rate = float(row[6])
        heart_rate = float(row[7])
        ecg_result = 0 if '正常心电图' in row[8] else 1
        pr = int(row[9])
        qrs = int(row[10])
        qrs_axis = int(row[11])
        qt = int(row[12])
        qtc = int(row[13])
        new_row = [gender, age, s_pressure, d_pressure, oxygen, glucose, res_rate, heart_rate, ecg_result, pr, qrs,
                   qrs_axis, qt, qtc]
        data.append(new_row)

# print(data)
# print(len(data))

save_path = '../../data/multi-index/data_precessed.csv'
with open(save_path, 'w', encoding='utf-8', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(data)

