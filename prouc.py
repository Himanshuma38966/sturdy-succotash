import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import statistics 
import csv

df =pd.read_csv("https://raw.githubusercontent.com/whitehatjr/Sampling-distribution/master/data.csv")
data = df["temp"].tolist()


raw_mean=statistics.mean(data)
print(raw_mean)
raw_sd = statistics.stdev(data)

print(raw_sd)


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig = ff.create_distplot([df],["temprature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))

    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of sampling Distribution",mean)
    sd=statistics.stdev(mean_list)
    print("sampling distribution Standard deveation",sd)

setup()
