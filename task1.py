import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


data = pd.read_csv("http://api.bitcoincharts.com/v1/trades.csv?symbol=bitstampUSD", names= ["time", "amount", "price"])
# print(data)
for x in data.index:
    if data.loc[x, "time"] < data["time"][10000] or  data.loc[x, "price"] >1 :
        data.drop(x, inplace=True)



x = np.array(data["time"]).reshape(-1, 1)
y = np.array(data["price"])




poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

# Fit the model
model = LinearRegression()
model.fit(x_poly, y)

# Predictions
y_pred = model.predict(x_poly)

timestamp = 1719252939
t_poly = poly.fit_transform(np.array(timestamp).reshape(-1, 1))
t_pred = model.predict(t_poly)
print(t_pred)

# Evaluation
# mse = mean_squared_error(y, y_pred)
# print(f'Mean Squared Error: {mse}')

# Plotting
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Regression')
plt.show()




