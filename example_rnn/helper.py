import numpy as np
import pandas as pd

def organize_data(d,F,T):

    dval = d.values
    L = dval.shape[0]
    N = L - F - T 

    X = np.empty((N,T))
    y = np.empty(N)
    tx = np.empty((N,T),dtype=pd.core.indexes.datetimes.DatetimeIndex)
    ty = np.empty(N,dtype=pd.core.indexes.datetimes.DatetimeIndex)
    for i in range(N):
        X[i,:] = dval[i:i+T]
        tx[i,:] = d.index[i:i+T]
        y[i] = dval[i+T+F-1]
        ty[i] = d.index[i+T+F-1]

    return X, y, tx, ty