# Population Genetics
Simulate basic population genetics on fake creatures' DNA. Concepts of mutation, crossover, fitness distribution covered

## Summary
* This script will simulate a generation of "creatures" generation after generation until the ideal color allele is found.
* Each creature has one allele in their "DNA" for color and is passed to offspring based on fundamentals of genetics (crossover, mutation). 
* Depending on how close the creature's color allele is to the ideal allele, it is given a fitness value which affects its chances of reproducing with another creature.
* This is meant to be a prototype before ProcJam 2018 to work out any janky behavior before implementing in C# and Unity.

## Sources:
* Basics of bitwise crossover/mutation http://www.obitko.com/tutorials/genetic-algorithms/crossover-mutation.php
* Noun and Adjective Lists https://github.com/aaronbassett/Pass-phrase


## Results
```
Searching for Ideal DNA: {'color': ['00000000', '11111111', '00000000']}
Parameters: 
   Generation Size: 1000
   Mutation Chance: 0.006
   Mystery DNA Chance: 0.001
   Asexual Reproduction Chance: 0.001
   Top Organisms Asexually Reproduce: 0.001
   Fitness Weights: [1, 2, 4, 6, 8]
   Ideal Organism Allowable Error: 5


Results of Test 01: 
   The Ideal Organism Found: ID: 00078-00875, Name: fabulous calendar, Fitness: 5
   DNA: {'color': ['00000001', '11111111', '00000100']}
   Total Generations Created: 78
   Total Organisms Created:   78000
   Executed for 2.162 seconds


Results of Test 02: 
   The Ideal Organism Found: ID: 00029-00354, Name: optimal hat, Fitness: 4
   DNA: {'color': ['00000001', '11111110', '00000010']}
   Total Generations Created: 29
   Total Organisms Created:   29000
   Executed for 0.812 seconds


Results of Test 03: 
   The Ideal Organism Found: ID: 00029-00354, Name: optimal hat, Fitness: 4
   DNA: {'color': ['00000001', '11111110', '00000010']}
   Total Generations Created: 0
   Total Organisms Created:   0
   Executed for 0.014 seconds


Results of Test 04: 
   The Ideal Organism Found: ID: 00241-00228, Name: picayune giraffe, Fitness: 5
   DNA: {'color': ['00000000', '11111010', '00000000']}
   Total Generations Created: 241
   Total Organisms Created:   241000
   Executed for 6.714 seconds


Results of Test 05: 
   The Ideal Organism Found: ID: 00067-00363, Name: available coal, Fitness: 3
   DNA: {'color': ['00000010', '11111110', '00000000']}
   Total Generations Created: 67
   Total Organisms Created:   67000
   Executed for 1.84 seconds


Results of Test 06: 
   The Ideal Organism Found: ID: 00222-00373, Name: strong harmony, Fitness: 5
   DNA: {'color': ['00000010', '11111110', '00000010']}
   Total Generations Created: 222
   Total Organisms Created:   222000
   Executed for 6.281 seconds


Results of Test 07: 
   The Ideal Organism Found: ID: 00293-00740, Name: skillful tiger, Fitness: 5
   DNA: {'color': ['00000011', '11111111', '00000010']}
   Total Generations Created: 293
   Total Organisms Created:   293000
   Executed for 8.21 seconds


Results of Test 08: 
   The Ideal Organism Found: ID: 00192-00821, Name: zany care, Fitness: 5
   DNA: {'color': ['00000011', '11111110', '00000001']}
   Total Generations Created: 192
   Total Organisms Created:   192000
   Executed for 5.686 seconds


Results of Test 09: 
   The Ideal Organism Found: ID: 00245-00443, Name: shy clam, Fitness: 2
   DNA: {'color': ['00000000', '11111110', '00000001']}
   Total Generations Created: 245
   Total Organisms Created:   245000
   Executed for 7.821 seconds


Results of Test 10: 
   The Ideal Organism Found: ID: 00114-00908, Name: wandering lettuce, Fitness: 2
   DNA: {'color': ['00000000', '11111111', '00000010']}
   Total Generations Created: 114
   Total Organisms Created:   114000
   Executed for 3.24 seconds


Ran Simulation 10 Time(s).
   Average Error - 4.0
   Average Execution Time - 4.278
   Average Generated Generations - 149.1
   Average Generated Organisms - 148100.0
```
## Console Raw
![https://github.com/barrettotte/Population-Genetics-Sim/blob/master/consoleRaw.PNG](https://github.com/barrettotte/Population-Genetics-Sim/blob/master/consoleRaw.PNG)
