import random


def print_list_vertically(list):
    for item in list:
        print(item)


def get_sorted(list):
    # https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column
    return sorted(list, key=lambda x: x[1])


def get_random_char():
    return chr(random.randint(97, 122))


def crossover(parent1, parent2, crossover_location=0):

    if crossover_location == 0:
        crossover_location = int(len(parent1) / 2)

    # TODO concatenate:
    # parent1[0 to `crossover_location`]
    # and
    # parent2[`crossover_location` to the end of parent2]
    child1 = 'TODO Child 1'

    # TODO concatenate:
    # parent1[0 to `crossover_location`]
    # and
    # parent2[`crossover_location` to the end of parent2]
    child2 = 'TODO Child 2'

    return child1, child2


def my_fitness_function(input):
    # TODO @arshi update this when Euclidean distance is comleted
    return random.randint(0, 9)


def calculate_fitness(population):

    for each individual in population:

        fitness = my_fitness_function(individual)

        individual[1] = fitness
        
    return population


def mutate(chromosome, mutation_round=0):
    '''
    This function takes a chromosome and replaces random location with random char for
    `mutation_round` many times.

    Parameters:
    chromosome                - String representation of the chromosome
    mutation_round      - Number of iterations to perform mutation
    '''

    chromosome = list(chromosome)

    mutated_chromosome = chromosome

    chromosomeLength = len(chromosome)

    for i in range(mutation_round):

        c = get_random_char()

        loc = random.randint(0, chromosomeLength-1)

        mutated_chromosome[loc] = c


    mutated_chromosome = ''.join(mutated_chromosome)

    return mutated_chromosome


def run_genetic_algorithm(population,
                          crossover_location=0,
                          mutation_round=0):

    print()
    print('=== Initial population ===')
    print_list_vertically(population)

    # Emulate do-wihle loop
    # https://coderwall.com/p/q_rd1q/emulate-do-while-loop-in-python
    while True:

        # Calculate fitness
        population = calculate_fitness(population)
        print()
        print('=== After fitness calculation ===')
        print_list_vertically(population)

        #

        # Selection
        population = get_sorted(population)
        parent1 = population[0][0]  # TODO get last chromosome in the list
        parent2 = population[0][0]  # TODO get 2nd last chromosome in the list
        print()
        print('=== Parents for crossover ===')
        print(parent1)
        print(parent2)

        #

        # Crossover
        child1, child2 = crossover(parent1, parent2, crossover_location)
        print()
        print('=== Cihldren from crossover ===')
        print(child1)
        print(child2)

        #

        # Mutation
        mutated_child = mutate(child1)
        print()
        print('=== Mutated chromosome ===')
        print(child1)

        #

        # Next generation. Replacing weakest chromos in the population
        population[0] = [child1, 0]
        population[1] = [child2, 0]
        population[2] = [mutated_child, 0]

        #

        print()
        print('=== Population after repalcing weak chromos ===')
        print_list_vertically(population)

        # Emulate do-wihle loop
        # TODO @arshi write the actual break conditions when more pieces are in place
        if True:
            break

    return population
