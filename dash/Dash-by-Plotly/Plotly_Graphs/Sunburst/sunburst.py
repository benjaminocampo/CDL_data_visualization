import plotly.express as px
import pandas as pd
import numpy as np

# https://mappingpoliceviolence.org/
df = pd.read_csv("MPVDataset.csv")
df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors='coerce').fillna(0).astype(np.int64)
df.rename(columns={'Fleeing (Source: WaPo)': 'Fleeing'}, inplace=True)

df = df[df["State"].isin(['NY', 'CA', 'TX'])]
df = df[df["Victim's race"].isin(["White", "Black", "Hispanic", "Asian"])]

import pdb; pdb.set_trace()

fig = px.sunburst(
    data_frame=df,
    path=["Fleeing", 'State', "Victim's race"],  # Root, branches, leaves
    color="Fleeing",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth=2,                        # set the sectors rendered. -1 will render all levels in the hierarchy
    # color="Victim's age",
    # color_continuous_scale=px.colors.sequential.BuGn,
    # range_color=[10,100],

    branchvalues="total",               # or 'remainder'
    hover_name="Unarmed",
    # # hover_data={'Unarmed': False},    # remove column name from tooltip  (Plotly version >= 4.8.0)
    # template='ggplot2',               # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
    #                                   # 'plotly_white', 'plotly_dark', 'presentation',
    #                                   # 'xgridoff', 'ygridoff', 'gridon', 'none'
)

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()
