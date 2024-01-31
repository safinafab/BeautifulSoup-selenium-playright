from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file_content:
    contents = file_content.read()

soup = BeautifulSoup(contents, "html.parser")
#to get the entire code along ith indentation
# print(soup.prettify())
anchor_tags = soup.find_all(name="a")

#for getting only the text out of it
# for tags in anchor_tags:
#     print(tags.getText())

name = soup.select(selector="#name")
print(name)


