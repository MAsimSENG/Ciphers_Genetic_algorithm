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
    '''
    This method takes two parents (strings) and returns two children (strings).
    The children are a combination of the parents as long as the string length is greater than 1. When the string length = 1, the children are a copy of the parent.
    '''
    if crossover_location == 0:
        crossover_location = int(len(parent1) / 2)

    child1 = 'N/A'
    child1 = parent1[:crossover_location] + parent2[crossover_location:len(parent2)]

    child2 = 'N/A'
    child2 = parent2[:crossover_location] + parent1[crossover_location:len(parent1)]

    return child1, child2


def my_fitness_function(input):
    # TODO @arshi update this when Euclidean distance is comleted
    return random.randint(0, 9)


def calculate_fitness(population):
    # TODO
    # for each 'gene' in the 2D list of 'population':
        # fitness = call the fitness function with gene
        # store the value in gene[1]

    return population


def mutate(gene, mutation_round=0):
    '''
    This function takes a gene and replaces random location with random char for
    `mutation_round` many times.

    Parameters:
    gene                - String representation of the gene
    mutation_round      - Number of iterations to perform mutation
    '''

    # https://stackoverflow.com/questions/2165172/replacing-one-character-of-a-string-in-python
    # TODO (see the link ^^^) turn `gene` into a list s.t. we can manipulate individual chars.
    mutated_gene = 'TODO Mutation'
    for i in range(mutation_round):
        pass  # TODO delete this when the loop is implemented
        # TODO get random char. See `get_random_char` function
        # TODO loc = get random location within the bound of the string length
        # TODO repalce mutated_gene's `loc` position with the char attained by `get_random_char`
    # TODO convert the list into string (''.join(...))
    mutated_gene = 'TODO Mutation'

    return mutated_gene


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
        '''
        TODO @Rafay
        '''
        population = get_sorted(population)
        parent1 = population[-1][0]  # TODO get last gene in the list
        parent2 = population[-2][0]  # TODO get 2nd last gene in the list
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
        print('=== Mutated gene ===')
        print(child1)

        #

        # Next generation. Replacing weakest genes in the population
        population[0] = [child1, 0]
        population[1] = [child2, 0]
        population[2] = [mutated_child, 0]

        #

        print()
        print('=== Population after repalcing weak genes ===')
        print_list_vertically(population)

        # Emulate do-wihle loop
        # TODO @arshi write the actual break conditions when more pieces are in place
        if True:
            break

    return population
