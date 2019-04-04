#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:58:00 2019

@author: Lennart
"""
#imports
import pandas as pd
import cbsodata as cbs
import barchart as bc
#import numpy as np
#import matplotlib.pyplot as plt
#import plotly.offline as py

def def_variables():
    ls_input = input("""What lifestyle do you want to analyse?
                     1\tSmoking
                     2\tDrinking
                     3\tDrug use
                     4\tActivity""")
    if ls_input == "1":
        lifestyle = 'Smokers_1'
    if ls_input == "2":
        lifestyle = 'Drinkers_17'    
    if ls_input == "3":
        lifestyle = ('LastMonth_44','LastYear_45','Ever_46')
    if ls_input == "4":
        lifestyle = 'WeeklySporter_67'
    pc_input = input('What personal characteristics do you want to analyze')    
    if pc_input == "1":
        pers_char = "Wealth"

    
print(def_variables())

# run program in loop until user chooses to exit
while True:
    choice = input("""What do you want to do?
    1\tBar chart.
    2\tTrend analysis.
    3\tHeat map.
    4\tExit program.
    """)
    # evaluate user choice and proceed accordingly
    if choice == "1":
#        def_variables()
        bc.barchart("Wealth","Smokers_1")
    elif choice == "2":
        print("fuckyoupython")
    elif choice == "3":
        print("heatmap")
    elif choice == "4":
        print("Thank you for using this program.")
        break
    else:
        print("Choice not recognized. Try again.")   
