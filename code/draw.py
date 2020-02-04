# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:48:26 2020

@author: zhesi
"""

import pandas as pd
import matplotlib.pyplot as plt


data_file = '../data/health.xlsx'
figure_dir = '../figure/'

df = pd.read_excel(data_file,sheet_name='temp')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
# 绘制体温
fig = plt.figure(figsize=(4,2.5))
ax = plt.subplot(111)

#ax.plot(df['date'],df['Temp'],'o-',label='Temp')
df.plot(ls='-',marker='o',ax=ax)
ax.set_ylim(35,40)
ax.axhline(y=37.3,color='k',ls='--')

ax.set_xlabel('Date',fontsize=13)
ax.set_ylabel('Temp',fontsize=13)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig(f'{figure_dir}/temp.png',dpi=150)

# 绘制体重
df = pd.read_excel(data_file,sheet_name='weight')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

fig = plt.figure(figsize=(4,2.5))
ax = plt.subplot(111)

#ax.plot(df['date'],df['Temp'],'o-',label='Temp')
df.plot(ls='-',marker='o',ax=ax)
ax.set_ylim(120,160)
ax.axhline(y=140,color='k',ls='--')

ax.set_xlabel('Date',fontsize=13)
ax.set_ylabel('Weight',fontsize=13)
ax.legend(loc='lower left')
plt.tight_layout()
plt.savefig(f'{figure_dir}/weight.png',dpi=150)