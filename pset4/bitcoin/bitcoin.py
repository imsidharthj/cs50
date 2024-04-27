import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    argument_float = float(sys.argv[1])
except ValueError:
    sys.exit("Command line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if response.status_code == 200:
    try:
        per_bitcoin = response.json()["bpi"]["USD"]["rate_float"]
        amount = per_bitcoin * float(sys.argv[1])
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Error: fetching Bitcoin price.")
else:
    sys.exit(f"Error: Bitcoin price data.{response.status_code}")