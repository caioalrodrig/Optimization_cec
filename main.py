import pygad
import numpy as np
import matplotlib.pyplot as plt
import cec2017.functions as cec
import statistics as st

class Heuristic():
    """Instantiates the problem budget"""
    def __init__(self, dimension):             
        self.D = dimension
        self.BUDGET = 10000 * self.D

        self.SOL_PER_EXEC = int(self.BUDGET / 51)
        self.LEN_POP =  int(np.sqrt(self.SOL_PER_EXEC))
        self.NUM_GEN = self.LEN_POP

    def cec_func(self,X):
        return cec.f4([X])[0]
    
    def fitness_func(self, ga_instance, solution, solution_idx):
        fitness = 1.0 / (self.cec_func(solution) + 0.0000000001)
        return fitness
    
    def GA(self):
        init_range_low = -100
        init_range_high = 100
        pop_size = (self.LEN_POP ,self.D)

        '''Run 51 times'''
        best_solutions = []
        best_fitnesses = []
        for i in range(51):
            #Initial populacao
            populacao =  np.random.uniform(low=init_range_low, high=init_range_high, size=pop_size)
            # GA module
            num_generations = self.LEN_POP 
            num_parents_mating = int(self.LEN_POP/2)
            mutation_probability = [0.4,0.05] #0.3 
            parent_selection_type = "sss" 
            keep_parents = int(num_parents_mating/2)
            ga_instance = pygad.GA( num_generations = num_generations,
                                    num_parents_mating = num_parents_mating,
                                    mutation_type = "adaptive",
                                    #    mutation_type = mutation_func,
                                    mutation_probability = mutation_probability,
                                    parent_selection_type = parent_selection_type,
                                    keep_parents = keep_parents,
                                    fitness_func = self.fitness_func,
                                    gene_space = {'low': init_range_low, 'high': init_range_high},
                                    initial_population = populacao)
            # Execução do algoritmo genético
            ga_instance.run()
            # Salva a melhor solução da execução atual
            solution, solution_fitness, solution_idx = ga_instance.best_solution()
            best_solutions.append(solution)
            best_fitnesses.append(self.cec_func(solution))
        return (best_fitnesses, best_solutions)


if __name__ == '__main__':
    D = 10
    obj = Heuristic(D)
    bests = obj.GA()
    best_fitnesses = bests[0]  
    plt.plot(best_fitnesses)
    plt.title('Fitness ao longo das gerações')
    plt.xlabel('Gerações')
    plt.ylabel('Fitness')
    plt.show()
    print(bests[1])
    print(best_fitnesses)
    print("Best: {} ".format(min(best_fitnesses)))
    print("Worst: {} ".format(max(best_fitnesses)))
    print("Std: {}".format(st.stdev(best_fitnesses)))
    print("Mediana: {}".format(st.median((best_fitnesses))))
    print("Media: {}".format(st.mean(best_fitnesses)))



