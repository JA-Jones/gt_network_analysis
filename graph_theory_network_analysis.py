# script for the graph theory network analysis of FMRI data
# import what you need
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import scipy
import scipy.stats as stats
import seaborn as sns
import pingouin as pg
import os
import networkx as nx
import scona as scn
import scona.datasets as datasets
from scona.scripts.visualisation_commands import view_corr_mat

# create holder for list of folder path length (os.walk also available)
holder=[]
folders = [r'C:\Users\1012\time_series',           
           r'C:\Users\1013\time_series',       
          ]

# loop for the import of time-series data for each ROI for each subject
for i in folders:
    li=[]
    df = pd.DataFrame()
    #root = r'C:\Users\JAJ58\Desktop\roi_ffd\'
    os.chdir(i)
    li = os.listdir()
    print(os.getcwd())
    df = pd.concat([pd.read_csv(item, names=[item[:-4]]) for item in li], axis=1)
    holder.append(df)
    
# create list of ROI names (see below for changing # of ROI - refined analysis)
name = df.columns.tolist()
# delete the regions you *want to keep* and save list
# this will then get rid of the columns in the list leaving you with a 
# reduced dataframe with your specific ROI
#for i in holder:
    #i.drop(list,axis=1, inplace=True)

# following code based off scona/networkX (see README for details)
nh = []
gh = []
for i in holder:
    M = scn.create_corrmat(i, method='pearson')
    G = scn.BrainNetwork(network=M, parcellation=name)
    H = G.threshold(10) #10% threshold
    H.calculate_nodal_measures()
    nodal = H.report_nodal_measures()
    nodal = nodal.T
    glob = H.calculate_global_measures()
    glob = pd.DataFrame.from_dict(glob, orient='index')
    glob = glob.T
    nh.append(nodal)
    gh.append(glob.copy())

# reformatting output for nodal measures per each ROI for each subject
df = pd.concat(nh)
header = df.iloc[0]
nodal_out = df.rename(columns = header)
nodal_out.drop(['name'], inplace=True)
nodal_out.sort_index(inplace=True)

# output of global measures for each subject
global_out = pd.concat(gh, axis=0)



   
