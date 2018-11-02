#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:30:16 2018

@author: isabellekluser
"""


import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

def clean_boats(dataset):
    data = dataset[:]
    data["boat"] = data["boat"].fillna(0)
    data.loc[data["boat"] != 0 , "boat"] = 1
    return data

def ts_mapplot(dataset, grid_rv, grid_cv, grid_hue, map_v):
    #set style for Plots
    sns.set(style="darkgrid")
    
    dataset = clean_boats(dataset)
    
    #generate grid 
    g = sns.FacetGrid(dataset, row=grid_rv, col=grid_cv, hue=grid_hue, margin_titles=True)
    #print grid
    g.map(plt.hist, map_v, alpha=0.5)
    
    plt.show()


def ts_surv_prop(dataset, xv, yv, colv, huev):
    #set style for Plots
    sns.set(style="darkgrid")

    # Make a custom palette with gendered colors
    pal = dict(male="#6495ED", female="#F08080")
    
    # Show the survival proability as a function of age and sex
    g = sns.lmplot(x=xv, y=yv, col=colv, hue=huev, data=dataset,
                   palette=pal, y_jitter=.02, logistic=True)
    g.set(xlim=(0, 80), ylim=(-.05, 1.05))    
    
    plt.show()
    