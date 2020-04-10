Graph theory network analysis of time-series fMRI data
Based on Scona (https://github.com/WhitakerLab/scona) & NetworkX (https://networkx.github.io/)

file setup:
1012/time_series is a folder than contains a series of text files (containing time-series data) extracted from a ROI based approach with functional fMRI data.
Each text file labelled by it's subsequent region e.g. thalamus.txt contains n values 

For each ROI script will output several relevant graph theory metrics nodally (betweeness/closeness/clustering/degree/module/participation coefficient & shortest path length),
and globally (average clustering/shortest path length/assortativity/modularity & efficiency). 

Output dataframes;
nodal_out
global_out

Amount of thresholding (H = G.threshold(#)) can impact data
name = df.columns.tolist() can be used easily to manually modify the number of ROI for the analysis

