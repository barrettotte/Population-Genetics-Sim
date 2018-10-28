# Population Genetics
Simulate basic population genetics on fake creatures' DNA. Concepts of mutation, crossover, fitness distribution covered

Used for ProcJam 2018, repo located here https://github.com/barrettotte/ProcJam-2018


## Process
* **Initialize** - Population N random DNA
* **Selection** - Evaluate fitness, generate mating pool
* **Reproduction** - Repeat N times, pick parents based on "weighted random" of mating rate
* **Crossover** - Combine DNA through some crossover method
* **Mutation** - Mutate child based on mutation rate
* Add child to new generation
* Discard old population
* Repeat until ideal organism within ideal error is found

### Additional Process
* A percentage of "Top" fitness organisms will asexually reproduce to keep their ideal DNA in the mating pool.
* There is a small chance a random organism will asexually reproduce
* There is a small chance that Parent 1 will not pass any DNA and will be replaced by newly generated DNA.
* An "Ideal Error" was introduced to speed up the algorithm's execution time, since it always got close, but sometimes never made a fitness value of 0.

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
   The Ideal Organism Found: ID: 00061-00194, Name: determined detail, Fitness: 5
   DNA: {'color': ['00000010', '11111110', '00000010']}
   Total Generations Created: 61
   Total Organisms Created:   61000
   Executed for 1.662 seconds


Results of Test 02: 
   The Ideal Organism Found: ID: 00019-00160, Name: subdued friction, Fitness: 5
   DNA: {'color': ['00000001', '11111100', '00000001']}
   Total Generations Created: 19
   Total Organisms Created:   19000
   Executed for 0.522 seconds


Results of Test 03: 
   The Ideal Organism Found: ID: 00123-00461, Name: jagged growth, Fitness: 5
   DNA: {'color': ['00000000', '11111100', '00000010']}
   Total Generations Created: 123
   Total Organisms Created:   123000
   Executed for 3.438 seconds


Results of Test 04: 
   The Ideal Organism Found: ID: 00085-00707, Name: knowledgeable collar, Fitness: 5
   DNA: {'color': ['00000001', '11111011', '00000000']}
   Total Generations Created: 85
   Total Organisms Created:   85000
   Executed for 2.381 seconds


Results of Test 05: 
   The Ideal Organism Found: ID: 00030-00794, Name: festive agreement, Fitness: 4
   DNA: {'color': ['00000001', '11111110', '00000010']}
   Total Generations Created: 30
   Total Organisms Created:   30000
   Executed for 0.835 seconds


Results of Test 06: 
   The Ideal Organism Found: ID: 00147-00003, Name: auspicious burn, Fitness: 5
   DNA: {'color': ['00000001', '11111111', '00000100']}
   Total Generations Created: 147
   Total Organisms Created:   147000
   Executed for 4.258 seconds


Results of Test 07: 
   The Ideal Organism Found: ID: 00247-00272, Name: snotty number, Fitness: 5
   DNA: {'color': ['00000001', '11111100', '00000001']}
   Total Generations Created: 247
   Total Organisms Created:   247000
   Executed for 6.816 seconds


Results of Test 08: 
   The Ideal Organism Found: ID: 00088-00328, Name: cuddly spark, Fitness: 2
   DNA: {'color': ['00000000', '11111110', '00000001']}
   Total Generations Created: 88
   Total Organisms Created:   88000
   Executed for 2.443 seconds


Results of Test 09: 
   The Ideal Organism Found: ID: 00090-00693, Name: frightened brass, Fitness: 2
   DNA: {'color': ['00000000', '11111101', '00000000']}
   Total Generations Created: 90
   Total Organisms Created:   90000
   Executed for 2.547 seconds


Results of Test 10: 
   The Ideal Organism Found: ID: 00001-00021, Name: macabre government, Fitness: 3
   DNA: {'color': ['00000000', '11111111', '00000011']}
   Total Generations Created: 1
   Total Organisms Created:   1000
   Executed for 0.042 seconds


Ran Simulation 10 Time(s).
   Average Error - 4.1
   Average Execution Time - 2.494
   Average Generated Generations - 90.1
   Average Generated Organisms - 89100.0

```
## Console Raw
![https://github.com/barrettotte/Population-Genetics-Sim/blob/master/consoleRaw.PNG](https://github.com/barrettotte/Population-Genetics-Sim/blob/master/consoleRaw.PNG)
