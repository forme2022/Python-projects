import pandas
import requests
from bs4 import BeautifulSoup
r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all=soup.find_all("div", "propertyRow")
#all[0].find_all("")
#print(all[0].find_all(""))
#print(all[0].find_all("h4",{"class":"propPrice"}))
#print(all[0].find("h4",{"class":"propPrice"}))
#print(all[0].find("h4",{"class":"propPrice"}).text)
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n",""))
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr)
l=[]
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
#for page in range(0,30,10):
for page in range(0,int(page_nr*10),10):
    
    #print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html",headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    #print(soup.prettify())
    all=soup.find_all("div","propertyRow")
    print(all)

    for item in all:
        d={}
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        #d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            #print(item.find("span",{"class":"infoBed"}).text)
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            #pass
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            #pass
            d["Area"]=None
        
        try:
            d["FullBath"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            #pass
            d["FullBath"]=None

        try:
            d["HalfBath"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            #pass
            d["HalfBath"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            #print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
                #print(feature_group, feature_name)
                #print(feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text

        #print(" ")
        l.append(d)
        #print(l)
        #print(len(l))
df= pandas.DataFrame(l)
print(df)
#df.to_csv("Output.csv")


