import sys
import json
import requests

if len(sys.argv) == 1:
    sys.exit('Not enough arguments')
else:
    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit('You are not my type')
    else:
        try:

            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            obj = response.json()
            rate = obj["bpi"]["USD"]["rate"]
            rate_flo = rate.replace(',', '')
            rate_bit = float(rate_flo)
            suma = value * rate_bit
            print(f"${suma:,.4f}")


        except requests.RequestException:
            print('wrong')
