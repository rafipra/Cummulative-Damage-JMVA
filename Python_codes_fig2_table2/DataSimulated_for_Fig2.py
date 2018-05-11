#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:50:24 2017

@author: jmaidana
"""
from __future__ import division
import numpy as np
from scipy import stats

def cuenta_distintos(avec,bvec,Ns):
    distintos = (1./(Ns+1))*avec<=bvec
    if len(np.where(distintos==False)[0])==len(avec):
        return True
    else:
        return False

def indice_distinto(sumaW,bvec,Ns):
    indices = []
    for i in range(len(bvec)):
        indices.append(np.min(np.where(sumaW[:,i]>Ns*bvec[i])[0]))
    return np.array(indices)

def choose_p(vecP,Nvals):
    cusumP = np.cumsum(vecP)
    cusumP = np.insert(cusumP,0,0)
    indices = []
    for i in range(Nvals):
        unif = np.random.rand()
        indx = np.min(np.where(unif<=cusumP)[0])
        indices.append(indx-1)
    return indices

def make_canonical(indxs,Nelem):
    result = [list(np.array([1.0 if i == indxs[l] else 0.0 for i in range(Nelem)])) for l in range(len(indxs))]
    return np.array(result)    

def Make_Sigma(probs):
    Nprob = len(probs)
    Sig = np.zeros([Nprob,Nprob])
    for i in range(Nprob):
        for j in range(Nprob):
            if i==j:
                Sig[i,j] = probs[i]*(1-probs[i])
            else:
                Sig[i,j] = -probs[i]*probs[j]
    return Sig

def PSI(Sig,mus,vec):
    Nvec=len(vec)
    Psi = np.zeros([Nvec,Nvec])
    for i in range(Nvec):
        for j in range(Nvec):
            Psi[i,j] = (Sig[i,j]*min(vec[i],vec[j]))/(mus[i]*mus[j])
    return np.matrix(np.linalg.inv(Psi))
        
def print_results(thast,Tnsim):
    for i in range(len(thast)):
        print 'theta-ast coord %i= '%(i+1),thast[i],'    ','Tn %i ='%(i+1),Tnsim[i]

def logRn(probabilities,Tnsim,ninterv):
    DimT = len(Tnsim)
    B = np.matrix(np.ones(DimT)).T       
    In = np.identity(DimT)        
    InvPsi = PSI(Make_Sigma(probabilities[:-1]),probabilities[:-1],Tnsim)
    IRP = In - np.dot(np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(B),InvPsi),B)),np.transpose(B)),InvPsi)
    result = ninterv*np.dot(np.dot(np.transpose(Tnsim),np.dot(np.dot(np.transpose(IRP),InvPsi),IRP)),Tnsim)
    return float(result)

def cuenta_rechazos(list_lRn,pdim,perc):
    limite = stats.chi2.ppf(perc,(pdim-1))
    nout = np.where(list_lRn>=limite)[0]
    return len(nout)

###############################################################################
###### p = 5 ##################################################################
entero = 2802 #choose this seed to replicate data showed in figure 6.2
np.random.seed(entero)
p1 = 0.2
p = [p1,p1,p1,p1,p1]    
Nsimvec = [2**i for i in range(4,12)]
Repeat = 10000

rechazos = []
dimp = len(p)-1
wast=0.1*np.ones(dimp)
lRn_all = []
for j in range(len(Nsimvec)):
    print 'empieza la simulacion ',j
    lRnvec = []
    Nsim = Nsimvec[j]
    Tsimula = np.arange(0,10,1./Nsim)
    for l in range(Repeat):
        S = np.transpose(np.array([list(Tsimula) for i in range(dimp)]))
        aux = choose_p(p,S.shape[0])
        vectores = make_canonical(aux,dimp)
        
        flag = True
        contador = 0
        copyvec = vectores.copy()
        copyS = S.copy()
        
        Wt = copyvec[0]
        Wt_sums = [list(vectores[0])]
        St = [list(S[0])] 
        Ssum = copyS[0]
        
        while flag:
            if cuenta_distintos(Wt,wast,Nsim):
                fin = contador
                flag = False
            else:
                contador+=1
                Wt+=copyvec[contador]
                Wt_sums.append(list(Wt.copy()))  
                St.append(list(S[contador]))
                Ssum+=copyS[contador] 
        
        thetaast = [wast[k]/p[k] for k in range(dimp)]
        indices_ = indice_distinto(np.array(Wt_sums),np.array(wast),Nsim)
        Tn =Tsimula[indices_]
        lRn = logRn(p,Tn,Nsim)
        lRnvec.append(lRn)
    lRn_all.append(lRnvec)    
    Nrej=cuenta_rechazos(lRnvec,dimp,0.95)
    rechazos.append(Nrej)

np.savetxt('Results/seed_%s_lRn_all_p_%s_Rep_%s.txt'%(entero,p1,Repeat),lRn_all)
print 'porcentajes de rechazo:', (1./Repeat)*np.array(rechazos)