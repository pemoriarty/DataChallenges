#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:56:25 2018

@author: pamela
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file = 'data/redcard.csv'
full_data = pd.read_csv(data_file)
full_data.head()
full_data.columns

#Start with some data cleaning
#check- is each row a unique player?
len(full_data['playerShort'].unique()) == len(full_data['playerShort'])
len(full_data['playerShort'])
#each player is in here many times- 2053 playes with 143K+ observations
#porbably need some sort of hierarchical/multielvel model

full_data[full_data['playerShort']=='lucas-wilchez']
full_data['rater1'].unique()
full_data['rater2'].unique()
#skin tone is 0, 0.25, 0.5, 0.75, 1- rated by two different people
#average these to create one skintone rating?

#check for NAs
sum(pd.isnull(full_data).any(axis=1))
#30,571 rows have a NA, that's quite a bit of data, so we shouldn't throw it out probably

skin_avg = (full_data['rater1'] + full_data['rater2'])/2
plt.hist(skin_avg[~np.isnan(skin_avg)])
