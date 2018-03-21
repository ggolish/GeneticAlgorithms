'''

    General purpose class for genetic algorithms.
    Written by Gage Golish.
    Licensed under MIT license.

'''

import random

class Genetics(object):

    def __init__(self, population_size, chromosome_size, min_gene, max_gene, crossover_rate = 0.7, mutation_rate = 0.1, anomaly_rate = 0.1):
        self.population_size = population_size
        self.chromosome_size = chromosome_size
        self.min_gene = min_gene
        self.max_gene = max_gene
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.anomaly_rate = anomaly_rate
        self.fitnesses = []
        self.population = self.new_population()
        self.generation = 1

    def new_population(self):
        return [self.new_chromosome() for _ in range(self.population_size)]

    def new_chromosome(self):
        return [self.new_gene() for _ in range(self.chromosome_size)]

    def new_gene(self):
        return random.randint(self.min_gene, self.max_gene)

    # Algorithm for creating the next generation
    # Note a certain percentage of the new population will be
    # entirely random based on the anomaly rate.
    def repopulate(self):
        new_population = []
        self.max_fitness = max(self.fitnesses)
        if self.max_fitness <= 0: return
        while len(new_population) < len(self.population):
            prob = random.uniform(0, 1)
            if prob > self.anomaly_rate:
                c1, c2 = self.choose(), self.choose()
                self.crossover(c1, c2)
                self.mutate([c1, c2])
            else:
                c1, c2 = self.new_gene(), self.new_gene()
            new_population.extend([c1, c2])
        self.population = new_population
        self.generation += 1

    # Chooses a member of the population using rejection sampling.
    def choose(self):
        while True:
            index = random.randint(0, self.population_size - 1)
            qualifier = random.uniform(0, self.max_fitness)
            if qualifier < self.fitnesses[index]:
                return list(self.population[index])

    # Creates two new members of population by splicing two existing members 
    # together. Only runs according to some probability.
    def crossover(self, c1, c2):
        prob = random.random()
        if prob < self.crossover_rate:
            index = random.randint(0, self.chromosome_size - 1)
            copy1 = list(c1)
            copy2 = list(c2)
            for i in range(index):
                c1[i] = copy2[i]
            for i in range(index, self.chromosome_size):
                c2[i] = copy1[i]

    # Randomizes the genes in a member of the population based on 
    # some probability
    def mutate(self, chromosomes):
        for c in chromosomes:
            prob = random.random()
            if prob < self.mutation_rate:
                c[random.randint(0, self.chromosome_size - 1)] = self.new_gene()

