# Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true;
# Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
#2zadanie jak znalezc inne kraje z terminalu

import sys
import requests
from pprint import pprint

inp = sys.argv[1]
url = "https://restcountries.com/v3.1/name/{inp}?fullText=true"
response = requests.request(method="GET", url=url)

data = response.json()[0]
pprint(data.keys())
print(f'Ludnosc:\t{data["population"]}')
print(f'Powierzchnia:\t{data["area"]}')
print(f'Waluta:\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t{data["capital"][0]}')