from flask import (
    Blueprint, render_template
)
import requests

url_ = 'https://api.iextrading.com/1.0'


def filter_symbols(filter_):
    """Returns a list of all available symbols"""
    endpoint = '/ref-data/symbols'
    req = requests.get(url_ + endpoint)
    data = req.json()
    symbols = [{'name': item['name'], 'symbol': item['symbol']}
               for item in data
               if filter_.lower() in item['name'].lower()
               or filter_.lower() in item['symbol'].lower()]
    return symbols


def last_price(symbol):
    """Gets the prices information for a given symbol"""
    endpoint = f'/tops/last?symbols={symbol}'
    req = requests.get(url_+endpoint)
    return req.json()


bp = Blueprint('symbols', __name__)


@bp.route('/')
def index():
    return render_template('symbols/index.html')


if __name__ == '__main__':
    msft = last_price('MSFT')
    print(msft)
