# Prototype for ProcJam 2018

import random, string, json, io, os, time
import allWords

# ------------- Global Parameters ----------------------
testsToRun = 10
genSize = 1000
allWords = allWords.AllWords()
mutationChance = 0.006
mysteryDnaChance = 0.001
asexReprChance = 0.001
asexTopOrganisms = 0.001
fitnessWeights = [1,2,4,6,8]
idealError = 5
idealDNA = {
    "color": ["00000000", "11111111", "00000000"]
}
# -----------------------------------------

def makeInitPopulation(size):
    generation = []
    if size < 50:
        print("Initial population must be at least 50 organisms.")
    else:
        for i in range(size):
            dna = makeDNA()
            generation.append(makeOrganism(makeId(0,i),randomName(),dna,['?????-?????','?????-?????']))
    return generation

def makeId(genIter, orgIter):
    return str(genIter).zfill(5) + "-" + str(orgIter).zfill(5)

def makeDNA():
    return { "color": randomAllele("color") }

def randomName():
    name = allWords.allAdjectives[random.randint(0, allWords.adjectivesLen-1)] + " "
    name += allWords.allNouns[random.randint(0, allWords.adjectivesLen-1)]
    return name

def makeOrganism(id, name, dna, parents):
    return { "id": id, "name": name, "DNA": dna, "parents": parents, "topMarker": 0 }

def randomAllele(name):
    allele = []
    if name == "color":
        allele = [
            decToBin(random.randint(0,255)),
            decToBin(random.randint(0,255)),
            decToBin(random.randint(0,255))
        ]
    return allele

def evaluateFitness(generation, idealDNA):
    fitnessScores = []
    topOrganisms = int(len(generation) * asexTopOrganisms)
    for alleleName,allele in idealDNA.items():
        for organism in generation:
            orgAllele = organism["DNA"][alleleName]
            fitnessScores.append(evaluateAllele(alleleName, orgAllele, allele))
    for i in range(len(fitnessScores)):
        generation[i]["fitness"] = fitnessScores[i]
    generation = sortDescending(generation, "fitness")
    for organism in generation[-topOrganisms:]:
        organism["topMarker"] = 1   # Top organism will asexually reproduce
    return generation

def evaluateAllele(alleleName, orgAllele, idealAllele):
    score = 0
    if alleleName == "color":
        for i in range(len(idealAllele)):
            if orgAllele[i] != idealAllele[i]:
                score += abs(binToDec(idealAllele[i]) - binToDec(orgAllele[i])) 
    return score

def setMatingChances(generation):
    popSize = len(generation)
    fifthPop = int(popSize * 0.20)
    fitnessDistrib = [fifthPop, popSize-(fifthPop*3), popSize-(fifthPop*2), popSize-(fifthPop), popSize]
    for i in range(len(generation)):
        for j in range(len(fitnessDistrib)):
            if i < fitnessDistrib[j]:
                generation[i]["matingChance"] = fitnessWeights[j]
                break
    return generation

def generateMatingPool(generation):
    genSize = len(generation)
    pool = []
    for _ in range(genSize):  # "Weighted Random" of organisms
        r = random.randint(0, genSize-1)
        pool.extend([generation[r]] * generation[r]["matingChance"])
    return pool

def newGeneration(matingPool, genSize, genIter):
    poolSize = len(matingPool)
    nextGeneration = []
    for i in range(genSize):
        parent1 = getRandElem(matingPool, 0, poolSize-1)
        parent2 = getRandElem(matingPool, 0, poolSize-1)
        if parent1["topMarker"] == 1:
            parent2 = parent1
        elif parent2["topMarker"] == 1:
            parent1 = parent2
        elif random.random() < mysteryDnaChance:
            parent1 = makeOrganism(makeId(genIter,i),randomName(),makeDNA(),['?????-?????','?????-?????'])
        nextGeneration.append(reproduce(parent1, parent2, genIter, i))
    return nextGeneration

def reproduce(parent1, parent2, genIter, orgIter):
    # Asexual Reproduction chance, "Top" organisms will always asexually reproduce
    if random.random() < asexReprChance or parent1["id"] == parent2["id"]:
        if random.random() < 0.50:
            dna = parent1["DNA"]
            parents = [parent1["id"], parent1["id"]]
        else:
            dna = parent2["DNA"]
            parents = [parent2["id"], parent2["id"]]
    else:
        dna = crossover(parent1["DNA"], parent2["DNA"])
        parents = [parent1["id"], parent2["id"]]
    dna = mutate(dna)
    return makeOrganism(makeId(genIter, orgIter), randomName(), dna, parents)

def crossover(parent1, parent2):
    offspringDNA = {}
    for allele,strand in parent1.items():
        offspringDNA[allele] = []
        crossoverMethod = random.randint(0,4)
        for i in range(len(strand)):
            if crossoverMethod == 0:  # Single Point Crossover
                crossPoint = parent1[allele][i] if random.random() < 0.50 else parent2[allele][i]
            elif crossoverMethod == 1:
                crossPoint = parityCrossover(parent1[allele][i], parent2[allele][i])
            elif crossoverMethod == 2:
                crossPoint = arithmeticCrossover(parent1[allele][i], parent2[allele][i])
            else:
                crossPoint = uniformCrossover(parent1[allele][i], parent2[allele][i])
            offspringDNA[allele].append(crossPoint)
    return offspringDNA

def parityCrossover(strand1, strand2):
    offspringStrand = ''
    for j,_ in enumerate(strand1):
        if j % 2 == 0:
            offspringStrand += strand1[j]
        else:
            offspringStrand += strand2[j]
    return offspringStrand

def arithmeticCrossover(strand1, strand2):
    offspringStrand = ''
    for j,_ in enumerate(strand1):
        if random.random() < 0.50:  # AND / OR strands
            offspringStrand += "1" if strand1[j] == "1" and strand2[j] == "1" else "0"
        else:
            offspringStrand += "1" if strand1[j] == "1" or strand2[j] == "1" else "0"
    return offspringStrand

def uniformCrossover(strand1, strand2):
    offspringStrand = ''
    for j,_ in enumerate(strand1):
        if random.random() < 0.50:
            offspringStrand += strand1[j]
        else:
            offspringStrand += strand2[j]
    return offspringStrand

def mutate(dna):
    for allele,strand in dna.items():
        for i in range(len(strand)):
            dna[allele][i] = list(dna[allele][i])
            for bit in range(len(dna[allele][i])):
                if random.random() < mutationChance:
                    if dna[allele][i][bit] == "1":
                        dna[allele][i][bit] = "0"
                    else:
                        dna[allele][i][bit] = "1"
            dna[allele][i] = "".join(dna[allele][i])
    return dna
                
def getRandElem(someList, min, max):
    return someList[random.randint(min, max)]

def decToBin(num):
    return bin(num)[2:].zfill(8)

def binToDec(num):
    return int(num, 2)

def sortDescending(collection, sortKey):
    return sorted(collection, key=lambda k: k[sortKey])[::-1]

def printGeneration(generation, genCount):
    print("\n\n" + repeatStr("-",15) + " Generation " + str(genCount).zfill(5) + repeatStr("-",15))
    print("   All Organisms of Generation " + str(genCount))
    for organism in generation:
        print("      " + str(organism))

def printPrettyJsonDict(jsonRaw):
    return json.dumps(jsonRaw, indent=4, sort_keys=True, separators=(',', ': '))

def repeatStr(s, i):
    return s * i

def checkForIdeal(generation, idealDNA):
    for organism in generation:
        if organism["fitness"] <= idealError:
            return True
    return False

def getAverage(someList):
    avg = 0
    for x in someList:
        avg += x
    return round(avg / len(someList),3)

def writeParamsToFile():
    with open('results.txt', 'w') as f:
        params = "Searching for Ideal DNA: " + str(idealDNA) + "\n"
        params += "Parameters: \n"
        params += "   Generation Size: " + str(genSize) + "\n"
        params += "   Mutation Chance: " + str(mutationChance) + "\n"
        params += "   Mystery DNA Chance: " + str(mysteryDnaChance) + "\n"
        params += "   Asexual Reproduction Chance: " + str(asexReprChance) + "\n"
        params += "   Top Organisms Asexually Reproduce: " + str(asexTopOrganisms) + "\n"
        params += "   Fitness Weights: " + str(fitnessWeights) + "\n"
        params += "   Ideal Organism Allowable Error: " + str(idealError) + "\n"
        f.write(params + "\n\n")

def printResults(test, ideal, genCount, orgCount, execTime):
    results = "Results of Test " + str(test+1).zfill(2) + ": \n"
    results += "   The Ideal Organism Found: " + "ID: " + ideal["id"] + ", "
    results += "Name: " + ideal["name"] + ", Fitness: " + str(ideal["fitness"]) + "\n"
    results += "   DNA: " + str(ideal["DNA"]) + "\n"
    results += "   Total Generations Created: " + str(genCount-1) + "\n"
    results += "   Total Organisms Created:   " + str(orgCount) + "\n"
    results += "   Executed for " + str(execTime) + " seconds" + "\n\n\n"
    return results

def main():
    stats = {
        "Error": [],
        "Execution Time": [],
        "Generated Generations": [],
        "Generated Organisms": []
    }
    print("Population Genetics Simulation:")
    print("   Ideal Organism DNA:  " + str(idealDNA) + "\n\n")
    writeParamsToFile()

    for test in range(testsToRun):
        foundIdeal = False
        startTime = time.time()
        organismCount = 0
        generationCount = 0

        generation = makeInitPopulation(genSize)
        generation = setMatingChances(evaluateFitness(generation, idealDNA)) 
        generationCount += 1
        foundIdeal = checkForIdeal(generation, idealDNA)
        topOrganism = generation[-1]

        while foundIdeal == False:
            nextGeneration = newGeneration(generateMatingPool(generation), genSize, generationCount)
            nextGeneration = setMatingChances(evaluateFitness(nextGeneration, idealDNA))   
            generationCount += 1
            organismCount += len(nextGeneration)
            foundIdeal = checkForIdeal(nextGeneration, idealDNA)
            bestOrganism = nextGeneration[-1]
            if bestOrganism["fitness"] < topOrganism["fitness"]:
                topOrganism = bestOrganism
            s = " ... " + "All Gen's Best:  " + str(topOrganism["name"]).ljust(15) + " - " + str(topOrganism["fitness"])
            s += " ... This Gen's Best:  " + str(bestOrganism["name"]).ljust(25) + " - " + str(bestOrganism["fitness"])
            print("Test " + str(test).zfill(3) + " ... Generation " + str(generationCount).zfill(5) + s)

        idealOrganism = nextGeneration[-1]
        execTime = round(time.time() - startTime, 3)
        results = printResults(test, idealOrganism, generationCount, organismCount, execTime)
        print(results)
        stats["Error"].append(idealOrganism["fitness"])
        stats["Execution Time"].append(execTime)
        stats["Generated Generations"].append(generationCount)
        stats["Generated Organisms"].append(organismCount)
        with open('results.txt', 'a') as f:
            f.write(results)
        time.sleep(0.25)

    averages = "Ran Simulation " + str(testsToRun) + " Time(s).\n"
    for key,val in stats.items():
        avg = getAverage(val)
        averages += "   Average " + key + " - " + str(avg) + "\n"
    print(averages)
    with open('results.txt', 'a') as f:
        f.write(averages)

if __name__ == "__main__":main()