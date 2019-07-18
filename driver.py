import cipher
import euclidean as euclid
import geneticalgorithm as ga
import random


def trial_run():

    plain_text = "this is some plain text"
    key = "quacktim"
    encrypted_text = cipher.encrypt(plain_text, key)

    population = [
        ['aaaaaaaa', -1],
        ['bbbbbbbb', -1],
        ['cccccccc', -1],
        ['dddddddd', -1],
        ['eeeeeeee', -1],
        ['ffffffff', -1],
    ]

    found_key = ga.run_genetic_algorithm(plain_text=plain_text,
                                         encrypted_text=encrypted_text,
                                         decrypt_function=cipher.decrypt,
                                         population=population,
                                         fitness_function=euclid.euclideanDistance,
                                         crossover_location=random.randint(0, 8),
                                         # crossover_location=4,
                                         mutation_round=4,
                                         # verbose=True
                                         )

    print("Key:", found_key)


if __name__ == "__main__":
    trial_run()
