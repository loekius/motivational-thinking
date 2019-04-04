#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:16:33 2019

@author: Lennart
"""

import pandas as pd
import cbsodata as cbs
import define_data as dd

#try:
#    df_orig = pd.DataFrame(cbs.get_data('83021ENG'))
#except IOError:
#    print('file not found')
    
##info = cbs.get_info('83021ENG')
##print(info)
#
##the same dataset, to be modified
#df = df_orig
#df1 = df.set_index(['CharacteristicsPersons','Periods'])
##print(df1)
##removes all rows except when CharacteristicsPersons contains 'Wealth'
#df = df[df.CharacteristicsPersons.str.contains('Wealth')]
##selects value, leaves out 95...
#df = df[df.Margins.str.contains('Value')]
##removes all columns except the three needed--
#df = df[['CharacteristicsPersons','Periods','Smokers_1',]]
##----
##FROM HERE AVG CALCULATION
## sets the index
#df = df.set_index(['CharacteristicsPersons','Periods'])
#print(df)
#print(df.unstack())
#print(pd.DataFrame.mean(df[:,'2014']))
## selects one year
#df = df[0::4]
#print(df)
#df.plot.bar()
#print(pd.DataFrame.mean(df['Smokers_1']))
#df = main.df

def trendanalysis(pers_char,lifestyle):
    df = dd.df
    df = df[df.CharacteristicsPersons.str.contains(pers_char)]
    df = df[df.Margins.str.contains('Value')]
    df = df[['CharacteristicsPersons','Periods',lifestyle]]
    df = df.set_index(['CharacteristicsPersons','Periods'])
    df.unstack(level=0).plot(kind='line', subplots=False)
    
#pers_char = input('What personal characteristics do you want to look at?')
#lifestyle = input('What lifestyle do you want to look at?')
#graphstyle = input('Visualization?')
#if lifestyle == 'smoking':
#    lifestyle = 'Smokers_1'
#if lifestyle == 'drinking':
#    lifestyle = 'Drinkers_17'

#df_test = main.df
#df_test = df_test[df_test.CharacteristicsPersons.str.contains('Wealth')]
#df_test = df_test[df_test.Margins.str.contains('Value')]
#df_test = df_test[['CharacteristicsPersons','Periods','Smokers_1']]
#df_test = df_test.set_index(['CharacteristicsPersons','Periods'])

    

#print(trendanalysis(pers_char,lifestyle,graphstyle))