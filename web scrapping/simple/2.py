import requests
from bs4 import BeautifulSoup
r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#rint(soup.prettify())
all=soup.find_all("div", "propertyRow")
#print(type(all))
#print(all)
#print(all[0])
#all[0].find_all("")
#print(all[0].find_all(""))
#print(all[0].find_all("h4",{"class":"propPrice"}))
#print(all[0].find("h4",{"class":"propPrice"}))
#print(all[0].find("h4",{"class":"propPrice"}).text)
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n",""))
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        #print(item.find("span",{"class":"infoBed"}).text)
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        #pass
        print(None)

    try:
        print(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        #pass
        print(None)
    
    try:
        print(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        #pass
        print(None)

    try:
        print(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        #pass
        print(None)

    for column_group in item.find_all("div",{"class":"columnGroup"}):
        #print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
            #print(feature_group, feature_name)
            #print(feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)

    print(" ")

#<div class="columnGroup">
#<span class="featureGroup">Age:&nbsp;</span><span class="featureName">New Construction</span>


