# linear regression modeling
# CPSC 483
import timeit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
data = pd.read_csv('Data1.csv')

x = np.linspace(0,1,101)
y = 1 + x * np.random.random(len(x))



tic = timeit.default_timer()
X1 = data.iloc[:,:-1].values
y1 = data.iloc[:,4].values
X_train, X_test, y_train, y_test = train_test_split(X1,y1, test_size = 0.2, random_state=0) 
X_train_df, X_test_df = pd.DataFrame(X_train), pd.DataFrame(X_test)
poly = PolynomialFeatures(degree=4)
X_train_poly = poly.fit_transform(X_train_df)
X_test_poly = poly.fit_transform(X_test_df)


regressor = LinearRegression()
regressor.fit(X_train_poly, y_train)
y_pred = regressor.predict(X_test_poly)
toc = timeit.default_timer()
delay = toc-tic
print(delay)

print(r2_score(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))

print(regressor.coef_)
print(len(regressor.coef_))

"""
plt.figure(figsize = (10,8))
plt.plot(x1, y1, 'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()"""

"""
A = numpy.vstack([x,numpy.ones(len(x))]).T

y = y[:,numpy.newaxis]

alpha = numpy.dot((numpy.dot(numpy.linalg.inv(numpy.dot(A.T,A)),A.T)),y)
print(alpha)

plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
"""

data.head()