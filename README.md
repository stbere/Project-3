# Project-3
Project 3 material for Bootcamp: TCC-VIRT-DATA-PT-10-2022-U-LOLC-MTTH

Created by: Steve, Jared, Levi, and Zac

## Requirements

### Data and Delivery (25 points)
Data components used in the project are clearly documented. (5 points)
The dataset contains at least 100 unique records. (5 points)
A database is used to house the data (SQL, MongoDB, SQLite, etc.). (5 points)
The project is powered by a Python Flask API and includes HTML/CSS, JavaScript, and the chosen database. (10 points)

### Back End (25 points)
The page created to showcase data visualizations runs without error. (7.5 points)
A JavaScript library not shown in class is used in the project. (7.5 points)
The project conforms to one of the following designs: (10 points)
A Leaflet or Plotly chart built from data gathered through web scraping.
A dashboard page with multiple charts that all reference the same data.

### Visualizations (25 points)
A minimum of three unique views present the data. (5 points)
Multiple user-driven interactions (such as dropdowns, filters, or a zoom feature) are included on the final page. (5 points)
The final page displays visualizations in a clear, digestable manner. (5 points)
The data story is easy to interpret for users of all levels. (10 points)

### Group Presentation (25 points)
All group members speak during the presentation. (5 points)
The content is relevant to the project. (5 points)
The presentation maintains audience interest. (5 points)
Content, transitions, and conclusions flow smoothly within any time restrictions. (10 points)

# Stock Prices vs Crypto Prices Analysis

This website presents an analysis of stock prices and crypto prices, exploring their similarities and differences, as well as their potential benefits and risks.

## Tools used
- Plotly
- Chart.js
- Pandas
- SQLite
- Flask

## Data Sources

The analysis is based on the following data sources:

- Stock prices and news: Yahoo Finance API
- Crypto prices: CoinGecko API

The analysis compares the performance of the Dow Jones Industrial Average (as a proxy for the stock market) and the S&P Cryptocurrency Indicies (as a proxy for the crypto market).

The Dow Jones Industrial Average is a stock market index that tracks the performance of 30 large publicly traded companies listed on US stock exchanges, providing a benchmark for the overall health of the US stock market and economy. The included companies are often referred to as "blue-chip stocks," which are high-quality, established companies with a reputation for reliability and relatively lower risk compared to other stocks. It's important to note that the performance of the S&P Cryptocurrency Indices and the Dow Jones Industrial Average can be affected by different factors, such as changes in market sentiment, geopolitical events, and economic data. Therefore, any comparison of their performance should be done with caution and with an understanding of the unique characteristics and drivers of each index. The S&P Cryptocurrency LargeCap Index may be the closest match to the DJIA in terms of its focus on larger, well-established cryptocurrencies. The index includes the 10 largest cryptocurrencies by market capitalization, with a minimum liquidity threshold and other criteria for inclusion. However, it's important to note that cryptocurrency is a relatively new asset class and its characteristics and performance are quite different from traditional stocks and indices like the DJIA. So, while the S&P Cryptocurrency LargeCap Index may be a useful benchmark for comparison, it may not be a perfect match in terms of risk and return characteristics.

https://www.spglobal.com/spdji/en/indices/digital-assets/sp-cryptocurrency-largecap-index/#overview

The launch date of the S&P Cryptocurrency LargeCap Index (USD) was July 13, 2021. All information presented prior to an index’s Launch Date is hypothetical (back-tested), not actual performance, and is based on the index methodology in effect on the index launch date. A score closer to 1.0 represents more volatility. The closer the value is to 1.0, the higher the standard deviation of the daily percentage changes, which indicates a greater level of price fluctuation and therefore more volatility. Conversely, a value closer to 0.0 indicates less volatility, as the daily percentage changes have a lower standard deviation and the price is more stable. (edited) 

The Sharpe ratio is a measure of risk-adjusted return, which takes into account the volatility of the returns. The correlation coefficient measures the degree of association between the stock market and the crypto market.

## Results

The analysis shows that:

Based on the data analysis conducted, it can be concluded that the performance and volatility of the Dow Jones Industrial Average (DJI) and the S&P Cryptocurrency Largecap Index are correlated to some extent. In terms of performance, both indices experienced significant growth in value in early 2020, but faced a sharp decline in September 2022. Additionally, the peak performance of both indices appears to have been correlated, with the DJI reaching its peak in December 2021 and the S&P in November 2021.
Regarding volatility, both indices showed a downward trend in volatility in 2018, but the DJI demonstrated an increase in volatility after September 2018, while the S&P Cryptocurrency Largecap Index continued to exhibit higher volatility than the DJI but with a continuous decrease in volatility from June 2017 to February 2023.
These observations may provide useful insights for investors seeking to make informed decisions about their portfolio, as the DJI and the S&P Cryptocurrency Largecap Index have shown different patterns of performance and volatility over the analyzed period, with some correlations between their peak performance and volatility trends.