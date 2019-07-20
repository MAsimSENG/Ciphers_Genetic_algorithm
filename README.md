# Ciphers and Genetic Algorithm

Using genetic algorithm to break ciphers



## Requirements

- Python 3





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

Expected sample output:

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

TODO @arshi





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
