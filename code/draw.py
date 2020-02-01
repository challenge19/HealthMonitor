# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:48:26 2020

@author: zhesi
"""

import pandas as pd
import matplotlib.pyplot as plt


data_file = '../data/health.xlsx'
figure_dir = '../figure/'

df = pd.read_excel(data_file)
df['date'] = pd.to_datetime(df['Date'])
# 绘制体温

fig = plt.figure(figsize=(4,3))
ax = plt.subplot(111)

ax.plot(df['date'],df['Temp'],'o-',label='Temp')
ax
ax.set_ylim(35,40)
ax.
plt.savefig(f'{figure_dir}/temp.png',dpi=200)