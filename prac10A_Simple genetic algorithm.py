import random

# Parameters
population_size = 10
generations = 5
mutation_rate = 0.1

# Fitness function (maximize x^2)
def fitness(x):
    return x ** 2

# Create initial population (random numbers between 0 and 31)
def create_population():
    return [random.randint(0, 31) for _ in range(population_size)]

# Select parents using tournament selection
def select_parents(population):
    return sorted(population, key=fitness, reverse=True)[:2]

# Crossover: One-point crossover
def crossover(parent1, parent2):
    return (parent1 + parent2) // 2  # Simple averaging crossover

# Mutation: Flip a bit in the binary representation
def mutate(x):
    if random.random() < mutation_rate:
        return x ^ (1 << random.randint(0, 4))  # Random bit flip
    return x

# Main genetic algorithm
def genetic_algorithm():
    population = create_population()
    for generation in range(generations):
        population = [mutate(crossover(*select_parents(population))) for _ in range(population_size)]
        best_individual = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best = {best_individual}, Fitness = {fitness(best_individual)}")
    return max(population, key=fitness)

# Run the genetic algorithm
best_solution = genetic_algorithm()
print(f"Best solution: {best_solution}, Fitness: {fitness(best_solution)}")