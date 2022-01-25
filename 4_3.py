from requests import get, utils
from decimal import Decimal, ROUND_HALF_UP
from datetime import date


def currency_rates(currency_code):
    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    xml_daily_list = content.split('</Valute>')
    for currency_str in xml_daily_list:
        if currency_code.upper() in currency_str.split('</CharCode>')[0][-3:]:
            exchange_rate = (Decimal(currency_str.split('<Value>')[1][:-8].replace(',', '.')) / Decimal(
                (currency_str.split('<Nominal>')[1].split('</Nominal>')[0]))).quantize(Decimal('1.00'), ROUND_HALF_UP)
            exchange_date = content.split('Date="')[1][:10].split('.')
            exchange_date = date(day=int(exchange_date[0]), month=int(exchange_date[1]), year=int(exchange_date[2]))
            return [str(exchange_rate), str(exchange_date)]


print(currency_rates('usd'))
print(currency_rates('EUR'))
