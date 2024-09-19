import random
import numpy as np

# Função objetivo
def f(x):
    return x**3 - 6*x + 14

# Codificação binária de um número real
def encode(x, bits=16):
    x_int = int((x + 10) * (2**(bits-1) / 20))
    return format(x_int, f'0{bits}b')

# Decodificação binária para um número real
def decode(binary, bits=16):
    x_int = int(binary, 2)
    return x_int * 20 / (2**(bits-1)) - 10

# Criação da população inicial
def create_population(size, bits=16):
    return [encode(random.uniform(-10, 10), bits) for _ in range(size)]

# Seleção por torneio
def tournament_selection(population, scores, k=3):
    selected = random.sample(list(zip(population, scores)), k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

# Crossover de um ponto
def crossover(parent1, parent2, crossover_rate=0.7):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

# Mutação
def mutate(individual, mutation_rate=0.01):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)

# Algoritmo genético
def genetic_algorithm(pop_size=10, generations=100, bits=16, crossover_rate=0.7, mutation_rate=0.01, elitism=True, elite_size=0.1):
    population = create_population(pop_size, bits)
    best_individual = None
    best_score = float('inf')

    for generation in range(generations):
        scores = [f(decode(ind, bits)) for ind in population]
        best_gen_score = min(scores)
        best_gen_individual = population[scores.index(best_gen_score)]

        if best_gen_score < best_score:
            best_score = best_gen_score
            best_individual = best_gen_individual

        new_population = []

        if elitism:
            elite_count = int(elite_size * pop_size)
            elite_individuals = sorted(zip(population, scores), key=lambda x: x[1])[:elite_count]
            new_population.extend([ind for ind, score in elite_individuals])

        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)
            offspring1, offspring2 = crossover(parent1, parent2, crossover_rate)
            new_population.append(mutate(offspring1, mutation_rate))
            if len(new_population) < pop_size:
                new_population.append(mutate(offspring2, mutation_rate))

        population = new_population

    best_x = decode(best_individual, bits)
    return best_x, best_score

# Configurações do algoritmo
pop_size = 10
generations = 100
bits = 16
crossover_rate = 0.7
mutation_rate = 0.01
elitism = True
elite_size = 0.1

# Executar o algoritmo genético
best_x, best_score = genetic_algorithm(pop_size, generations, bits, crossover_rate, mutation_rate, elitism, elite_size)
print(f"Melhor x: {best_x}, Melhor valor da função: {best_score}")
