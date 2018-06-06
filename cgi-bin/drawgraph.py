#!/usr/bin/env python
import plotly
plotly.__version__
#import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import time
import numpy as np
import pandas as pd
import cgi
import urllib2

form = cgi.FieldStorage()
daterequested = form.getvalue("daterequested")
requireddate = daterequested.translate(None, '-')
csvurl = "http://192.168.1.151/csv/waterlevel-{}.csv".format(requireddate)

def file_exists(location):
    request = urllib2.Request(location)
    request.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(request)
        return True
    except urllib2.HTTPError:
        return False

if file_exists(csvurl):
	df = pd.read_csv(csvurl,header=0,names=('TimeMeasured','WaterLevel'))
	trace = go.Scatter(x = df['TimeMeasured'], y = df['WaterLevel'],
		name='Sump Water Level (in inches)') 
	layout = go.Layout(title='Playroom Sump Pump Level',
					plot_bgcolor='rgb(230, 230,230)',
					showlegend=True) 
	fig = go.Figure(data=[trace], layout=layout) 

	requestedchart = plotly.offline.plot(fig, output_type='div')
#print(requestedchart)
	print("Content-Type: text/html\n\n")

	chart = requestedchart

	htmlFormat = """
	<html>
	<Title>Sump Basin Water Levels For {requireddate}</Title>
	<body>
	<p>{chart}</p>
	</body>
	</html> """

	print(htmlFormat.format(**locals()))

else:
	print "Content-type:    text/html\r" 
	print "Location:        ../nodataerror.html\r\n\r" 
	


exit()
