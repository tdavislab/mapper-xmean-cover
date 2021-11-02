# Mapper X-Means Adaptive Cover
By [Nithin Chalapathi](https://ieeexplore.ieee.org/author/37088395878) [Youjia Zhou](https://www.sci.utah.edu/people/zhou325.html), and [Bei Wang](http://www.sci.utah.edu/~beiwang/).

## Overview
Abstract:

> The mapper construction is a widely used tool from topological data analysis in obtaining topological summaries of large, high-dimensional point cloud data. It has enjoyed great success in data science, including cancer research, sports analytics, and visualization. However, developing practical and automatic parameter selection for the mapper construction remains a challenging open problem for both the topological analysis and visualization communities. In this paper, we focus on parameter selection for the 1-dimensional skeleton of the mapper construction, called the mapper graph. Specifically, we explore how information criteria used in the X-means clustering algorithm can inform and generate adaptive covers for mapper graphs. Our approach thus makes novel progress towards automatic parameter selection for the mapper construction using information theory.

This repository contains all of the code for the above paper. It also contains an implementation of the enhanced mapper graph by [Brown, Bobrowski, Munch and Wang](https://arxiv.org/abs/1909.03488). 

## Installation

Requirements:

```
python>=3.6
matplotlib
networkx
numpy
pyvis
scikit_learn
imageio
```

The recommended installation is via pip which handles dependencies for you. The package is currently not published and must be installed locally:

```bash
$ git clone https://github.com/tdavislab/mapper-xmean-cover/
$ cd mapper-xmean-cover
$ pip install .
```

If you would like to edit the repository locally, please use `pip install -e .` to see the changes reflected in your pip installation. The instructions are no different when using conda. 

## Usage

The main method to run the xmean adaptive cover is `xmeans_adaptive_cover()`. It returns a cover object which can be passed to `generate_mapper_graph()`. Here is an example:

```
from mapper_xmean_cover import Cover, generate_mapper_graph, xmeans_adaptive_cover
from sklearn.cluster import DBSCAN

X # np array of the point cloud (n pts x d dimensions)
lens # np array containing the lens (n pts)

# First, generate an initalization cover
initial_cover = Cover(num_intervals=5, percent_overlap=0.2)

# Now run xmean adaptive cover
adaptive_cover = xmeans_adaptive_cover(X, lens=lens,
																			 clusterer=DBSCAN(eps=2), # Sklearn Cluster obj 
																			 iterations=100, # Maximum num of iterations
																			 max_intervals=100, # Max num of intervals
																			 BIC=True, # False uses AIC
																			 # Percentage change to determine convergence
																			 delta=0.01,
																			 # One of BFS, DFS, or Randomized
																			 method='BFS')
final_graph = generate_mapper_graph(X, lens, cover=adaptive_cover, clusterer=DBSCAN(eps=2),
																	  refit_cover=False) # VERY IMPORTANT - See note
```

Here are some important notes:

* `refit_cover` passed to `generate_mapper_graph` MUST be set to False. Otherwise, the cover will be converted to a normal uniform cover.
* The default parameters are set as:
  * `iterations=10`
  * `max_intervals=10`
  * `BIC=True`
  * `delta=0.`
  * `method='BFS'`

## Issues and Feedback?

For installation troubles and bugs, please open a github issue.

For feedback or more in-depth discussions, please email one of the authors.