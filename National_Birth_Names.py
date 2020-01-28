# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:53:25 2020

@author: jmiller
"""

import numpy as np
import pandas as pd
import os

# Empty df
df_m = pd.DataFrame()
df_f = pd.DataFrame()

# Load all names into dataframes
for file in os.listdir('data'):
    year = file[3:7]
    temp_df = pd.read_csv('data/' + file,
                          header = None,
                          names = ['Name', 'Sex', 'Count'])
    m_names = temp_df[temp_df['Sex'] == 'M']\
                     [['Name', 'Count']].set_index('Name').T
    f_names = temp_df[temp_df['Sex'] == 'F']\
                     [['Name', 'Count']].set_index('Name').T
    df_m = df_m.append(pd.Series(m_names.to_dict('records')[0], name = year))
    df_f = df_f.append(pd.Series(f_names.to_dict('records')[0], name = year))

# Sort index for plotting
df_m = df_m.sort_index()
df_f = df_f.sort_index()