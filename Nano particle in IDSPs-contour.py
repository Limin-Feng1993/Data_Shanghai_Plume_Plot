# -*- coding: utf-8 -*-
"""
Plot nano particle size distribution in the IDSPs: contour

@author: Limin Feng 

Email: fenglimin1993@gmail.com

Project address: https://github.com/Limin-Feng1993

Blog: https://limin-feng1993.github.io/
"""
#################import tools#################################################
import matplotlib
from matplotlib.font_manager import FontProperties
import numpy
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
from matplotlib.ticker import MultipleLocator
import pandas as pd
import datetime
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateLocator, DateFormatter
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import math
from matplotlib.ticker import FuncFormatter
import matplotlib as mpl
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from math import sqrt
#####################################################################################
def TS(x):
	return (x - np.datetime64('1970-01-01T00:00:00Z'))/np.timedelta64(1, 's')
	#return datetime.utcfromtimestamp(x.astype('O')/1e9)
	#return datetime.fromtimestamp(x.tolist()/1e9)
def DT(x):
	return datetime.utcfromtimestamp(x)

def labeller(x, pos):
	if x < 1:
		return '0.'+'0'*(abs(int(np.log10(x)))-1)+\
				format(x/10**(np.floor(np.log10(x))),'.0f')
	else:
		return format(x,'.0f')
#############################################load data##################################################
xlsfile='data.xlsx'
Ydata=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'Size'))
Ydata=Ydata['size'].astype('float64')
Y=Ydata.values
########################################################################################
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171219-urban'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171221-highway'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171221-upper air'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-AM1'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-AM2'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-PM1'))
data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-PM2'))
#######################################################################################
Xdata=data['Date Time']
Xdata=pd.to_datetime(Xdata, unit='s')
Xdata=Xdata.values
Xdata.astype(datetime)
X=[DT(TS(i)) for i in Xdata]
print(X)
GMDdata=data['GMD'].astype('float64')
TNdata=data['TN'].astype('float64')
Zdata=data.ix[:,1:13]#Zdata=data.loc['11.5':'273.8']#both the start and the stop are included
print(Zdata)
Zdata.astype('float64')
Z=Zdata.values
GMD=GMDdata.values
TN=	TNdata.values
################################################################################
#minval, maxval=0, 1400
#minval, maxval=0, 10000
#minval, maxval=0, 1000
#minval, maxval=0, 8000
#minval, maxval=0, 12000
#minval, maxval=0, 4000
minval, maxval=0, 10000
##################################################################################
ZT=Z.T
ZT=np.where(ZT>maxval, maxval-1, ZT)
ZT=np.where(ZT<minval, minval+1, ZT)
plt.rcParams['axes.unicode_minus']=False 
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Times New Roman'#
fig = plt.figure(figsize=(12,8))                                                               
ax = fig.add_subplot(111)
x, y= np.meshgrid(X, Y)
cs = plt.contourf(x, y, ZT, np.arange(minval, maxval, 1),cmap=plt.cm.get_cmap('jet'))
#plt.plot(X[::5], GMD[::5], 'y*-', linewidth=8.0, label='GMD')
plt.plot(X, GMD, 'y*-', linewidth=8.0, label='GMD')
plt.legend(loc='upper center', bbox_to_anchor=(0.8, 1.1), frameon=False, ncol=1, fontsize=28)                                                                                       
plt.gca()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  
plt.tick_params(labelsize=24)
cs.ax.tick_params(labelsize=24)
ax.set_yscale('log')
custom_formatter = FuncFormatter(labeller)
ax.yaxis.set_major_formatter(custom_formatter)
dmt= [10,50,100,200]
plt.gca().set_yticks(dmt)
plt.gca().set_yticklabels(dmt)
plt.ylim(11.5, 273.8)
plt.ylabel('Mobility Diameter (nm) ', fontsize=24)
cbar = plt.colorbar(cs)
cbar.ax.tick_params(labelsize=18)
#cbar.set_label('Mass Concentration ('+r'$PM_2.5$'+'g/'+'$m^{3}$'+')', fontsize=24)
cbar.set_label('Number Concentration (#/'+'$cm^{3}$'+')', fontsize=24)
#############################################################################
#cbar.set_ticks(np.linspace(0, 1400, 8))
#cbar.set_ticks(np.linspace(0, 10000, 6))
#cbar.set_ticks(np.linspace(0, 1000, 6))
#cbar.set_ticks(np.linspace(0, 8000, 5))
#cbar.set_ticks(np.linspace(0, 12000, 7))
#cbar.set_ticks(np.linspace(0, 4000, 5))
cbar.set_ticks(np.linspace(0, 10000, 6))

#titleStr='2017-12-19 in an urban site'
#titleStr='2017-12-21 in a road site'
#titleStr='Flight-1 in 2017-12-21 PM'
#titleStr='Flight-1 in 2017-12-22 AM'
#titleStr='Flight-2 in 2017-12-22 AM'
#titleStr='Flight-3 in 2017-12-22 PM'
titleStr='Flight-2 in 2017-12-22 PM'
##############################################################################
plt.tight_layout()
filename=titleStr
plt.title(str(filename), loc='left', fontsize=28)
plt.savefig(str(filename)+'.png')
plt.clf()
print("ALL -> Finished OK")




