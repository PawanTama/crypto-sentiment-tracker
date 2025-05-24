import requests
import pandas as pd
from datetime import datetime

#Config
coin_id = 'bitcoin'  # 'ethereum', 'solana', etc. also work
vs_currency = 'usd'
days = '30'  # '1', '7', '30', '90', 'max'

url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
params = {
    'vs_currency': vs_currency,
    'days': days
}
response = requests.get(url, params=params)
data = response.json()

print("🔍 Raw API response:")
print(data)

# to look for erros
if 'prices' not in data:
    print("Error from API:", data)
    exit()


prices = data['prices']
df = pd.DataFrame(prices, columns=['timestamp', 'price'])
df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
df = df[['datetime', 'price']]

df.to_csv('./data/bitcoin_prices.csv', index=False)
print("Saved to data/bitcoin_prices.csv")
