# A Comparison of Portfolios From the Markowitz Portfolio Optimization and the Fama-French Three-Factor Model

## Context
Multi-factor modelling is a popular way to analyze the performance of a portfolio using specific characteristics (also called factors). 
Instead of attributing all the returns of one stock to the overall market, it captures the underlying factors that can influence risk and return like macroeconomic factors (i.e., interest rates) and fundamental factors (i.e., firm size).
One well-known example would be the Fama-French three-factor model which  is used to describe stock returns using three factors: 
1. size of firms (difference between small-cap and large-cap firms), 
2. book-to-market values (high minus low), and 
3. excess return on the market (portfolio’s return less the risk-free rate of return). 

These models often utilize covariance matrices, but when there are a lot of firms in one portfolio, the data becomes noisy which leads to unreliable risk forecasts.

Fortunately, Random Matrix Theory (RMT) is a statistical tool commonly used to separate meaningful correlations from noise alongside the Marchenco Pasteur distribution. 
If this were to be used on the covariance matrices, then we can better filter out the noise from the dataset. 
In this mini-project, we aim to determine whether noise-filtered covariance matrices derived from RMT provide a more accurate and stable foundation for multifactor-based portfolio modeling compared to the Markowitz Portfolio Optimization and the unmodified Fama-French three-factor model.

## Problem Statement
Estimating portfolio risk accurately is challenging when asset correlations are noisy, leading to unstable and unreliable forecasts. Traditional covariance matrices often fail to separate meaningful relationships from random noise in large datasets.

## Proposed Solution
This mini-project aims to determine whether RMT-based noise-filtering techniques can improve the stability and predictive accuracy of portfolio risk models.

## Methodology
We based our methodology on two papers:
1. Sandoval et al. (2014)
         - Used Random Matrix Theory to clean a correlation matrix of log returns and build a portfolio.
2. L. Molero-González et al. (2023)
         - With the Onatski test, they concluded that the presence of only one factor, Market factor,  is significant.


## Goals
### Basic Goal: Compare the Fama-French three-factor model and the Markowitz Portfolio Optimization 
Plan: 
1. Data gathering

         - We randomly chose 30 firms from the S&P 500.
         - Using the yfinance API, gathered information on the closing prices of the stocks from August 31, 2022 until August 31, 2025.
         - We turned the closing prices into two matrices to be used later on:
               - Simple returns
               - Log returns
         - We used  the daily Fama-French factors from the Kenneth French website from August 31, 2022 until August 31, 2025.
3. Implement the PCA Markowitz portfolio optimization
      - PCA on normalized returns
      - Check if PC1 is significant using Tracy-Widow
      - Get the portfolio that corresponds to PC1
4. Implement the Fama-French three-factor model
      - For each stock, run the standard time series regression for the Fama-French model. 
      - Get the covariance matrix from the residuals 
5. Compare the 2 portfolios against the efficient frontier

### Intermediate Goal:  Integrate rotationally invariant estimators (RIE) in the Markowitz Portfolio
Plan:
1. Implement the RIE Markowitz portfolio optimization
      - Estimate the covariance matrix by doing RIE on the log returns
2. Check which eigenvectors are significant using Marchenco-Pastur and pick one to use for the portfolio (this should be the second largest eigenvalue).
3. Compare its fit to the efficient frontier.

### Advanced Goal: Integrate RMT within the fama-french factor model
Plan:
As per the study done by Molero-Gonzales et al., (2023), the steps we will follow are the ff:
1. Apply the Fama-French 3 Factor Model on the log returns matrix.
2. Turn the coefficients for each of the factors for each stock in the portfolio into a matrix.
3. Apply RMT.
      - Eigenvalue decomposition
      - Identify the significant eigenvectors using the Tracy-Widom distribution.
4. Create a portfolio out of the significant factors and the residuals.
5. Compare its performance against the matrix in the Basic Goal section to predict stock risk.

