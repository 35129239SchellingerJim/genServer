import os

from sklearn.datasets import make_classification
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#from sklearn import preprocessing
from sklearn.neighbors import KernelDensity
from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import StandardScaler
#from sklearn.mixture import GaussianMixture

from datetime import datetime
from serverTests.data import ExpSet,PFit


d=32*32
n_samples=2000
n_features=d
n_informative=int(0.3*d)
n_redundant=int(0.2*d)
n_repeated=int(0.2*d)
n_classes=int(60)
n_clusters_per_class=1
class_sep=7
desc="test"

X, y = make_classification(n_samples=n_samples,
                           random_state=0,
                           n_features=n_features,
                           n_informative=n_informative,
                           n_redundant=n_redundant,
                           n_repeated=n_repeated,
                           n_classes=n_classes,
                           n_clusters_per_class=n_clusters_per_class,
                           class_sep=class_sep)

# Pipeline
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import cross_val_score
time_start = datetime.now()

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    random_state=0,
                                                    test_size=0.2)

#pipe = make_pipeline(GaussianMixture(n_components=n_classes, random_state=0,max_iter=1000))  # standardisiere daten
pipe = make_pipeline( KernelDensity(kernel='gaussian', bandwidth=0.5))  # standardisiere daten
pipe.fit(X_train)

p_scores = pipe.score(X_test, y_test)  # apply scaling on testing data, without leaking training data
# Evaluate the models using crossvalidation
# scores = cross_val_score(pipe, X_test, y_test,
#                         scoring="accuracy", cv=5)
# scores=accuracy_score(y_train, pipe.predict(X_train))

# print("%0.2f balanced_accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
print(p_scores)

time_to_fit1=round(((datetime.now()-time_start).total_seconds()),2)
print("Time to fit "+str(time_to_fit1))


exp=ExpSet.load(os.getcwd()+"/results")
exp.addPFit(PFit({'n_samples':n_samples,
                 'n_features':n_features,
               'n_informative':n_informative,
               'n_redundant':n_redundant,
               'n_repeated':n_repeated,
               'n_classes':n_classes,
               'n_clusters_per_class':n_clusters_per_class,
                  'time':time_to_fit1,
                  'score':p_scores,
                  'desc':desc,
                  'class_sep':class_sep,
                  }))
