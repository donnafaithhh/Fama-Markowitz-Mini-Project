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
1. Data Gathering
    - We randomly chose 30 firms from the S&P 500.
    - Using the yfinance API, gathered information on the closing prices of the stocks from August 31, 2022 until August 31, 2025.
    - We turned the closing prices into two matrices to be used later on:
        - Simple returns
        - Log returns
2. Implement the PCA Portfolio Optimization
    - Apply PCA on normalized, simple returns
    - Get the portfolio that corresponds to PC1
3. Implement the Fama French Portfolio Optimization
    - Get the excess returns from simple returns
    - Get the residuals of the excess returns
    - Get the covariance matrix
    - Get the portfolio that minimizes idiosyncratic risk
4. Compare PCA and Fama-French portfolio optimization to the efficient frontier.
    - Plot random portfolios. 
    - Compare the Sharpe Ratios.

### Intermediate Goal:  Integrate rotationally invariant estimators (RIE) in the Markowitz Portfolio
Plan:
1. Implement RIE Markowitz optimization and filter for the relevant eigenvectors.
    - Implement RIE Markowitz optimization 
    - Get the significant eigenvectors using the Machenco-Pastur distribution.

### Advanced Goal: Integrate RMT within the fama-french factor model
Plan:
As per the study done by Molero-Gonzales et al., (2023), the steps we will follow are the ff:
1. Identify significant factors through the Onatski Test.
    - Split a time series to construct a complex matrix.
    - Compute the eigenvalues
    - Compute the test statistic 
2. Check at different significance levels (0.01, 0.05, 0.1).

