import argparse
import cipher
import euclidean as euclid
import geneticalgorithm as ga
import numpy as np
import random
import sys


# Global variables
__plain_text = "this is some plain text"
__key = "quacktim"
__encrypted_text = cipher.encrypt(__plain_text, __key)

__population = [
    ['aaaaaaaa', -1],
    ['bbbbbbbb', -1],
    ['cccccccc', -1],
    ['dddddddd', -1],
    ['eeeeeeee', -1],
    ['ffffffff', -1],
]
# End of global variables


def main():

    # Init parser
    parser = argparse.ArgumentParser()

    #

    # Define arguments.
    # https://docs.python.org/2/howto/argparse.html
    parser.add_argument('--dev',
                        action='store_true',
                        help='Run the GA to completion only once')

    parser.add_argument('-e', '--experiment',
                        help='Run the GA for specified iterations to collect statistics',
                        type=int)

    parser.add_argument('-v', '--verbosity',
                        help='Increase output verbosity',
                        type=int,
                        choices=[0, 1, 2])

    #

    # Parse arguments
    args = parser.parse_args()

    #

    if len(sys.argv) == 1:
        print('Not enough arguments. See --help (or -h)')
        # https://stackoverflow.com/questions/10698468/argparse-check-if-any-arguments-have-been-passed

    # Run the respective function with respective parameters
    if args.dev:
        trial_run(args.verbosity)
    elif args.experiment is not None:
        run_experiment(args.experiment, args.verbosity)


def run_experiment(iterations, verbosity):

    if verbosity is None:
        verbosity = 1

    results = np.array([])

    for n in range(iterations):
        unused, num_of_gens = ga.run_genetic_algorithm(plain_text=__plain_text,
                                                       encrypted_text=__encrypted_text,
                                                       decrypt_function=cipher.decrypt,
                                                       population=__population,
                                                       fitness_function=euclid.euclideanDistance,
                                                       verbose=0
                                                       )

        results = np.append(results, num_of_gens)

        if verbosity >= 1:
            print('Experiment:', n, '\t\t',
                  'Number of generation:', num_of_gens)

    #

    # Calculate stats and report
    print('=== Stats Summary ===')
    print('n = ', iterations)
    print('Mean:', np.mean(results))
    print('Var:', np.var(results))
    print('StDev:', np.std(results))

    if verbosity == 2:
        print(results)


def trial_run(verbosity):

    if verbosity is None:
        verbosity = 1

    found_key = ga.run_genetic_algorithm(plain_text=__plain_text,
                                         encrypted_text=__encrypted_text,
                                         decrypt_function=cipher.decrypt,
                                         population=__population,
                                         fitness_function=euclid.euclideanDistance,
                                         verbose=verbosity
                                         )

    print()
    print("Key Found:", found_key[0])
    print("Num of Generations:", found_key[1])


if __name__ == "__main__":
    main()
