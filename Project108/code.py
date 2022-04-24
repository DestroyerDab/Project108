import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("project108data.csv")
avg_rating = df["Avg Rating"].tolist()
fig = ff.create_distplot([avg_rating], ["Average"], show_hist=True)
fig.show()