import numpy as np
import pandas as pd

class Model:
    def fit(self, X, Y):
        return self


    def predict(self, X):
        pred = pd.DataFrame()
        pred['evtID'] = X['evtID']
        keys = ['E', 'R']
        for col in keys:
            pred[col] = np.random.normal(
                                size=len(X)
                            )
        return pred
