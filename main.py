import requests
from bs4 import BeautifulSoup
try:
  result = requests.get('https://pogoda1.ru/katalog/sverdlovsk-oblast/temperatura-vody/')
  data = BeautifulSoup(result.content)
  fi = open("inf.txt", 'w')
  fi.write('Температура рек: \n')
  for table in data.select('.x-table > .x-row'):
	  temperature = table.select_one('.x-cell-water-temp').get_text(strip=True)
	  links = [a for a in table.select('.x-cell > .link')]
	  name = links[0].text
	  new_name = name.split()
	  fi.write(new_name[1] + ':\t\t ' + temperature + '\n')
  fi.close()
  print('готово')
except:
  print('проверь код/соединение с сервером')