import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_convert(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.

    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)
    elif currency == "EUR" or "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": os.getenv("TOKEN")}

        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return float(response.json()["result"])
    else:
        return float(amount)
