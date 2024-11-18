import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Test read .dat file 
Vo = pd.read_csv('Ch1_Vo_FAN300mA_TMCS1127.dat', delimiter = '\t')
Cr = pd.read_csv('Ch2_LineCurrent_FAN300mA_TMCS1127.dat', delimiter = '\t')

# Export from .dat to .txt file
Vo.to_csv('Vout.txt', index=False)
Cr.to_csv('Cout.txt', index=False)

# Filter data for prepare to plot
Volt = np.loadtxt('Vout.txt')
Curr = np.loadtxt('Cout.txt')
Vsize = np.shape(Volt)
Csize = np.shape(Curr)
print("Size of voltage set : ",Vsize)
print("Size of Current set : ",Csize)

# Define parameter as need to plot
timing = Volt[:,0]
Vline =  Volt[:,1]
Cline =  Curr[:,1]

# Start plot function
plt.figure(1, dpi = 120)
#plt.plot(timing,'b', label = '') 
plt.plot(timing, Vline,'b-',label='Voltage') 
plt.plot(timing, Cline,'r-',label='Current')
plt.legend()
plt.grid()
plt.xlabel('Timing')
plt.ylabel('Current(A), Power(V)')
plt.show()