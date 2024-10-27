'''This file reads a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

import zipfile
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


with zipfile.ZipFile('Crime_Data_from_2020_to_Present.csv.zip') as z:
    with z.open("Crime_Data_from_2020_to_Present.csv") as f:
        df = pd.read_csv(f)

df['TimeOccHr'] = df['TIME OCC']//100 + df['TIME OCC']%100/60

## Show summary statistics of the dataframe.
display(df.describe())

# Distribution of Crome Occcurence over Time of Occurence
plt.figure(figsize = (15,6))
h = (df['TimeOccHr']).hist(bins = 24)
h.set(xlabel = "Hour of Day", ylabel = "Crime Occurences",
      title = "Distribution of Crime Occurences over Time of Day")
plt.xticks(ticks = [2*i for i in range(13)])


# Create a geographical plot to capture LAPD Crime Rate by LAT and LON
df_graph = df[df['LAT'] != 0].groupby(['AREA NAME', 'LAT', 'LON']).count()[['DR_NO']].reset_index()

df_graph.dropna(
    axis=0,
    how='any',
    subset=None,
    inplace=True
)

color_scale = [(0, 'pink'), (1,'red')]

fig = px.scatter_mapbox(df_graph,
                        lat="LAT",
                        lon="LON",
                        color="DR_NO",
                        color_continuous_scale=color_scale,
                        hover_name="AREA NAME",
                        hover_data=["AREA NAME"],
                        size="DR_NO",
                        zoom=10,
                        height=800,
                        width=800,
                        )

fig.update_layout(mapbox_style="carto-positron") #open-street-map
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# Create a Histogram of Victim Age
plt.figure(figsize = (15, 5))
p = df[df['Vict Age'] > 0]['Vict Age'].hist(bins = 16)
p.set(xlabel = 'Victim Age', ylabel = 'Number of Victims',
      title = "Distribution of Victim Ages in LAPD")
plt.xticks(ticks = [10*i for i in range(0,13)])
plt.xlim(0,120)

fig.show()
plt.show()
plt.close()
