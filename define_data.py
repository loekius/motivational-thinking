# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:20:14 2019

@author: loekb
"""
import pandas as pd
import cbsodata as cbs


try:
    pd.read_csv('data.csv')
except IOError:
    pd.DataFrame(cbs.get_data('83021ENG')).to_csv('data.csv')
df_orig = pd.read_csv('data.csv').drop('Unnamed: 0', 1)
#
#cols = df_orig.columns.values
#for i, item in enumerate(cols,0):
#    print(i, '. ' + item, sep='',end='\n')

cols = df_orig.columns.values
useful_cols = []
def selection1(useful_cols):
    for i in [5, 91, 19, 103, 87, 57, 64, 26, 117, 66]: #57, 64, 26: drug use, 66 is margins 
        useful_cols += [cols[i]]
    df = df_orig[useful_cols]
    return df

df = selection1(useful_cols)
print(df)


