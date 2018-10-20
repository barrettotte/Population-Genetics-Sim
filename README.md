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