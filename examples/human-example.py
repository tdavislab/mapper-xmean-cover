import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN
import matplotlib


# Library functions
from mapper_xmean_cover import Cover, generate_mapper_graph, xmeans_adaptive_cover, vis_graph

# Visualization
from pyvis.network import Network
from matplotlib import cm
from matplotlib.colors import rgb2hex
import pickle as pkl
import imageio
from os import listdir
from os.path import join

# First, load the data and generate the lens
X = np.loadtxt('human.txt')
lens = X[:, -1]
lens = MinMaxScaler().fit_transform(lens.reshape(-1, 1))

# Parameter setup
initial_intervals = 2
overlap = 0.4
initial_cover = Cover(num_intervals=initial_intervals, percent_overlap=overlap, enhanced=False)
eps = 0.1
clusterer = DBSCAN(eps=eps)
labels = None
delta = 0
BIC=True
save_loc = './horse-example/'

# Generating adaptive cover
adaptive_cover = xmeans_adaptive_cover(X, lens, initial_cover, clusterer=clusterer, iterations=100, max_intervals=40, BIC=BIC, delta=delta, method='BFS')

# Now use the new cover
graph = generate_mapper_graph(X, lens, cover=adaptive_cover, clusterer=clusterer, refit_cover=False)

# Save visualization
vis_graph(graph, title='Horse Example', lens=lens, save_loc=save_loc)