from sklearn.linear_model import LinearRegression
import numpy as np


def train(dateFrame):
    X_train = np.array(dateFrame.wind).reshape((-1, 1))
    y_train = np.array(dateFrame.drop(columns=['wind','solar','biomass','coal']))
    model=LinearRegression()
    model.fit(y_train,X_train)
    model = LinearRegression().fit(X_train, y_train)
    r_sq = model.score(X_train, y_train)
    print('coeficiemtul de determinare:', r_sq)
    return model

