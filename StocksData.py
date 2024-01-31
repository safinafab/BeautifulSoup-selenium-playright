import requests
from bs4 import BeautifulSoup
import json

url ="https://finance.yahoo.com/most-active/"

r= requests.get(url=url)
response = r.text
soup = BeautifulSoup(response,'html.parser')
most_actives = soup.select('tr')
# print(most_actives)
# company_list = [c.find('td').text for c in most_actives[1::]]
# print(company_list)
list=[]
for i in most_actives[1::]:
    dictionary={
        "name": i.find_all('td')[1].text,
        # print(name)
        "price" :i.find_all('td')[2].text,
        # print(price)
        "change": i.find_all('td')[3].text,
        # print(change)
    }
    list.append(dictionary)


#now i want the data to be converted to a json file
with open("myStocks.json","w") as f:
    json.dump(list,f)