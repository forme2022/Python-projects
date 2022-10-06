import pandas
from pandas.core import tools
from bokeh.plotting import figure, output_file, show

df=pandas.read_csv("verlegenhuken.csv")
x=df["Temperature"]/10
y=df["Pressure"]/10

f=figure(plot_width=500,plot_height=400,tools="pan, reset")

f.title.text="Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="italic"
f.title.text_font_style="bold"
f.yaxis.minor_tick_line_color="red"
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"

f.circle(x,y,size=0.5)
output_file("weather.html")
show(f)