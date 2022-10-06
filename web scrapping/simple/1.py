import requests
from bs4 import BeautifulSoup
r=requests.get("https://pythonizing.github.io/data/example.html")
c=r.content
#print(type(c))
#print(c)
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
soup.find_all("div",{"class":"cities"})
all=soup.find_all("div",{"class":"cities"})
#print(type(all))
#all[0].find_all("h2")
#print(all[0].find_all("h2"))
#print(type(all[0].find_all("h2")))
all[0].find_all("h2")[0].text
#print(all[0].find_all("h2")[0].text)
for item in all:
    print(item.find_all("h2")[0].text)