import random
import cipher
import euclidean

# Constant
NEW = -1


def print_list_vertically(list):
    for item in list:
        print(item)


def get_sorted(list):
    # https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column
    return sorted(list, key=lambda x: x[1], reverse=True)


def get_random_char():
    return chr(random.randint(97, 122))


def crossover(parent1, parent2, crossover_location=random.randint(2, 6)):
    '''
    This method takes two parents (strings) and returns two children (strings).
    The children are a combination of the parents as long as the string length
    is greater than 1. When the string length = 1, the children are a copy of
    the parent.
    '''
    if crossover_location == 0 or crossover_location > len(parent1):
        crossover_location = int(len(parent1) / 2)

    child1 = 'N/A'
    child1 = parent1[:crossover_location] + \
        parent2[crossover_location:len(parent2)]

    child2 = 'N/A'
    child2 = parent2[:crossover_location] + \
        parent1[crossover_location:len(parent1)]

    return child1, child2


def my_fitness_function(individual):
    '''
    Returns the fitness of an individual
    '''

    return euclidean.euclideanDistance(individual)


def calculate_fitness(population):
    '''
    Returns the fitness of the entire populations as a 2d list
    '''

    for individual in population:
        fitness = my_fitness_function(individual)
        individual[1] = fitness

    return population


def mutate(chromosome, mutation_round=2):
    '''
    This function takes a chromosome and replaces random location with random
    char for `mutation_round` many times.

    Parameters:
    chromosome          - String representation of the chromosome
    mutation_round      - Number of iterations to perform mutation

    # https://stackoverflow.com/questions/2165172/replacing-one-character-of-a-string-in-python
    '''

    chromosome = list(chromosome)
    mutated_chromosome = chromosome
    chromosomeLength = len(chromosome)

    for i in range(mutation_round):
        c = get_random_char()
        loc = random.randint(0, chromosomeLength - 1)
        mutated_chromosome[loc] = c

    mutated_chromosome = ''.join(mutated_chromosome)

    return mutated_chromosome


def calc_exit(population):
    '''
    Checks the exit condition
    '''

    for individual in population:
        fitness = individual[1]
        if fitness == 0:
            return False

    return True


def run_genetic_algorithm(population,
                          crossover_location=4,
                          mutation_round=4):

    print()
    print('=== Initial population ===')
    print_list_vertically(population)

    # Emulate do-wihle loop
    # https://coderwall.com/p/q_rd1q/emulate-do-while-loop-in-python
    x = 0
    while (calc_exit(population) == True):
        x += 1
        print("Iteration #", x)

        # Calculate fitness
        population = calculate_fitness(population)
        print()
        print('=== After fitness calculation ===')
        print_list_vertically(population)

        #

        # Selection
        population = get_sorted(population)
        parent1 = population[-1][0]  # get last chromosome in the list
        parent2 = population[-2][0]  # get 2nd last chromosome in the list
        print()
        print('=== Parents for crossover ===')
        print(parent1)
        print(parent2)

        #

        # Crossover
        child1, child2 = crossover(parent1, parent2, crossover_location)
        print()
        print('=== Children from crossover ===')
        print(child1)
        print(child2)

        #

        # Mutation
        mutated_child = mutate(child1)
        print()
        print('=== Mutated chromosome ===')
        print(child1)

        #

        # Next generation. Replacing weakest chromosome in the population
        population[0] = [child1, NEW]
        population[1] = [child2, NEW]
        population[2] = [mutated_child, NEW]

        #

        print()
        print('=== Population after repalcing weak chromosome ===')
        print_list_vertically(population)

    return population
