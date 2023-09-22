import requests
import json
import sys


if len(sys.argv) !=2:
    sys.exit("Missing command-line argument")
elif float(sys.argv[1])>0:
    try:
        price=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        i = price.json()
        result=i["bpi"]["USD"]["rate_float"]*float(sys.argv[1])
        print(f"${result:,.4f}")
    except requests.RequestException:
            sys.exit("Cant get a rate")
else:
    sys.exit("Command-line argument is not a number")
