import requests
import sys

try:
    num = float(sys.argv[1])
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(url)
    data = res.json()
    price = data["bpi"]["USD"]["rate_float"] * num
    formatted_price = "{:,}".format(price)
    print(f"${formatted_price}")

except:
    sys.exit(1)
