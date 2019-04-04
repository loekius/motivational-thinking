# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:48:56 2019

@author: loekb
"""

#imports
import pandas as pd
import cbsodata as cbs
import define_data as dd






def barchart(pers_char,lifestyle):
    df = dd.df
#    df = df[df.Margins.str.contains('Value')]      #see define_data.py
    df = df[df.CharacteristicsPersons.str.contains(pers_char)]
    df = df[['CharacteristicsPersons','Periods',lifestyle]]
    df = df.set_index(['CharacteristicsPersons','Periods'])
    return df.unstack(level=0).plot.bar()





