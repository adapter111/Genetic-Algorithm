import random
class DNA:
    def __init__(self, length):
        self.genes=[]
        self.fitness=0
        for i in range(length):
            self.genes.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))

    def  crossover(self, partner):
        child=DNA(len(self.genes))
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

def mutate(self, mutationRate):
    for i in range(len(self.genes)):
        if random.random()<mutationRate:
            self.genes[i]=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def draw(self, population, target):
    matingPool = []
    for phrase in population:
        phrase.calculateFitness(target)
        n=phrase.fitness*100
        for j in range(int(n)):
            matingPool.append(phrase)
    r
    for i in range(len(population)):
        parentA=random.choice(matingPool)
        parentB=random.choice(matingPool)
        child=parentA.crossover(parentB)
        child.mutate(0.01)
        population[i]=child
    return population

def checkForWinner(self, population, target):
    for phrase in population:
        if phrase.genes==list(target):
            return True
    return False

