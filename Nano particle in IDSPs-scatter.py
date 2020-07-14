# -*- coding: utf-8 -*-
"""
plot nano particle size distribution in the IDSPs: scatter

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
#or
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
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171221-AM'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171221-PM'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-AM1'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-AM2'))
#data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-PM1'))
data=pd.DataFrame(pd.read_excel(xlsfile, sheet_name=u'20171222-PM2'))
#######################################################################################
GMDdata=data['GMD'].astype('float64')
TNdata=data['TN'].astype('float64')
Zdata=data.iloc[:,1:13]#Zdata=data.loc['11.5':'273.8']#both the start and the stop are included
Zdata.astype('float64')
Z=Zdata.values
GMD=GMDdata.values
TN=	TNdata.values
plt.rcParams['axes.unicode_minus']=False 
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Times New Roman'#
fig = plt.figure(figsize=(12,8))                                                               
ax = fig.add_subplot(111)
plt.scatter(GMD, TN, s=200, c='r', alpha=0.5)                                                                                     
plt.tick_params(labelsize=24)
plt.ylabel('Total Number Concentration (#/'+'$cm^{3}$'+')', fontsize=24)
plt.xlabel('Geometric Mean Diameter (nm)', fontsize=24)
#############################################################################
#titleStr='TN versus GMD, 2017-12-19 in an urban site'
#titleStr='TN versus GMD, 2017-12-21 in a road site'
#titleStr='TN versus GMD, Flight-1 in 2017-12-21 AM'
#titleStr='TN versus GMD, Flight-2 in 2017-12-21 PM'
#titleStr='TN versus GMD, Flight-3 in 2017-12-22 AM'
#titleStr='TN versus GMD, Flight-4 in 2017-12-22 AM'
#titleStr='TN versus GMD, Flight-5 in 2017-12-22 PM'
titleStr='TN versus GMD, Flight-6 in 2017-12-22 PM'
##############################################################################
#plt.tight_layout()
filename=titleStr
plt.title(str(filename), fontsize=28)
plt.savefig(str(filename)+'.png')
plt.clf()

print("ALL -> Finished OK")
