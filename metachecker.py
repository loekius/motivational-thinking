# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:45:06 2019

@author: Buf
"""
import cbsodata as cbs
import pandas as pd

try:
    pd.read_csv('data.csv')
except IOError:
    pd.DataFrame(cbs.get_data('83021ENG')).to_csv('data.csv')
df_orig = pd.read_csv('data.csv').drop('Unnamed: 0', 1)

try:
    pd.read_csv('metadata.csv')
except IOError:
    pd.DataFrame(cbs.get_meta('83021ENG', 'DataProperties', catalog_url=None)).to_csv('metadata.csv')
metadata = pd.read_csv('metadata.csv')[['Key', 'Title', 'Description']].set_index('Key')

selection1 = ['Drinkers_17',
              'Smokers_1',
              'NormalWeight_50',
              'LastMonth_44',               # Drug use
              'LastYear_45',                # Drug use
              'Ever_46',                    # Drug use
              'WeeklySporter_67'] 

for key in selection1:
    print(f'{key}\t{metadata.Title[key]}\t{metadata.Description[key]}')
    
    