import pandas
from bokeh.plotting import figure, output_file, show
df=pandas.read_csv("adbe.csv", parse_dates=["Date"])

p=figure(plot_width=500, plot_height=250, x_axis_type="datetime",sizing_mode="stretch_both")

p.line(df["Date"],df["Close"],color="blue",alpha=0.5)

output_file("timeseries.html")
show(p)