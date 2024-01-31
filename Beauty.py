from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content,"html.parser")
# print(soup.select_one("a"))
all_anchor_tags = soup.findAll(name = "a")
# all_links = [s['href'] for s in soup.select('span.titleline > a[href]')]
# print(all_links)
tag = soup.select('span.titleline > a[href]')
text =[article_text.getText() for article_text in tag]
links = [article_text.get('href') for article_text in tag]
article_upvote =soup.findAll(name="span", class_ ="score")
upvote = [int(vote.getText().split()[0]) for vote in article_upvote]
# print(int(upvote[0].split()[0]))
# print(text)
# print(links)
# print(upvote)

#now to find the most popular article
largest_no = max(upvote)
largest_index = upvote.index(largest_no)
print(links[largest_index])
print(text[largest_index])




# upvote = [vote for vote in article_upvote]
# print(upvote)

# article_text = tag.getText()
# print(article_text)
# article_link = tag.get("href")
# 
# print(article_text)
# print(article_link)
# print(article_upvote)


    
