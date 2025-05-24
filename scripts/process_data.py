import pandas as pd

# Load Data 
price_df = pd.read_csv("./data/bitcoin_prices.csv", parse_dates=["datetime"])
sentiment_df = pd.read_csv("./data/news_sentiment.csv", parse_dates=["datetime"])

# Round datetimes to the hour for joining 
sentiment_df['datetime'] = sentiment_df['datetime'].dt.tz_localize(None).dt.floor('d')
price_df['datetime'] = price_df['datetime'].dt.floor('d')


#sentiment scores per hour 
sentiment_hourly = sentiment_df.groupby('datetime').agg({
    'sentiment_score': 'mean',
    'headline': lambda x: ', '.join(x[:3])  # keep first 3 headlines per time period
}).reset_index()


# Merge price + sentiment 
merged_df = pd.merge(price_df, sentiment_hourly, on='datetime', how='left')

#  Fill missing sentiment scores with 0 (neutral) 
merged_df['sentiment_score'] = merged_df['sentiment_score'].fillna(0)


merged_df.to_csv("./data/merged_crypto_data.csv", index=False)
print(" Merged data saved to data/merged_crypto_data.csv")
