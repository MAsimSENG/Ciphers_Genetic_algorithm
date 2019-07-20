import argparse
import cipher
import euclidean as euclid
import geneticalgorithm as ga
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
                        help='Run GA to completion only once')

    parser.add_argument('-e', '--experiment',
                        help='Run GA for specified iterations to collect statistics',
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
        run_experiment(args.experiment)


def run_experiment(iterations):
    # TODO @arshi
    print('Unimplemented. Iterations:', iterations)
    pass


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

    print("Key:", found_key)


if __name__ == "__main__":
    main()
