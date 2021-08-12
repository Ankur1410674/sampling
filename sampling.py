import random
import pandas as pd
import typing as counter 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st 
import csv

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def randomsetoffmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
def show_fig(meanlist):
    df = meanlist
    mean = st.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setoffmeans=randomsetoffmean(100)
        meanlist.append(setoffmeans)
    show_fig(meanlist)
setup()        
        
