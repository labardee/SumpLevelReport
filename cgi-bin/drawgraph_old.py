#!/usr/bin/env python
import plotly
plotly.__version__
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import time
import numpy as np
import pandas as pd
#from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("requireddate", help="The date you are requesting data from, specfied YYYYMMDD")
args = parser.parse_args()
requireddate = args.requireddate.translate(None, '-')
csvurl = "http://192.168.1.151/csv/waterlevel-{}.csv".format(requireddate)

df = pd.read_csv(csvurl,header=0,names=('TimeMeasured','WaterLevel'))
trace = go.Scatter(x = df['TimeMeasured'], y = df['WaterLevel'],
     name='Sump Water Level (in inches)')
layout = go.Layout(title='Playroom Sump Pump Level',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

outfilename = "./{}-graph.html".format(requireddate)

plotly.offline.plot(fig, filename=outfilename)
print "Script ran successfully file: {} created" .format(outfilename)
exit()
