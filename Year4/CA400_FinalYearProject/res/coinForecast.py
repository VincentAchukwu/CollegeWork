# code is for experimenting with the ARIMA model (p,d,q values, PACF/ACF testing, training the model, etc)

# #########################################

import pandas as pd, numpy as np, matplotlib.pyplot as plt, statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima import auto_arima
from sklearn.metrics import mean_squared_error
from math import sqrt

# reading dataset, setting date column as index, treating date values as dates and not strings
df = pd.read_csv("BTCEUR.csv", index_col="date", parse_dates=True)
# drop any missing values in the dataset
df = df.dropna()

# determining if the data is stationary or not
from statsmodels.tsa.stattools import adfuller
def adf_test(dataset):
    dftest = adfuller(dataset, autolag="AIC")
    print("1. ADF: ", dftest[0])
    print("2. P-Value: ", dftest[1])
    print("3. Num Of Lags: ", dftest[2])
    print("4. Num Of Observations Used For ADF Regression:", dftest[3])
    print("5. Critical Values:")
    for key, val in dftest[4].items():
        print("\t", key, ": ", val)

# # if p < 0.05 it is stationary, else it's non-stationary
adf_test(df["close"])
# P-Value: 0.9862380601118591 -> therefore it's non-stationary, need to make it stationary

# differencing once to make it stationary
df["Close First Difference"] = df["close"] - df["close"].shift(1)
adf_test(df["Close First Difference"].dropna())
plt.title("Close First Difference")
df["Close First Difference"].plot()
plt.show()
# now P-Value: 1.2770080148370808e-10 -> therefore it's stationary

# using auto_arima to determine the best model from the order values (p, d, q)
#   - p = AR model lags (best done with PACF)
#   - d = differencing
#   - q = MA lags (best done with ACF)
stepwise_fit = auto_arima(df['close'], trace=True, suppress_warnings=True)
print(stepwise_fit.summary())
# result we get is (2, 1, 2)

# differencing the dataset for PACF and ACF tests
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df["Close First Difference"].iloc[2:], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df["Close First Difference"].iloc[2:], lags=40, ax=ax2)
plt.title("Close First Difference")
plt.show()

# splitting the data into training and testing (last 30 for testing, everything prior is training)
print(df.shape)
train = df.iloc[:-30]
test = df.iloc[-30:]
print("train and test shape:", train.shape, test.shape)

# fitting the train model
model = ARIMA(train["close"], order=(2, 1, 2))
model = model.fit()
print("Model summary for training set:", model.summary())

# now we predict via specifying the start and end range
# in this case, we want to compare prediction with the testing dataset
start = len(train)
end = len(train) + len(test) - 1
# if the predicted values don't have date values as index, uncomment specified line below*
prediction = model.predict(start=start, end=end, typ="levels").rename("ARIMA Predictions")
prediction.index = df.index[start:end + 1]    # uncomment if needed*
# plotting comparison of predicted vs test
plt.title("Prediction vs Testing Set")
test["close"].plot(legend=True)
prediction.plot(legend=True)
plt.show()

# mean squared error for analysis
print(test["close"].mean())
rmse = sqrt(mean_squared_error(prediction, test["close"]))
print(rmse)

# training the model now based on entire dataset to make future predictions
model2 = ARIMA(df["close"], order=(2, 1, 2))    # (need to experiment w/ p, d, q values)
model2 = model2.fit()
# print(df.tail())  # checking what the last date is, then predict from this day onward

# let's predict Bitcoin's price from Oct 7th 2021 until 26th Mar 2022
indexFutureDates = pd.date_range(start="2021-10-07", end="2022-03-26")
prediction = model2.predict(start=len(df), end=len(df) + 170, typ="levels").rename("ARIMA Predictions")
# like before, we're handling dataset for indexing so we can plot it
prediction.index = indexFutureDates
# print(prediction)

# now we're plotting predicted vs actual price
plt.title("Bitcoin Price Prediction")
df["close"].plot(figsize=(12, 5), legend=True)
prediction.plot(figsize=(12, 5), legend=True)
plt.show()
