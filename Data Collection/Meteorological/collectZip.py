import requests
from fake_useragent import UserAgent
from selectorlib import Extractor
from pprint import pprint as print

ua = UserAgent()

url = 'https://www.zipcodestogo.com/California/'

ua = UserAgent()
headers = {'User-Agent': ua.random}

site = requests.get(url, headers=headers).text

selector = """
zip_code:
    css: null
    xpath: '//div[@id="leftCol"]//tr[position()>=3 and (position()-3) mod 1=0]//td[1]//a'
    multiple: true
    type: Text
city:
    css: null
    xpath: '//div[@id="leftCol"]//tr[position()>=3 and (position()-3) mod 1=0]//td[2]'
    multiple: true
    type: Text
county:
    css: null
    xpath: '//div[@id="leftCol"]//tr[position()>=3 and (position()-3) mod 1=0]//td[3]'
    multiple: true
    type: Text
"""

zipcode = Extractor.from_yaml_string(selector).extract(site)

with open('zipcode.py', 'w') as f:
    f.write(str(zipcode))