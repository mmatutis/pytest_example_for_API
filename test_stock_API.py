import pytest
import requests
import csv


class TestStockAPI:

    parameters = []
    with open('external_data.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            concat = []
            for item in rows:
                concat.append(item)
            parameters.append(concat)

    @pytest.mark.parametrize("from_currency, to_currency", parameters)
    def test_currency_exchange_rate(self, base_url, from_currency, to_currency):
        url = base_url + '?function=CURRENCY_EXCHANGE_RATE&' \
                         'from_currency=' + from_currency + \
                         '&to_currency=' + to_currency + '&apikey=demon'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200, "Bad status code"
        assert data['Realtime Currency Exchange Rate'][
                   '1. From_Currency Code'] == from_currency, "Fail, bad from currency"
        assert data['Realtime Currency Exchange Rate']['3. To_Currency Code'] == to_currency, "Fail, bad from currency"
        assert float(data['Realtime Currency Exchange Rate'][
                         '5. Exchange Rate']) > 0, "Fail, Exchange rate is less then 0"

    def test_fx_daily(self, base_url):
        url = base_url + '?function=FX_DAILY' \
                         '&from_symbol=EUR' \
                         '&to_symbol=USD' \
                         '&apikey=demo'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200, "Bad status code"
        for item in data['Time Series FX (Daily)']:
            assert type(data['Time Series FX (Daily)'][item]['1. open']) is str, "Fail bad element type"
            assert type(data['Time Series FX (Daily)'][item]['2. high']) is str, "Fail bad element type"
            assert type(data['Time Series FX (Daily)'][item]['3. low']) is str, "Fail bad element type"
            assert type(data['Time Series FX (Daily)'][item]['4. close']) is str, "Fail bad element type"

    def test_crypto_currency_exchange_rate(self, base_url):
        url = base_url + '?function=CURRENCY_EXCHANGE_RATE' \
                         '&from_currency=BTC' \
                         '&to_currency=CNY' \
                         '&apikey=demo'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200, "Bad status code"
        assert data['Realtime Currency Exchange Rate'][
                   '1. From_Currency Code'] == 'BTC', "Fail, bad from currency"
        assert data['Realtime Currency Exchange Rate']['3. To_Currency Code'] == 'CNY', "Fail, bad from currency"

    def test_global_quote(self, base_url):
        url = base_url + '?function=GLOBAL_QUOTE' \
                         '&symbol=MSFT' \
                         '&apikey=demo'
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200, "Bad status code"
        assert data['Global Quote'][
                   '01. symbol'] == 'MSFT', "Fail, bad symbol"
