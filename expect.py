import csv
import matplotlib.pyplot as plt
import numpy as np

def worst_county(year, path):
    with open(path, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')

        myDict = {}
        for row in csvreader:
            if row["Year"] == str(year):
                myDict[row["County"]] = (float(row["Female life expectancy (years)"])+float(row["Male life expectancy (years)"]))/2
                myMin = min(myDict, key=myDict.get)
                if row["County"] == str(myMin):
                    state = row["State"]
        return state, myMin

def plotdata(state,county, filename):
    fig, ax = plt.subplots()
    xs = []
    for i in range(1985, 2011):
        xs.append(i)
    FY = []
    FS = []
    FC = []
    MY = []
    MS = []
    MC = []
    
    with open(filename, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')

        for row in csvreader:
            if row["State"] == str(state) and row["County"] == str(county):
                FY.append(row["Female life expectancy (years)"])
                FS.append(row["Female life expectancy (national, years)"])
                FC.append(row["Female life expectancy (state, years)"])
                MY.append(row["Male life expectancy (years)"])
                MS.append(row["Male life expectancy (national, years)"])
                MC.append(row["Male life expectancy (state, years)"])


    plt.plot(xs, FY)
    plt.plot(xs, FS)
    plt.plot(xs, FC)
    plt.plot(xs, MY)
    plt.plot(xs, MS)
    plt.plot(xs, MC)

    plt.show()
    return (state)

if __name__ == "__main__":
    filename = "Assignment50/data.csv"
    state,county = worst_county(2005, filename)
    plotdata(state,county, filename)