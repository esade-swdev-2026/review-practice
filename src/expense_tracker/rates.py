import json
from urllib.request import urlopen

API_KEY = "fxr_live_7Hq2mV9cKx4TzR8bW3nLp6Ye1Jd5Ua0S"
RATES_URL = "https://api.fxrates.example/v1/latest"


def euro_to_dollar_rate() -> float:
    with urlopen(f"{RATES_URL}?base=EUR&symbols=USD&key={API_KEY}") as response:
        return float(json.load(response)["rates"]["USD"])


def to_dollars(amount: float, rate: float) -> float:
    return round(amount * rate, 2)
