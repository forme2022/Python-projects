from branca.element import Html
import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html=""" 
vocano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def c_p(ddd):
    if ddd < 1000:
        return "green"
    elif 1000<= ddd <=2000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

fgv= folium.FeatureGroup("Volcanoes")

for a, b, c in zip(lat, lon, elev):
    iframe=folium.IFrame(html=html % (a, b, c), width=200, height=100)
    fgv.add_child(folium.Marker(location=[a, b], radius = 6, popup=folium.Popup(iframe), fill=True, fill_color=c_p(c), color = "grey", fill_opacity=0.7, icon=folium.Icon(color=c_p(c))))


fgp= folium.FeatureGroup("population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="UTF-8-sig").read(),
style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 1000000 else "orange" if 1000000 <= x["properties"]["POP2005"] < 2000000 else "red"}))

map.add_child(fgv)

map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")