#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:56:25 2018

@author: pamela
"""
import pandas as pd
import numpy as np
from scipy import stats
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
#average these to create one skintone rating? light <0.5, dark >0.5?

#check for NAs
sum(pd.isnull(full_data).any(axis=1))
#30,571 rows have a NA, that's quite a bit of data, so we shouldn't throw it out probably

skin_avg = (full_data['rater1'] + full_data['rater2'])/2
full_data['skin_avg'] =skin_avg
plt.hist(skin_avg[~np.isnan(skin_avg)])

#goal: model if dark players get more red cards; 
#need to account for other variables and repeated measurements
#modeling ideas: some sort of hierarchical/multielvel model, where the random effect is on the individual player
#count total # red cards per player- does this differ between light and dark players?
# this is essentially an A/B test- which won't account for other factors
#   repeated measures two-way ANOVA?

#to start: I don't think an A/B test is particularly valid, since the groups aren't controlled,
# but it will give us some sense of what is going on in the data, so is probably useful to quickly run

#count red cards per player
by_player = pd.DataFrame()
by_player['red_counts'] = full_data['redCards'].groupby(full_data['playerShort']).count()
by_player['skin_avg'] =  full_data['skin_avg'].groupby(full_data['playerShort']).mean()
by_player.head()

light = by_player[by_player['skin_avg'] <=0.5]
dark = by_player[by_player['skin_avg'] > 0.5]
stats.ttest_ind(light, dark)
#notes- data is very imbalanced

#other notes: the last several columns have to do with implicit bias tests from the countries that ref is from
#probably very useful, but didn't get to dig into it
