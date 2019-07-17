import geneticalgorithm as ga
import euclidean
import cipher

'''
population = [
    ['aaaaaaaa', 0],
    ['bbbbbbbb', 0],
    ['cccccccc', 0],
    ['dddddddd', 0],
    ['eeeeeeee', 0],
    ['ffffffff', 0],
]

population = ga.run_genetic_algorithm(population, mutation_round=4)

'''

def trial_run():
    key = "quacktim"
    population = [
        ['aaaaaaaa', -1],
        ['bbbbbbbb', -1],
        ['cccccccc', -1],
        ['dddddddd', -1],
        ['eeeeeeee', -1],
        ['ffffffff', -1],
    ]
    pfile = open("plain.txt", "r")
    efile = open("encrypted.txt", "w")


    for line in pfile:
        singleEncryptedLine = cipher.encrypt(line,key)
        efile.write(singleEncryptedLine)
    pfile.close()
    efile.close()

    population = ga.run_genetic_algorithm(population=population,
                                          crossover_location=4,
                                          mutation_round=10)







if __name__ == "__main__":
    trial_run()
