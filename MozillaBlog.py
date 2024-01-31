import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

listdict=[]
# url="https://blog.mozilla.org/latest/"
def request(url):
    r= requests.get(url=url)
    soup=BeautifulSoup(r.content,'lxml')
    return soup.find_all(name='a',class_='mzp-c-card-block-link')
# print(articles)
def parse(articles):
    for item in articles:
        title=item.find(name='h2',class_='mzp-c-card-title').text
        link = item['href']
        dictionay={
            'title':title,
            'link':link
        }
        listdict.append(dictionay)
    return  
        
def output():
    df = pd.DataFrame(listdict)
    df.to_excel('BlogsPost.xlsx',index=False)
    
x=1 
while True:
    try:
        article=request(f'https://blog.mozilla.org/en/latest/page/{x}/')
        print('started')
        parse(articles=article)
        print(f'rendering page{x}')
        x +=1
        if(x==6):
            break
        time.sleep(2)
    except:
        print('no items available')
        break     
       
output()
print("saved to xl")
    
# for i in range(1,6):   
#     article=requests(f'https://blog.mozilla.org/latest/')
#     # print(f'renedring: page{i}')
#     parse(articles=article)
#     print("collecting data")
#     time.sleep(2)



    
    