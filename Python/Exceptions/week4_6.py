#bitcoin price index
import sys
import json
import requests
try:
    n=float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except (requests.RequestException,requests.ConnectionError,requests.HTTPError,requests.ConnectTimeout,requests.ReadTimeout,requests.Timeout):
    sys.exit()
o=response.json()
rate=o["bpi"]["USD"]["rate"]
cost=n*float(rate.replace(",",""))
print(f"${round(cost,4):,.4f}")
 