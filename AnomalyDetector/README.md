## Anomaly detection using an LSTM-based Autoencoder 


An autoencoder is a type of artificial neural network used to learn efficient data codings in an unsupervised manner (although they are trained using supervised learning methods). The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”. 


Along with the reduction side, a reconstructing side is learned, where the autoencoder tries to generate from the reduced encoding a representation as close as possible to its original input, hence its name. The goal is to minimize reconstruction error based on a loss function, such as the mean squared error.

![image](https://user-images.githubusercontent.com/12089275/111929730-8336ff80-8ab7-11eb-9063-0df948ae5444.png)

In this notebook, we will try to detect anomalies in Ford’s historical stock price time series data with an LSTM autoencoder.
The data can be downloaded from Yahoo Finance (also available in the repository).

The steps we will follow to detect anomalies in Ford stock price data using an LSTM autoencoder:
- Train an LSTM autoencoder on the Ford stock price data from 1972–06–01 to 2010–12–31. We assume that there were no anomalies and they were normal.
- Use the LSTM autoencoder to reconstruct the error on the test data from 2011–01–01 to 2021–03–19.
- If the reconstruction error for the test data is above the threshold (25% of the max MAE), we classify the data point as an anomaly.
