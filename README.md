# Portfolio Optimization using Monte Carlo Simulation

This project is part of my ongoing journey in **quantitative finance**. It demonstrates how to optimize a portfolio using a Monte Carlo simulation approach while minimizing risk. By simulating 10,000 random portfolios using historical data from **AAPL**, **MSFT**, and **TSLA**, the project identifies the portfolio with the highest **Sharpe ratio**, a key metric for risk-adjusted returns.

## Key Insights

- **Annualized Portfolio Returns**: The portfolio's expected return was calculated based on historical data.
- **Annualized Portfolio Volatility**: The portfolio risk was computed using annualized volatility.
- **Efficient Frontier**: The relationship between portfolio risk and return was visualized, showing the tradeoff between risk and return for different portfolios.
- **Optimal Portfolio**: The portfolio with the highest Sharpe ratio was identified, along with its asset weights for each stock.

## Libraries Used

This project is implemented using the following Python libraries:
- **yfinance**: For downloading historical stock data.
- **numpy**: For mathematical calculations.
- **pandas**: For data manipulation.
- **matplotlib**: For data visualization.
