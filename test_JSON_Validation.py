from jsonschema import validate
import requests


def testJSONschemaValidation(base_url):
    schema = {
        "type": "object",
        "properties": {
            "Realtime Currency Exchange Rate": {
                "type": "object",
                "properties": {
                    "1. From_Currency Code": {"type": "string"},
                    "2. From_Currency Name": {"type": "string"},
                    "3. To_Currency Code": {"type": "string"},
                    "4. To_Currency Name": {"type": "string"},
                    "5. Exchange Rate": {"type": "string"},
                    "6. Last Refreshed": {"type": "string"},
                    "7. Time Zone": {"type": "string"},
                    "8. Bid Price": {"type": "string"},
                    "9. Ask Price": {"type": "string"},
                }
            }
        },
    }
    url = base_url + '?function=CURRENCY_EXCHANGE_RATE&' \
                     'from_currency=USD' \
                     '&to_currency=EUR' \
                     '&apikey=demon'
    data = requests.get(url).json()
    validate(data, schema)
