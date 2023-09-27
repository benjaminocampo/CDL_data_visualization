import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.4) #pip install plotly==4.5.4
import plotly.express as px
import plotly.io as pio

# excel sheet from https://www.kaggle.com/rajanand/prison-in-india/data
# National Crime Records Bureau (NCRB), Govt of India has shared this dataset
df = pd.read_csv("Caste.csv")
df = df[df['state_name']=='Maharashtra']
df = df.groupby(['year','gender',],as_index=False)[['detenues','under_trial','convicts','others']].sum()
print (df[:5])

#fake margin of error, standard deviation, or 95% confidence interval
# df['err_plus'] = df['convicts']/100
# df['err_minus'] = df['convicts']/40

import pdb; pdb.set_trace()

barchart = px.bar(
    data_frame=df,
    x="year",
    y="convicts",
    color="gender",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="v",              # 'v','h': orientation of the marks
    barmode='group',           # in 'overlay' mode, bars are top of one another.
                                  # in 'group' mode, bars are placed beside each other.
                                  # in 'relative' mode, bars are stacked above (+) or below (-) zero.
    #----------------------------------------------------------------------------------------------
    # color_discrete_sequence=["pink","yellow"],               # set specific marker colors. Color-colum data cannot be numeric
    # color_discrete_map={"Male": "gray" ,"Female":"red"},     # map your chosen colors
    # text='convicts',            # values appear in figure as text labels
    hover_name='under_trial',   # values appear in bold in the hover tooltip
    # hover_data=['detenues'],    # values appear as extra data in the hover tooltip

    # log_x=True,                 # x-axis is log-scaled
    # log_y=True,                 # y-axis is log-scaled

    labels={"convicts":"Convicts in Maharashtra",
    "gender":"Gender"},           # map the labels of the figure
    title='Indian Prison Statistics', # figure title
    width=1400,                   # figure width in pixels
    height=720,                   # figure height in pixels
    template='gridon',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'

    # # range_x=[5,50],           # set range of x-axis
    range_y=[0,9000],           # set range of x-axis
)

# barchart.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
# barchart.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
# 
# barchart.update_layout(uniformtext_minsize=14, uniformtext_mode='hide',
#                        legend={'x':0,'y':1.0}),
# barchart.update_traces(texttemplate='%{text:.2s}', textposition='outside',
#                        width=[.3,.3,.3,.3,.3,.3,.6,.3,.3,.3,.3,.3,.3])
# 

pio.show(barchart)
