#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:56:25 2018

@author: pamela
"""
import pandas as pd

data_file = 'data/redcard.csv'
full_data = pd.read_csv(data_file)
full_data.head()
full_data.columns

#Start with some data cleaning
#check- is each row a unique player?
len(full_data['playerShort'].unique()) == len(full_data['playerShort'])
len(full_data['playerShort'])
#each player is in here many times