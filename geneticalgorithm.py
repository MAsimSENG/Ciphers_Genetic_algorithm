import random

# Constant
FITNESS_OF_NEW_CHROMOSOME = -1


def print_list_vertically(list):
    for item in list:
        print(item)


def get_sorted(list):
    # https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column
    return sorted(list, key=lambda x: x[1], reverse=True)


def get_random_char():
    return chr(random.randint(97, 122))

#  Unused
# def crossover_single_point(parent1, parent2, crossover_location=0):
#     '''
#     This method takes two parents (strings) and returns two children (strings).
#     The children are a combination of the parents as long as the string length
#     is greater than 1. When the string length = 1, the children are a copy of
#     the parent.
#     '''
#     if crossover_location == 0 or crossover_location > len(parent1):
#         crossover_location = int(len(parent1) / 2)
#
#     child1 = parent1[:crossover_location] + \
#         parent2[crossover_location:len(parent2)]
#
#     child2 = parent2[:crossover_location] + \
#         parent1[crossover_location:len(parent1)]
#
#     return child1, child2


def crossover_k_point(parent1, parent2, crossover):
    '''
    This method takes two parents (strings) and crossover (integer).
    This method returns two children (strings).
    The children are a combination of the parents. How the child is formed
    is dictated by value of crossover.
    '''
    child1=parent1[:crossover]
    child2=parent2[:crossover]
    i=1
    while(crossover*i<len(parent1)):
        if(i%2==0):
            child1=child1+parent1[crossover*i:crossover*(i+1)]
            child2=child2+parent2[crossover*i:crossover*(i+1)]
        else:
            child1=child1+parent2[crossover*i:crossover*(i+1)]
            child2=child2+parent1[crossover*i:crossover*(i+1)]
        i+=1

    if(i%2==0):
        child1=child1+parent1[crossover*i:crossover*(i+1)]
        child2=child2+parent2[crossover*i:crossover*(i+1)]
    else:
        child1=child1+parent2[crossover*i:crossover*(i+1)]
        child2=child2+parent1[crossover*i:crossover*(i+1)]

    return child1, child2


def mutate(chromosome, mutation_round=2):
    '''
    This function takes a chromosome and replaces random location with random
    char for `mutation_round` many times.

    Parameters:
    chromosome          - String representation of the chromosome
    mutation_round      - Number of iterations to perform mutation

    # https://stackoverflow.com/questions/2165172/replacing-one-character-of-a-string-in-python
    '''

    mutated_chromosome = list(chromosome)
    for i in range(mutation_round):
        c = get_random_char()
        loc = random.randint(0, len(chromosome) - 1)
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


def run_genetic_algorithm(*,
                          plain_text,
                          encrypted_text,
                          decrypt_function,
                          population,
                          fitness_function,
                          verbose=1):

    if verbose == 2:
        print()
        print('=== Initial population ===')
        print_list_vertically(population)

    #

    # Emulate do-wihle loop
    # https://coderwall.com/p/q_rd1q/emulate-do-while-loop-in-python
    loop_counter = 0
    while (calc_exit(population) == True):
        loop_counter += 1

        #

        # Calculate fitness
        for individual in population:

            # For optimization:
            # As the list is sorted, chromosomes with fitness of
            # FITNESS_OF_NEW_CHROMOSOME (i.e. -1) will be in the begining of
            # the list. And as this for loop is linear, there is no need
            # to recalculate the fitness of chromosomes that already has
            # a value other than FITNESS_OF_NEW_CHROMOSOME.
            if individual[1] != -1:
                break

            key_guess = individual[0]
            decrypted_text_guess = decrypt_function(encrypted_text, key_guess)
            fitness = fitness_function(plain_text, decrypted_text_guess)
            individual[1] = fitness

        population = get_sorted(population)
        if verbose == 2:
            print()
            print('=== After fitness calculation and sort ===')
            print_list_vertically(population)

        #

        # Selection
        parent1 = population[-1][0]  # get last chromosome in the list
        parent2 = population[-2][0]  # get 2nd last chromosome in the list
        if verbose == 2:
            print()
            print('=== Parents for crossover ===')
            print(parent1)
            print(parent2)

        #

        # Crossover
        # Change k value to crossover every k characters
        k=random.randint(1,10)
        child1,child2=crossover_k_point(parent1, parent2, k)
        # I also saw the following:
        #
        #     child1, child2 = crossover_single_point(parent1, parent2,
        #                                             crossover_location=random.randint(2,6))
        #
        # Splitting the chromosome at random location is a greate idea and
        # definately worth eploring.
        if verbose == 2:
            print()
            print('=== Children from crossover ===')
            print(child1)
            print(child2)

        #

        # Mutation
        mutated_child = mutate(child1, mutation_round=2)
        if verbose == 2:
            print()
            print('=== Mutated chromosome ===')
            print(mutated_child)

        #

        # Next generation. Replacing weakest chromosome in the population
        population[0] = [child1, FITNESS_OF_NEW_CHROMOSOME]
        population[1] = [child2, FITNESS_OF_NEW_CHROMOSOME]
        population[2] = [mutated_child, FITNESS_OF_NEW_CHROMOSOME]

        #

        if verbose == 2:
            print()
            print('=== Population after repalcing weak chromosome ===')
            print_list_vertically(population)
            print()

        if verbose >= 1:
            print("End of iteration:", loop_counter, "\t\t",
                  "Best Fitness:", population[-1][1])

        #

    # After the loop. I.e. break condition met.
    found_key = population[-1][0]  # Last chromosome in population

    return found_key, loop_counter
