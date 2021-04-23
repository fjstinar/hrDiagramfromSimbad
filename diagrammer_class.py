#these two imports allow us to format the Simbad data
import pandas as pd
import numpy as np

#this import plots the data for us
import matplotlib.pyplot as plt

#this import allows terminal arguments so that we can pass the database file by name into the script
import sys

#this funcution turns the Simbad database into a dataframe
def createDf(fileName):
    df = pd.read_csv(fileName)
    df = df.iloc[1:]
    return df

#this function calculates magB and magV from the dataframe
def calculateVals(df):
    magB = df['B ( mag )']
    magV = df['V ( mag )']

    magB = magB[:-1]
    magV = magV[:-1]

    magB = list(map(float, magB))
    magV = list(map(float, magV))

    magB = np.array(magB)
    magV = np.array(magV)

    return magB, magV

#this functions creates the HR diagram and saves it to the file (also calculates magB - magV)
def createFig(magB, magV):
    plt.plot((magB - magV), magV, 'bo')
    plt.xlabel('Temp')
    plt.ylabel('Luminosity')
    plt.title('H-R Diagram')
    figName = 'HRDiagram' + sys.argv[1] + '.png'
    plt.savefig(figName, bbox_inches = 'tight')
    print('Hertzsprung-Russell Diagram Created!')

df = createDf(sys.argv[1])
magB, magV = calculateVals(df)
createFig(magB, magV)
