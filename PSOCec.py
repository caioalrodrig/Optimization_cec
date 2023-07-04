import numpy as np
import matplotlib.pyplot as plt
import cec2017.functions as cec
import statistics as st
import random
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import main

class PSO_run():
    ''' Arguments: iterations, LEN_PART, u_bound, l_bound, D (dimension)'''
    def __init__(self, **kwargs ):
        self.iterations = kwargs.get('iterations')
        self.n_particles = kwargs.get('LEN_PART')
        self.l_bound = kwargs.get('u_bound')
        self.u_bound = kwargs.get('l_bound')
        self.n_dimensions = kwargs.get('D')
        self.bounds = (self.l_bound, self.u_bound)

        self.options = {'c1': 2, 'c2': 2, 'w': 0.9}
        initial_position = np.random.uniform(self.l_bound, self.u_bound, (self.n_particles, self.n_dimensions))
        
    def objective_function(self, x):
        results = []
        for i in range(x.shape[0]):
            result = cec.f4([x[i]])[0]
            results.append(result)
        return results


if __name__ == '__main__':
    D = 10   
    u = 100
    l = -100
    N_independ_exec = 51
    obj = main.Heuristic(D)
    print(obj.LEN_POP)
    pso = PSO_run(D = D, iterations = obj.SOL_PER_EXEC, LEN_PART = obj.LEN_POP, u_bound = u , l_bound= l )
    pso_objective = pso.objective_function
    best_fitnesses = []
        
    # for i in range(N_independ_exec):
    # Executar o algoritmo PSO
    optimizer = ps.single.GlobalBestPSO(n_particles= 45, dimensions= D, options={'c1': 0.5, 'c2': 0.5, 'w': 0.9}, bounds= (-100*np.ones(D),100*np.ones(D)))
    cost, pos = optimizer.optimize(pso_objective, iters = 90  , verbose = False)
    best_fitnesses.append(cost)

'''Resultados'''
plt.plot(best_fitnesses)
print(best_fitnesses)
print("Best: {} ".format(min(best_fitnesses)))
print("Worst: {} ".format(max(best_fitnesses)))
print("Std: {}".format(st.stdev(best_fitnesses)))
print("Mediana: {}".format(st.median((best_fitnesses))))
print("Media: {}".format(st.mean(best_fitnesses)))
