import seaborn as sns
import os, sys
import numpy as np
import matplotlib.pyplot as pl
input=sys.argv[1]
output=sys.argv[2]
with open(input,'r') as fd:
  d = fd.read().splitlines()
fd.close
dd = [float(i)  for i in d]
sns.set_style('darkgrid')
ddd = np.asarray(dd)
print (ddd.shape)

#sns_plot=sns.distplot(ddd,kde=True,norm_hist=True)
#fig = sns_plot.get_figure()
#fig.savefig(output)

aa = pl.hist(ddd, bins='auto')
pl.savefig(output)
