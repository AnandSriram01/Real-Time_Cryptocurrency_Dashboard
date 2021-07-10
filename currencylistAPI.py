import requests
import pprint
import json

parameters = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10
}

response = requests.get("https://api.coingecko.com/api/v3/coins/markets", params=parameters)
print(response.status_code)
# pprint.pprint(response.json())

text = json.dumps(response.json(), sort_keys=True, indent=4)
# print(text)

reqd_info = []

for coin in response.json() :
    # print(type(coin))
    name = coin['name']
    mktcap = "{:,}".format(coin['market_cap'])
    volume = "{:,}".format(coin['total_volume'])
    price = coin['current_price']
    change_percent = coin['price_change_percentage_24h']
    rank = coin['market_cap_rank']

    dict = {
        "mktcap_rank": rank,
        "coin_name": name,
        "current_price": price,
        "market_cap": mktcap,
        "volume": volume,
        "percentage_change": change_percent
    }

    reqd_info.append(dict)

print(json.dumps(reqd_info, sort_keys=False, indent=4))
