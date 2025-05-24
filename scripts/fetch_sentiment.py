import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

api_key = "fe24d86776484170b23592695f142351"
query = "cryptocurrency OR bitcoin OR ethereum"
page_size = 250  # max per request but max is only 100 becasue of the free api limit
analyzer = SentimentIntensityAnalyzer()


# fetching news from Newsapi

all_articles = []
for page in range(1, 6):  # pages 1 to 5
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 50,
        "page": page,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'articles' not in data:
        print("API Error:", data)
        break

    all_articles.extend(data['articles'])

records = []
for article in all_articles:
    title = article['title']
    description = article.get('description') or ""
    combined_text = title + " " + description
    published_at = article['publishedAt']
    score = analyzer.polarity_scores(combined_text)['compound']
    
    records.append({
        "datetime": pd.to_datetime(published_at),
        "headline": title,
        "sentiment_score": score
    })
    
df = pd.DataFrame(records)
df = df.sort_values("datetime")
df.to_csv("./data/news_sentiment.csv", index=False)
print(f" Saved {len(df)} headlines to data/news_sentiment.csv")