import random
import numpy as np

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        return np.sqrt((self.x - city.x) ** 2 + (self.y - city.y) ** 2)

class Fitness:
    def __init__(self, tour, cities):
        self.tour = tour
        self.cities = cities

    def route_distance(self):
        return sum(self.cities[self.tour[i]].distance_to(self.cities[self.tour[(i + 1) % len(self.tour)]]) for i in range(len(self.tour)))

    def fitness(self):
        return 1 / (1 + self.route_distance())

def genetic_algorithm(cities, generations=500, pop_size=10):
    population = [random.sample(range(len(cities)), len(cities)) for _ in range(pop_size)]

    for gen in range(generations):
        population.sort(key=lambda tour: Fitness(tour, cities).fitness(), reverse=True)
        new_pop = population[:pop_size // 2]

        while len(new_pop) < pop_size:
            parent1, parent2 = random.sample(new_pop, 2)
            crossover_point = random.randint(1, len(cities) - 1)
            child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
            new_pop.append(child)
        
        population = new_pop

    best_tour = population[0]
    return best_tour, Fitness(best_tour, cities).route_distance()

# Example cities
cities = [City(random.randint(0, 100), random.randint(0, 100)) for _ in range(5)]

# Run the Genetic Algorithm
best_tour, best_distance = genetic_algorithm(cities)
print(f"Best Tour: {best_tour}, Distance: {best_distance}")