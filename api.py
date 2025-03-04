import requests
import json

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)

if response.status_code == 200:
        data = response.json()
        print("data==",data)
        
   


