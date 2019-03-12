import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.tree import DecisionTreeRegressor
# from sklearn.datasets import load_boston
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.utils import check_random_state
from IPython.display import display # To display entire dataset

from titanic_visualizations import survival_stats

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

print( np.zeros(5) )
#adding a temp change