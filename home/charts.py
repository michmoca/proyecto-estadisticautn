# file charts.py
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from home.views import Descriptiva_InfoView
import tkinter as tk # Python 3
import matplotlib
matplotlib.use('Agg')

sns.set(color_codes=True)
sns.set_style("whitegrid")

def histograma(request):
    lista_p = Descriptiva_InfoView.lista_num
    #print(Descriptiva_InfoView.lista_num)
    lista= lista_p.split(',')
    lista_np = np.array(lista)
    lista_np = lista_np.astype(float)
    fig = plt.figure()

    ax=fig.add_subplot(111)
    ax.hist(lista_np)
    #ax.boxplot(lista_np)
    ax.set_xlabel('Números ingresados')
    ax.set_ylabel('Cantidad de apariciones')

    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def boxplot(request):

    lista_p = Descriptiva_InfoView.lista_num
    #print(Descriptiva_InfoView.lista_num)
    lista= lista_p.split(',')
    lista_np = np.array(lista)
    lista_np = lista_np.astype(float)
    fig = plt.figure()
    ax_box=fig.add_subplot(111)
    sns.boxplot(lista_np, ax=ax_box)
    sns.despine(ax=ax_box, left=True)
    #ax.boxplot(lista_np)

    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/jpg')
    canvas.print_png(response)
    return response

def boxplot_respaldo(request):

    lista_p = Descriptiva_InfoView.lista_num
    #print(Descriptiva_InfoView.lista_num)
    lista= lista_p.split(',')
    lista_np = np.array(lista)
    lista_np = lista_np.astype(float)
    fig = plt.figure()
    ax=fig.add_subplot(111)
    ax.boxplot(lista_np)

    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/jpg')
    canvas.print_png(response)
    return response

def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response