# Fama-Markowitz-Mini-Project

## Context
Multi-factor modelling is a popular way to analyze the performance of a portfolio using specific characteristics (also called factors). Instead of attributing all the returns of one stock to the overall market, it captures the underlying factors that can influence risk and return like macroeconomic factors (i.e., interest rates) and fundamental factors (i.e., firm size).
One well-known example would be the Fama-French three-factor model which  is used to describe stock returns using three factors: 
size of firms (difference between small-cap and large-cap firms), 
book-to-market values (high minus low), and 
excess return on the market (portfolio’s return less the risk-free rate of return). 
These models often utilize covariance matrices, but when there are a lot of firms in one portfolio, the data becomes noisy which leads to unreliable risk forecasts.
Fortunately, Random Matrix Theory (RMT) is a statistical tool commonly used to separate meaningful correlations from noise alongside the Marchenco Pasteur distribution. If this were to be used on the covariance matrices, then we can better filter out the noise from the dataset. 
In this mini-project, we aim to determine whether noise-filtered covariance matrices derived from RMT provide a more accurate and stable foundation for multifactor-based portfolio modeling compared to the Markowitz Portfolio Optimization and the unmodified Fama-French three-factor model.

## Goals
### Basic Goal: Compare the Fama-French three-factor model and the Markowitz Portfolio Optimization 
Plan: 
Data gathering
Randomly select 30 stocks from the S&P 500 
Get data for each of the stocks from the past 3 years using yfinance.  
Get the daily Fama-French factors from the Kenneth French website.
Implement the PCA Markowitz portfolio optimization
PCA on normalized returns
Check if PC1 is significant using Tracy-Widow
Get the portfolio that corresponds to PC1
Implement the Fama-French three-factor model
For each stock, run the standard time series regression for the Fama-French model. 
Get the covariance matrix from the residuals 
Compare the 2 portfolios against the efficient frontier

### Intermediate Goal:  Integrate rotationally invariant estimators (RIE) in the Markowitz Portfolio
Plan:
Implement the RIE Markowitz portfolio optimization
Estimate the covariance matrix by doing RIE on the log returns
Check which eigenvectors are significant using Marchenco-Pastur and pick one to use for the portfolio (this should be the second largest eigenvalue).
Compare its fit to the efficient frontier.

### Advanced Goal: Integrate RMT within the fama-french factor model
Plan:
As per the study done by Molero-Gonzales et al., (2023), the steps we will follow are the ff:
Apply the Fama-French 3 Factor Model on the log returns matrix.
Turn the coefficients for each of the factors for each stock in the portfolio into a matrix.
Apply RMT.
Eigenvalue decomposition
Identify the significant eigenvectors using the Tracy-Widom distribution.
Create a portfolio out of the significant factors and the residuals.
Compare its performance against the matrix in the Basic Goal section to predict stock risk.
