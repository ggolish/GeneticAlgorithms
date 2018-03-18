
import random

class Genetics(object):

    def __init__(self, population_size, chromosome_size, min_gene, max_gene, crossover_rate = 0.7, mutation_rate = 0.1):
        self.population_size = population_size
        self.chromosome_size = chromosome_size
        self.min_gene = min_gene
        self.max_gene = max_gene
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.fitnesses = []
        self.population = self.new_population()
        self.generation = 1

    def new_population(self):
        return [self.new_chromosome() for _ in range(self.population_size)]

    def new_chromosome(self):
        return [self.new_gene() for _ in range(self.chromosome_size)]

    def new_gene(self):
        return random.randint(self.min_gene, self.max_gene)

    def repopulate(self):
        new_population = []
        self.max_fitness = max(self.fitnesses)
        if self.max_fitness <= 0: return
        self.probabilities = [f / self.max_fitness for f in self.fitnesses]
        while len(new_population) != len(self.population):
            c1, c2 = self.choose(), self.choose()
            self.crossover(c1, c2)
            self.mutate([c1, c2])
            new_population.extend([c1, c2])
        self.population = new_population
        self.generation += 1

    def choose(self):
        while True:
            index = random.randint(0, self.population_size - 1)
            qualifier = random.uniform(0, self.max_fitness)
            if qualifier < self.fitnesses[index]:
                return list(self.population[index])

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

    def mutate(self, chromosomes):
        prob = random.random()
        if prob < self.mutation_rate:
            for c in chromosomes:
                c[random.randint(0, self.chromosome_size - 1)] = self.new_gene()

