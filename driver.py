import geneticalgorithm as ga

population = [
    ['aaaaaaaa', 0],
    ['bbbbbbbb', 0],
    ['cccccccc', 0],
    ['dddddddd', 0],
    ['eeeeeeee', 0],
    ['ffffffff', 0],
]

population = ga.run_genetic_algorithm(population, mutation_round=2)
