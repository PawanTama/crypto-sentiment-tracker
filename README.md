
# Crypto Market + Sentiment Tracker

**Live Demo**: [View Tableau Dashboard](https://public.tableau.com/app/profile/pawan.tamang/viz/CryptoMarketSentimentTrackerBTCAnalysisAprilMay2025/Dashboard1?publish=yes)

---

## Overview
This project combines financial data and natural language processing to explore how public sentiment in cryptocurrency news may influence **Bitcoin (BTC)** price movements. It utilizes Python for data ingestion and sentiment analysis, and Tableau for interactive visualization.

---

## 🔧 Tech Stack
- **Python 3**: Data collection, processing
- **APIs Used**:
  - [CoinGecko API](https://www.coingecko.com/en/api) – BTC price history
  - [NewsAPI](https://newsapi.org/) – Crypto news headlines
- **Libraries**:
  - `pandas`, `requests`, `vaderSentiment`
- **Tableau Public**: Dashboard for sentiment vs. price visualization

---

## Project Structer 

```
crypto_sentiment_tracker/
├── data/
│   ├── bitcoin_prices.csv
│   ├── news_sentiment.csv
│   └── merged_crypto_data.csv
├── scripts/
│   ├── fetch_prices.py
│   ├── fetch_sentiment.py
│   └── process_data.py
├── notebooks/              # (optional for EDA)
├── README.md
```

---

## How It Works

1. **`fetch_prices.py`** – Pulls hourly BTC price data from CoinGecko.
2. **`fetch_sentiment.py`** – Uses NewsAPI to grab recent crypto headlines and analyzes their sentiment using VADER.
3. **`process_data.py`** – Merges price and sentiment by timestamp and outputs a clean dataset for Tableau.
4. **Tableau Dashboard** – Visualizes the correlation between sentiment scores and price changes with filters and a trendline.

---

## Dashboard Features
- Scatterplot of **sentiment score vs. % price change**
- Trendline to show correlation direction
- Interactive tooltips for timestamp context
- Dashboard title and layout suitable for presentations

---

## ✨ Key Takeaway
Even with a small window of sentiment data, directional shifts in public sentiment can align with short-term BTC price volatility. This shows potential for **news-based signal integration** in crypto analytics.

---

## Credits
- Built by [Pawan Tamang]
- Sentiment analysis: VADER
- Visualization: Tableau Public
