from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class NB(BaseEstimator, ClassifierMixin):
    
    def __init__(self):
        self.num_classes = None
        self.classes = {}
        self.prior = []
        self.condprob = []
        
    def fit(self, X, y):
        # Compute number of docs
        N = len(y)
        # Compute classes
        self.classes = set(y)        
        lapl = sum([ sum(x) for x in zip(*X) ]) + X.shape[0]
        
        for c in self.classes:
            # Take only wordcounts of data with class c
            useful_data = [ X[idx, :] for idx, val in enumerate(y) if val == c ]
            # Compute prior probability
            Nc = len(useful_data)
            self.prior.append(Nc/N)
            # Compute conditional probability
            self.condprob.append([ (sum(x)+1)/lapl for x in zip(*useful_data)])
        return self
    
    def predict(self, X):
        res = []
        for x in X:
            class_score = []
            for c in self.classes:
                class_score.append(np.log(self.prior[c]))
                class_score[-1] += sum( [ np.log(x) for x in self.condprob[c] ] )
            res.append(np.argmax(class_score))
        return res

    def score(self, X, y):
        return np.mean(self.predict(X) == y)