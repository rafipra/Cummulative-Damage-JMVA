#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:39:47 2017

@author: jmaidana
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn
seaborn.set(style='ticks')
#### p = 5-1 
data = np.loadtxt('Results/seed_2802_lRn_all_p_0.2_Rep_10000.txt')
limite = stats.chi2.ppf(0.95,(4-1))

##
fig, ax10 = plt.subplots(figsize=(8,6))
##
## This is the figure A
fig = plt.figure(figsize=(9,7), facecolor="white")
ax1 = fig.add_subplot(111, projection='3d')
#plt.suptitle('Histograms of $-2\log(\mathscr{R}_n)$ for different values of n',fontsize=26)
colores = plt.cm.Greys
yticks = [0, 1, 2, 3, 4, 5, 6, 7]
lj=0
for k in yticks:
#    ys,xs = np.histogram(data[lj],range=(0,26),bins=27)
#    ax.bar(xs[1:], ys, zs=k, zdir='y', color=colores(10+k*25))
    n, bins, patches = ax10.hist(data[lj],range=(0,26),bins=27,normed=1)
    ax1.bar(bins[1:],n,zs=k,zdir='y',color='white',lw=0.5,edgecolor='black')
    lj+=1
ax1.view_init(elev=30., azim=335)
ax1.set_yticklabels(['16', '32', '64', '128', '256', '512', '1024', '2048'])
ax1.set_xlabel('$-2\log(\mathscr{R}_n)$')
ax1.set_ylabel('$n$')
ax1.set_zlabel('density')
ax1.plot([limite,limite],[-0.1,7],'-',color='black',lw=1)
ax1.set_ylim(0,7)
ax1.set_xlim(0,26)
ax1.w_xaxis.set_pane_color((1.0,1.0,1.0,1.0))
ax1.w_yaxis.set_pane_color((1.0,1.0,1.0,1.0))
ax1.w_zaxis.set_pane_color((1.0,1.0,1.0,1.0))
#seaborn.despine(ax=ax1, offset=10, trim=True)
#ax1.xaxis.get_ticklines() # the majors
#ax1.xaxis.get_ticklines(minor=True) # the minors
#ax1.xaxis.get_minorticklines()

#plt.savefig('3dplot_p4_v2.eps',dpi=450)
#plt.savefig('3dplot_p4_v2.pdf',dpi=450)

plt.show()
#%%

## This is the figure B
#plt.clf()
fig, ax2 = plt.subplots(figsize=(9,7), facecolor="white")
ax2.hist(data[7],range=(0,26),bins=27, color='white',normed=True,lw=0.5,edgecolor='black')#, alpha=0.8)
df=3
x = np.linspace(stats.chi2.ppf(1e-10, df),stats.chi2.ppf(1.-1e-4, df), 1000)
rv = stats.chi2(3)
ax2.set_ylabel('density')
ax2.set_xlabel('$-2\log(\mathscr{R}_n)$')
ax2.plot(x,rv.pdf(x),'--',color='black',lw=2)
seaborn.despine(ax=ax2, offset=5, trim=True)
#ax2.xaxis.get_ticklines() # the majors
#ax2.xaxis.get_ticklines(minor=True) # the minors
#ax2.xaxis.get_minorticklines()
#plt.savefig('histplot_p4_v2.eps',dpi=450)
#plt.savefig('histplot_p4_v2.pdf',dpi=450)

plt.show()