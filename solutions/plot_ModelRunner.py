"""
Use the ModelRunner to generate Arrhenius plot
"""

#read the output and get T and TOF
try:
    with open('ScanKinetics.dat') as infile:
        lines = infile.readlines()
except:
    print('ScanKinetics.dat is missing!'); import sys;sys.exit()

iT = 0; iTOF = 3 # columns for each variable
results = []
for thisline in lines:
    if thisline[0] != '#':
        values = thisline.strip().split(' ')
        info = {'T_inv':1/float(values[iT]), 'TOF':float(values[iTOF])}
        results.append(info)

#sort the results
sorted_results = sorted(results, key=lambda x: (x['T_inv']))

# ... and then plot
import matplotlib.pyplot as plt
import numpy as np
plt.plot([x['T_inv'] for x in sorted_results], np.log10([x['TOF'] for x in sorted_results]), '-o')
plt.xlabel('1/T [1/K]')
plt.ylabel('log(TOF [events (sites s)^-1])')
plt.savefig('arrhenius_ModelRunner.pdf') # Optionally, save plot
plt.show()
