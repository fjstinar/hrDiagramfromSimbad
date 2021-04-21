import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#system arguments - the one will be the filename of the database



df = pd.read_csv(sys.argv[1])
df = df.iloc[1:]

magB = df['B ( mag )']
magV = df['V ( mag )']

magB = magB[:-1]
magV = magV[:-1]

magB = list(map(float, magB))
magV = list(map(float, magV))

magB = np.array(magB)
magV = np.array(magV)

plt.plot((magB - magV), magV, 'bo')
plt.xlabel('Temp')
plt.ylabel('Luminosity')
plt.title('H-R Diagram')
figName = 'HRDiagram' + sys.argv[1] + '.png'
plt.savefig(figName, bbox_inches = 'tight')
