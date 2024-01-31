import requests
import json
import pandas as pd

url="https://helmboots.com/products.json?limit=250&page=1"
r= requests.get(url=url)
result =r.json()
#now to print all the title
#it is because we are parsing using json
# product_title=result['products'][0]['title']
# print(product_title)
product_list=[]
for i in result['products']:
    title =i['title']
    handle=i['handle']
    created=i['created_at']
    updated=i['updated_at']
    # print(title,handle,created,updated)
    for images in i['images']:
        images=images['src']
    for variant in i['variants']:
        price=variant['price']
        sku=variant['sku']
        available=variant['available']
        # print(price,sku,available)
        dictionary={
            'title':title,
            'handle':handle,
            'created':created,
            'updated':updated,
            'image':images,
            'price':price,
            'sku':sku,
            'available':available,
        }
        product_list.append(dictionary)
# print(product_list)
df=pd.DataFrame(product_list)
df.to_csv('boots.csv',index=False) 
print("saved file to csv")      
    
