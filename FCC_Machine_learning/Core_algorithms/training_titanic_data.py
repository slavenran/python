from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
# from six.moves import urllib

# import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

# Load dataset
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

print(dftrain.head())   # gives back 5 rows of data for checking of the right data is in data frame

print(dftrain.describe())   # gives back overall information (values like mean, min and max for some columns)

print(dftrain.shape)    # data frame also has a shape like tensors

print(dftrain.age.hist(bins=20))   # makes (draws) a histogram of age column, bins are like containers for all the data (more bins==more precision)

print(y_train.hist())   # has only one column so it doesn't need to be specified (or rather it can't be)

print(dftrain.sex.value_counts().plot(kind='barh'))    # makes a custom histogram that nicely visualises binary values

print(dftrain['class'].value_counts().plot(kind='barh'))    # another way to pull a column from a data frame, similar to JS

# Stopped copypasting here, everything is contained instide ipynt files