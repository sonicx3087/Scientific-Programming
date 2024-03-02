import pandas as pd
import numpy as np#import statements
import matplotlib.pyplot as plt

data = pd.read_csv('graph.txt', skiprows=9, delim_whitespace=True, header=None).values

year = data[:,0] #store years columns
glob = data[:,1] #stores global tempatures celcius
Nhem = data[:,2] #store northern hemispheres data
Shem = data[:,3] #stores soutern hemisphere data
zone = data[:,5] #stores equilateral zones



fig1 = plt.figure(figsize=[9,18])  #This increases the size of the figure

# Create subplots with adjusted spacing
#The 9, 1 here represents:Grid paper looks like. 9 rows and 1 column. 0,0 represents: Row 0 column 0. X is the row and Y is the column
ax1 = plt.subplot2grid((9, 1), (0, 0), rowspan=2)  # Span first two rows. rowspan = 2 simply makes the plot better
plt.setp(ax1.get_xticklabels(), visible=False) #Visible = False is Surpressing the x axis

ax2 = plt.subplot2grid((9, 1), (2, 0), rowspan=2)  # Span rows 2 and 3
plt.setp(ax2.get_xticklabels(), visible=False)

ax3 = plt.subplot2grid((9, 1), (4, 0), rowspan=2)  # Span rows 4 and 5
plt.setp(ax3.get_xticklabels(), visible=False)

ax4 = plt.subplot2grid((9, 1), (6, 0), rowspan=2) #No visible=false here because the code looks more clean.


ax1.plot(year, glob, c='g')
ax2.plot(year, Nhem, c='pink')
ax3.plot(year, Shem, c='r')
ax4.plot(year, zone, c=(0.6, 0, 0.6))

ax1.set_title('Temperature anomalies from four zones') #Sets title to fit alll my ladderp lots



ax1.set_ylabel('Global Temps Celsius') #This sets a y label for each ladder plots
ax2.set_ylabel('Nhem Celsius')
ax3.set_ylabel('Shem Celsius')
ax4.set_ylabel('24S-24N Celsius')


ax4.set_xlabel('Years') #Adds an x label only on the foruth ladder plot at the bottom. Which can represent
plt.show()

HEADER = "Year,Global,NHem,SHem, 24S-24N\nThese are temperature  anomalies"
np.savetxt('Columns.csv', data, fmt='%1.2f', delimiter=' ', header=HEADER, comments=' ')
#comments: Represents whether you want a special character on any lines without data





