import numpy as np
import matplotlib.pyplot as plt
import cec2017.functions as cec
import statistics as st
import random
from control.matlab import *

class DeployPso():
    def __init__(self,**kwargs):
        self.N = kwargs.get('particles')
        self.K = kwargs.get('iterations')
        self.D = kwargs.get('Dim') 
        self.l = kwargs.get('lowB') 
        self.u = kwargs.get('upB') 
        self.parameters = {'c1': 0.5, 'c2': 0.5, 'w': 0.9}

        self.s = TransferFunction.s
        self.sys1= (0.54/(1.3*self.s+1),2.5)
        self.sys2= (1/(6.3*self.s+1),0)
        self.sys3= (0.32/(self.s**2+self.s*0.08+0.16),10)


    def startPSO(self):
        '''     Set up algorithm, initialize all dictionaries: x, Gbx and Ibx. Set up velocity[0]. [Return = x, Ibx , Gbx , v]
        '''
        # np.random.seed(24)
        array_pos0 = np.random.uniform(self.l, self.u, (self.N, self.D))
        swarm_pos0 = {}
        for line in range(array_pos0.shape[0]):
            swarm_pos0[line] = array_pos0[line]  
        bestI_0 = []
        v = {}
        X = swarm_pos0.copy()
        Ibx = swarm_pos0.copy()
        for i in range(self.N):
            bestI_0.append(self.objective_function(X[i]))
        Gbx = min(bestI_0)
        Gbx_indv = np.where(bestI_0 == Gbx)[0][0]
        Gbx_indv = Ibx[Gbx_indv]
        for i in range(self.N):
            v[i] = np.zeros(self.D)
        # print(bestI_0)
        return X , Ibx , bestI_0, Gbx , Gbx_indv, v  
        
    def loopPSO(self):
        '''     Run all K PSO iterations 
        '''
        X , Ibx , Ifit , Gbx , G_indv ,v = self.startPSO()
        Gfit = np.zeros(self.K)
        Gindv = np.zeros((self.K,self.D))
        Gindv[0] = G_indv
        Gfit[0] = Gbx.copy()
        for k in range(self.K): 
            for indv in X.keys():
                for d in range(self.D):
                    v[indv][d] = 0.8*v[indv][d] + self.parameters['c1']*(Ibx[indv][d] - X[indv][d]) +  self.parameters['c2']*(Gbx-X[indv][d])
                    X[indv][d] += v[indv][d] 
                    if X[indv][d] > self.u:
                        X[indv][d] = np.random.uniform(self.l, self.u)
                    elif X[indv][d] < self.l:
                        X[indv][d] = np.random.uniform(self.l,self.u)   
                # print(X[indv])
                fit = self.objective_function(X[indv])
                if fit < Ifit[indv]:
                    Ifit[indv] = fit
                    Ibx[indv] = X[indv].copy()
            aux = min(Ifit)
            if aux < Gbx :
                Gbx = aux.copy()
                Gfit[k] = Gbx.copy()
                Gindv[k] = np.array(X[indv])  
            else:
                if k > 0:
                    Gfit[k] = Gfit[k-1].copy()
                    Gindv[k]=Gindv[k-1].copy()     
        G_best = min(Gfit)
        P_best = Gindv[np.where(Gfit == G_best)[0][0]]
        # plt.plot(Gfit)
        # plt.show(block=False)
        return {'best_fitness' : G_best , 'best_indv': P_best}      
                
    def objective_function(self, indv):
        return cec.f4([indv])[0]
            
    def objctv_function_Sys(self, K , T , Delay):
        
        Ytst, Xtst= step(feedback(self.sys1[0]))
        Gfit = K/(self.s*T+1)
        Xfit = Xtst.copy() 
        Yfit, Xfit = step(feedback(Gfit), Xfit)
        Xtst += self.sys1[1]
        Xfit += Delay

        quad_err = np.square(Ytst - Yfit)
        rmse = np.sqrt(np.mean(quad_err))
        return rmse


if __name__ == '__main__':
    psoInstance = DeployPso(particles = 44 , iterations = 44 , lowB = -100 , upB = 100 , Dim = 10)
    bests = []
    for i in range(51):
        b = psoInstance.loopPSO()
        print(b['best_fitness'],b['best_indv'])
        psoInstance.objctv_function_Sys(0.54,3,2.5)
        bests.append(b['best_fitness'])
    plt.plot(bests)
    plt.show()