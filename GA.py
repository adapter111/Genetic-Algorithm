import random
class DNA:
    def __init__(self, length):
        self.genes=[]
        self.fitness=0
        self.length=length
        for i in range(self.length):
            self.genes.append(random.choice(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))

    def  crossover(self, partner):
        child=DNA(self.length)
        midpoint=random.randint(0,len(self.genes)-1)
        for i in range(len(self.genes)):
            if i<midpoint:
                child.genes[i]=self.genes[i]
            else:
                child.genes[i]=partner.genes[i]
        return child
 
def generatePopulation(populationSize, target):
    population = []
    for i in range(populationSize):
        population.append(DNA(len(target)))
    return population

def calculateFitness(target, population):
    for i in population:
        score=0
        for j in range(len(target)):
            if i.genes[j]==target[j]:
                score+=1
        i.fitness = score/len(target)

def draw(population):
    matingPool = []
    for phrase in population:
        n=phrase.fitness*100
        for j in range(int(n)):
            matingPool.append(phrase)
    return matingPool

def breed(matingPool, populationSize):
    newPopulation=[]
    for i in range(populationSize):
        parentA=random.choice(matingPool)
        parentB=random.choice(matingPool)
        child=parentA.crossover(parentB)
        newPopulation.append(child)
    return newPopulation

def mutate(mutationRate, population):
    for phrase in population:
        for i in range(len(phrase.genes)):
            if random.random()<mutationRate:
                phrase.genes[i]=random.choice(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return population

def areThereWinners(population, target):
    for i in population:
        print(''.join(i.genes))
        if ''.join(i.genes)==target:
            print(target,'found after',generation,'generations')
            return True
    return False

populationSize=int(input("Enter the population size: "))
target=input("Enter the target phrase: ")
population = generatePopulation(populationSize, target)
mutationRate=0.01
generation=0

while not areThereWinners(population, target):
    generation+=1
    calculateFitness(target, population)
    matingPool=draw(population)
    population=breed(matingPool, populationSize)
    population=mutate(mutationRate, population)