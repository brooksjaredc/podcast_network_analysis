import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors as colors
import matplotlib.cm as cmx
import pandas as pd
#import seaborn as sns
from datetime import datetime as dt

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

df = pd.read_csv('evolution_of_measures.csv', sep = '\t', header=0, index_col=0)

#print(list(df.columns.values))

dates = df['dates'].values
dates = [(dt.strptime(x, '%Y-%m-%d')) for x in dates]

#f = plt.figure(figsize=(8,6))
f = plt.figure()
ax = f.add_subplot(111)

#print(sns.color_palette("Set2", 10))
# NCURVES = 10
# np.random.seed(101)
# curves = [np.random.random(20) for i in range(NCURVES)]
# values = range(NCURVES)

# jet = cm = plt.get_cmap('jet') 
# cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
# scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

# i=0
# for col in df.columns:
# 	if(col != 'dates'):
# 		ax.plot(dates,df[col],color=scalarMap.to_rgba(values[i]),linestyle='solid',linewidth=1,label=col)
# 	i+=1

ax.plot(dates,df['avg_path'])

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)


ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
f.autofmt_xdate()

ax.set_xlabel(r'date')
ax.set_ylabel(r'Average Path Length')

#legend = plt.legend(fancybox=True, loc='lower right',labelspacing=0, framealpha=0.8)

plt.gcf()
plt.draw()
plt.savefig('plots/avg_path_evol.pdf',format='pdf')
plt.show()

