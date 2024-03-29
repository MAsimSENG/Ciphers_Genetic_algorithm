# Ciphers and Genetic Algorithm

Using Genetic Algorithm (GA) to break ciphers and find the key used to encrypte
a message.



## Requirements

- Python 3
- Libraries:
    - NumPy


## Run

To see a demo, run the following command:

```
$ python driver.py --dev
```

To see more outputs, run the following command:

```
$ python driver.py --dev -v 2
```


---


## Usage

```
$ python driver.py [operational_mode]
```

Operational modes:

- `--dev` - for quick runs, test functionality, see numbers, and debugging.
- `--experiment n` - run the entire GA for `n` iterations and collect statistics.





### Simple Run (`--dev`)

```
$ python driver.py --dev
```

Expected sample output (with default verbosity of 1):

```
End of iteration: 1 		 Best Fitness: 31.670175244226233
End of iteration: 2 		 Best Fitness: 31.0
...
End of iteration: 2385 		 Best Fitness: 1.0
End of iteration: 2386 		 Best Fitness: 0.0
Key: quacktim
```


---


Change the output verbosity with `--verbosity` (or `-v`):

```
$ python driver.py --dev -v 2
```

Expected output:

```
=== Initial population ===
['aaaaaaaa', -1]
['bbbbbbbb', -1]
['cccccccc', -1]
...

=== After fitness calculation and sort ===
['ffffffff', 36.55133376499413]
['eeeeeeee', 35.874782229304195]
['dddddddd', 35.7211421989835]
...

=== Parents for crossover ===
aaaaaaaa
bbbbbbbb

=== Children from crossover ===
aaaabbbb
bbbbaaaa

=== Mutated chromosome ===
aaaadbbu

=== Population after repalcing weak chromosome ===
['aaaabbbb', -1]
...
['aaaaaaaa', 31.670175244226233]

End of iteration: 1 		 Best Fitness: 31.670175244226233
```


---


```
$ python driver.py --dev -v 0
```

Expected output is the found key by the GA. E.g.

```
Key: quacktim
```





### Experiment

Run an experiment using the `--experiment` (or `e`) argument. This will run the
GA for `n` iterations. At each iteration, the number of generations is
recorded. At the end of the experiment, results are reported. Results include:
mean, variance, and standard deviation.

```
$ python driver.py -e 5
```

Expected sample output (with default verbosity of 1):

```
Experiment: 0 		 Number of generation: 1339
Experiment: 1 		 Number of generation: 3147
Experiment: 2 		 Number of generation: 5127
Experiment: 3 		 Number of generation: 1350
Experiment: 4 		 Number of generation: 612
=== Stats Summary ===
n =  5
Mean: 2315.0
Var: 2676715.6
StDev: 1636.067113537828
```

Verbose level 0 will simply show the Stats Summary at the end of execution.
Verbosity of 2 will show the list containing number of generation across all
experiments.





### Verbose

Specify verbosity level using `--verbosity` (or `-v`). Verbosity levels:
```
0 - None
1 - Summary
2 - All (Debug)
```



### Others

Use `--help` (or `-h`) to see a list of all argument and usages.

```
$ python driver.py -h
```
