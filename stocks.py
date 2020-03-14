import requests

url = 'https://api.iextrading.com/1.0'


def all_symbols():
    """Returns a list of all available symbols"""
    endpoint = '/ref-data/symbols'
    req = requests.get(url + endpoint)
    data = req.json()
    symbols = [(item['name'], item['symbol']) for item in data]
    return symbols


def last_price(symbol):
    """Gets the prices information for a given symbol"""
    endpoint = f'/tops/last?symbols={symbol}'
    req = requests.get(url+endpoint)
    return req.json()


if __name__ == '__main__':
    msft = last_price('MSFT')
    print(msft)
