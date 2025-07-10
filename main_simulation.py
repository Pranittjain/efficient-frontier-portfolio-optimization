import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



tickers=["AAPL","MSFT","TSLA"]
data = yf.download(tickers, start='2018-01-01', end='2025-01-01')

data = data['Close']
returns=data.pct_change()
# pct_change() is a pandas function that calculates the percentage change between consecutive values.
cov_matrix = returns.cov()

num_of_portfolios=10000
portfolio_returns=np.zeros(num_of_portfolios)
portfolio_volat=np.zeros(num_of_portfolios)
sharpe_ratio=np.zeros(num_of_portfolios)
all_weights = np.zeros((num_of_portfolios, len(tickers)))
risk_free_rate=0.04
for i in range(num_of_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)
    all_weights[i] = weights
    portfolio_returns[i] = np.sum(weights * returns.mean())
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_volat[i]=np.sqrt(portfolio_variance)
    sharpe_ratio[i] = (portfolio_returns[i] - risk_free_rate) / portfolio_volat[i]

portfolio_returns_annualized = portfolio_returns * 252  # Annualize the portfolio returns (252 trading days)
portfolio_volat_annualized = portfolio_volat * np.sqrt(252)  # Annualize the volatility (scaled by sqrt(252))
sharpe_ratio_annualized = (portfolio_returns_annualized - risk_free_rate) / portfolio_volat_annualized  # Annualized Sharpe ratio

max_sharpe_idx = np.argmax(sharpe_ratio_annualized)
max_sharpe_return = portfolio_returns_annualized[max_sharpe_idx]
max_sharpe_volatility = portfolio_volat_annualized[max_sharpe_idx]
max_sharpe_ratio = sharpe_ratio_annualized[max_sharpe_idx]
optimal_weights = all_weights[max_sharpe_idx]

print("\nOptimal Portfolio with Highest Sharpe Ratio:")
print(f"Return: {max_sharpe_return:.4f}")
print(f"Volatility (Risk): {max_sharpe_volatility:.4f}")
print(f"Sharpe Ratio: {max_sharpe_ratio:.4f}")
print("\nOptimal Portfolio Weights:")
for ticker, weight in zip(tickers, optimal_weights):
    print(f"{ticker}: {weight:.4f}")

plt.scatter(portfolio_volat_annualized, portfolio_returns_annualized, c=sharpe_ratio_annualized, cmap='viridis', alpha=0.7)
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Portfolio Volatility (Risk)')
plt.ylabel('Portfolio Return')
plt.title('Monte Carlo Simulation - Efficient Frontier')
plt.scatter(max_sharpe_volatility, max_sharpe_return, color='red', marker='*', s=200, label="Optimal Portfolio")
plt.legend()
plt.savefig('efficient_frontier.png')
plt.show()