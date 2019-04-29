import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import datetime
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt


def readData():
    data = pd.read_excel(r'D:\Toegepaste Informatica\2018 - 2019 Semester 2\Data Advanced\pe\voetbal.xlsx')
    return data


def addBirthDate(data):
    for i in range(len(data)):
        data["geboortedatum"][i] = randomDate()


def randomDate():
    month = randint(1, 12)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = randint(1, 31)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = randint(1, 30)
    else:
        day = randint(1, 28)

    return datetime.date(2011, month, day)


def addCategory(data):
    categories = []
    for i in range(len(data)):
        if data["geboortedatum"][i].month >= 1 and data["geboortedatum"][i].month <= 3:
            categories.append(1)
        elif data["geboortedatum"][i].month >= 4 and data["geboortedatum"][i].month <= 6:
            categories.append(2)
        elif data["geboortedatum"][i].month >= 7 and data["geboortedatum"][i].month <= 9:
            categories.append(3)
        else:
            categories.append(4)
    data["categorie"] = categories


def addInzet(data):
    for i in range(len(data)):
        if data["geboortedatum"][i].month >= 1 and data["geboortedatum"][i].month <= 3:
            data["inzet"][i] = "zeer goed"
        elif data["geboortedatum"][i].month >= 4 and data["geboortedatum"][i].month <= 9:
            data["inzet"][i] = "goed"
        else:
            data["inzet"][i] = "matig"


def Opdracht4(data):
    sns.regplot(x=data["gewicht"], y=data["lengte"], fit_reg=False)
    plt.show()


def Opdracht5(data):
    # Positions
    positions = ([i for i in data["positie"].unique()] * 4)
    positions.sort()

    # Goals
    temp = data.groupby(["positie","categorie"]).agg({'aantal gemaakte goalen':'sum'}).reset_index()
    goals = []
    for arr in temp.values : goals.append(arr[2])
    print(goals)

    # Leeftijd
    categorie = ([i for i in data["categorie"].unique()] * 5)

    data2 = DataFrame({
        'positions' : Series(positions),
        'categorie' : Series(categorie),
        'goals' : Series(goals)
    })

    pd.pivot_table(data2, index="positions", columns="categorie", values="goals").plot(kind="bar", stacked=True)
    plt.show()


def Opdracht6(data):
    average = data.groupby(["positie"]).agg({'aantal gemaakte goalen':np.average}).reset_index()
    print(average)

    median = data.groupby(["positie"]).agg({'aantal gemaakte goalen':np.median}).reset_index()
    print(median)


def Opdracht7(data):
    gewichten = data.query("categorie==1")
    print(gewichten["gewicht"].values.std())


# Waarschuwing afzetten
pd.options.mode.chained_assignment = None

# Opdracht 1
data = readData()

# Opdracht 2
addBirthDate(data)
addCategory(data)

# Opdracht 3
addInzet(data)

# Opdracht 4
#Opdracht4(data)

# Opdracht 5
#Opdracht5(data)

# Opdracht 6
#Opdracht6(data)

# Opdracht 7
Opdracht7(data)

# Print
#print(data)