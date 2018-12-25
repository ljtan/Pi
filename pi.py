#Pi Generator 
#Author: Jason Tan 
#Created: 03/22/2016

from __future__ import division
import math
import csv
import plotly.graph_objs as go
import plotly.offline as py
from plotly.graph_objs import Scatter


X = []
PI1 = []
PI2 = []
PI3 = []

def pi1(lim):
    sum1=sum(((-1)**(n))/((2*n)+1) for n in range (0,lim))
    pi=sum1*4
    return(pi)

def pi2(lim):
    sum1=sum(1/(n**2) for n in range (1,lim))
    sum1=sum1*6
    pi=math.sqrt(sum1)
    return(pi)

def pi3(lim):
    return(3.14159265358979323)

def write_csv():    
    csv_file=open('pi.csv','w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    wr.writerow(['X', 'PI1', 'PI2', 'PI3'])
    for x in range (1,251):
        wr.writerow([x, pi1(x), pi2(x), pi3(x)])

def read_csv():
    csv_file=open('pi.csv','r')
    dictionary = csv.DictReader(csv_file)

    for row in dictionary:
	X.append(row['X'])
	PI1.append(row['PI1'])
	PI2.append(row['PI2'])
	PI3.append(row['PI3'])

def graph_csv():
    
    trace1= go.Scatter(
        x=X,
        y=PI1,
        name = 'PI1'
    )
    trace2= go.Scatter(
        x=X,
        y=PI2,
        name = 'PI2'
    )
    trace3= go.Scatter(
        x=X,
        y=PI3,
        name = 'PI3'
    )
    data = [trace1, trace2, trace3]
    plot_url = py.plot(data, filename='Pi Graph')
    
    
write_csv()
read_csv()
graph_csv()
