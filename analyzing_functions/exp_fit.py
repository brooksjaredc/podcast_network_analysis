import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors as colors
import matplotlib.cm as cmx
import pandas as pd


measures = pd.read_csv('evolution_of_measures.csv', sep='\t', index_col=0)

# plt.plot(measures['day_num'].values(), measures['num_people'].values(), label='Data')
# plt.scatter(measures['day_num'], 6.13534785e+02*np.exp(9.86796867e-04*measures['day_num']), color='Firebrick', label='Model Fit')
# print(measures['num_people'].values)
# print(type(measures['day_num'].values[0]))
x=measures['num_people'].values[:85]
# print(x[84], type(x[84]))
print(x)
plt.plot(x,x, label=r'10^{4}')

plt.xlabel('Days')
plt.ylabel('Number of People')

# plt.xscale('log')
# plt.yscale('log')

# plt.xlim([0.9,1200])
# plt.ylim([1e-5,1])

plt.legend()

plt.gcf()
plt.draw()
# plt.savefig('plots/auths_evol_top_ten.pdf',format='pdf')
plt.show()

