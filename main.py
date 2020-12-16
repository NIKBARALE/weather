import requests
from bs4 import BeautifulSoup
result = requests.get('https://pogoda1.ru/katalog/sverdlovsk-oblast/temperatura-vody/')
data = BeautifulSoup(result.content)
ar = []
print("Температура рек: ")
for table in data.select('.x-table > .x-row'):
	ar.append([])
	temperature = table.select_one('.x-cell-water-temp').get_text(strip=True)
	links = [a for a in table.select('.x-cell > .link')]
	name = links[0].text
	ar[-1].append(temperature)
	ar[-1].append(name)
	print(ar[-1])
