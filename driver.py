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

population = ga.run_genetic_algorithm(population, mutation_round=2)

'''

def trial_run():
    key = "abcd"
    population = [
        ['aaaaaaaa', 0],
        ['bbbbbbbb', 0],
        ['cccccccc', 0],
        ['dddddddd', 0],
        ['eeeeeeee', 0],
        ['ffffffff', 0],
    ]
    pfile = open("plain.txt", "r")
    efile = open("encrypted.txt", "w")


    for line in pfile:
        singleEncryptedLine = cipher.encrypt(line,key)
        efile.write(singleEncryptedLine)
    pfile.close()
    efile.close()

    population = ga.run_genetic_algorithm(population, mutation_round=2)








if __name__ == "__main__":
    trial_run()
