# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import matplotlib.pyplot as plt

# to clean the .txt file by getting rid of experiment information.
txtRead = open('cannelle.txt')
a = txtRead.read()
txtRead.close()
b = a.split('\n\n')[-1]
b = b.replace(',','.')
print(b,  file=open('dummy.txt', 'w'))

# to get the raw data from cleaned .txt file
data = pd.read_csv('dummy.txt', sep='\t')
data = data.drop(columns = [data.columns[-1]])

for k in range(0,len(data.columns),2):
    data.iloc[:,k] = -0.000014*data.iloc[:,k]**2 + 2.0117*data.iloc[:,k] - 1248.8670

# to plot visible range [from -850 nm to 1500 nm]
for i in range(4,len(data.columns),2):
    plt.plot(data.iloc[200:1400,i], data.iloc[200:1400,i+1], label=data.columns[i].split(' (')[0])
plt.legend(loc='upper left', frameon=True); plt.xlabel('Wavelength (nm)'); plt.ylabel('Absorbance [AU]')
plt.savefig('cannelle.png', format='png')
plt.show()