# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:20:14 2019

@author: loekb
"""
import pandas as pd
import cbsodata as cbs

# Tries to read 'data.csv', and if it doesnt exist, it creates the file
try:
    pd.read_csv('data.csv')
except IOError:
    pd.DataFrame(cbs.get_data('83021ENG')).to_csv('data.csv')
df_orig = pd.read_csv('data.csv').drop('Unnamed: 0', 1)


##### when testing, use this to get a list of column names plus their numbers
#cols = df_orig.columns.values
#for i, item in enumerate(cols,0):
#    print(i, '. ' + item, sep='',end='\n')


def select_columns(selection):
    useful_cols = ['CharacteristicsPersons', 'Periods', 'Margins'] + selection
    df_useful = df_orig[useful_cols]
    for i in df_useful.index:                ## comment/uncomment these lines to
        if df_useful.Margins[i] != 'Value':  ## include/exclude 95% conf interval
            df_useful = df_useful.drop(i)    ## upper and lower bounds,
    df_useful = df_useful.drop('Margins', 1) ## and the 'Margins' column itself
    return df_useful

                                            ## Metadata descriptions ##
selection1 = ['Drinkers_17',                # The percentage of persons in the population aged 12 years or older that answered Yes to the question: Did you ever drink an alcoholic beverage during the last 12 months, such as beer, wine, liqueur, gin or mixed drinks containing alcohol, such as breezers? Beer without alcohol or containing only little alcohol does not count.
              'Smokers_1',                  # The percentage of persons in the population aged 12 years or older who answered Yes to the question: Do you ever smoke?
              'NormalWeight_50',            # The percentage of persons whose BMI value is between 18,5 and 25,0 kg/m2 .
              'LastMonth_44',               # Drug use todo
              'LastYear_45',                # Drug use todo
              'Ever_46',                    # Drug use todo
              'WeeklySporter_67']           # The percentage of persons of 12 years or older who practise sport at least once a week. From 2017 onwards, the percentage of weekly sporters aged 4 years and older is published. The percentage of weekly sporters aged 12 and older is published for the last time in 2017.
df = select_columns(selection1)



