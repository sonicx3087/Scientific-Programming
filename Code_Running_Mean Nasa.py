


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading both columns from the CSV file

#nasa_df = pd.read_csv('graph.csv', sep=',', header=None, skiprows=2, encoding='latin1')
nasa_df = pd.read_csv('graph.csv', sep=',', header=None, skiprows=2)

# Displaying the data
#print(nasa_df)



# Get years and temperature anomalies
years = nasa_df[0].values #years contrains all the values in the first column
noSmoothing = nasa_df[1].values #smoothing contains all the values in the second column
lowess = nasa_df[2].values



# Compute 5-year running mean
running_mean = np.zeros(len(noSmoothing))  # Initialize an array for storing the running mean. Stores a bunch of zeros
i = 2 # Define the window size
 # Initialize the counter



while i < len(noSmoothing) - 2:#Condtion for while my counter is less then the length of the array - 2. Since we don't want the last two
    running_mean[i] = (noSmoothing[i]+noSmoothing[i+1]+noSmoothing[i+2]+noSmoothing[i-1]+noSmoothing[i-2])/5 #This computes the running means
    i = i +1

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.xlabel("Years")
plt.ylabel("Temperature Anomaly Celsius")
plt.title("Land-Ocean: Southern Hemispheric Means")

# Plots the original data with label
plt.plot(years, noSmoothing, label="No Smoothing")

# Plots the 5-year running mean data with label
plt.plot(years[2:-2], running_mean[2:-2], label="5-Year Running Mean")

# Plots the lowess smoothed data with label
plt.plot(years, lowess, label="Lowess Smoothed")

# Display legend
plt.legend()

plt.show()



