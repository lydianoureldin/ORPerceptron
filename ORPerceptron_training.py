'''
April 7 2017
Lydia Noureldin
This program solves the ORPerceptrom problem
'''

import random
combinations = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0],\
                [1, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0],\
                [1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 1],\
                [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]


'''
calculates the X value given a list of weights and a vector of values
'''
def getX(aVector, weights):
    X = 0
    # make sure input is valid
    if len(aVector) != len(weights):
        print "Lengths of aVector and weights must be equal!"
    for i in range(len(aVector)):
        X = X + aVector[i] * weights[i]
    return X


'''
Takes in a vector of values and returns a list of randomly generated
weights of the same length of the given vector
'''
def getInitialWeights():
    random.seed()
    weights = []
    for i in range(4):
        aVal = random.uniform(-1, 1)  # get a random float from -1 to 1
        weights.append(aVal)
    return weights


'''
Takes in X value and a threshold and calculates Y based on these values
'''
def step(X, threshold):
    if X > threshold:
        return 1
    return 0


'''
Recalculates the weights until the Y value matches the expected value
Returns the weights and, 0 if no updates happened to the weights and 1 otherwise. 
t = 0
a = 0.1

'''
def calculate(vector, weights) :
    learningValue = 0.1
    threshold = 0
    X = getX(vector, weights)
    Y = step(X, threshold)
    expectedValue = getExpectedValue(vector)
    if expectedValue == Y:
        return weights, 0
    while Y != expectedValue:
        error = expectedValue - Y
        weights = calculateNewWeights(learningValue, error, vector, weights)
        X = getX(vector, weights)
        Y = step(X, threshold)
        if expectedValue == Y:
            return weights, 1

'''
Calculates new weights, only called if the initial randomly
generated weights produced an error
'''
def calculateNewWeights(learningValue, error, vector, oldWeights):
    weights = []
    for i in range(len(vector)):
        # Check if the weight contributed to the error
        if vector[i] == 0:
            weights.append(oldWeights[i])
            continue
        weights.append(oldWeights[i] + (learningValue * vector[i] * error))
    return weights


'''
Mimics the "OR" function, given a list of bits
Returns 1 if there is at least one 1 in vector, and 0 otherwise
'''
def getExpectedValue(vector) :
    # checks input is valid
    for aVal in vector:
        if aVal != 0 and aVal != 1:
            print "vector must contain only 0 and 1 values"
    # Check if there is at least one 1 in vector
    if 1 in vector:
        return 1
    return 0

'''
writes trained OR Perceptron weight values to a text file
'''
def writeOutput(file, weights):
    for aWeight in weights:
        file.write(str(aWeight) + "\n")


def main():
    f = open("training.txt", "w")
    weights = getInitialWeights()
    while True:
        updateSum = 0
        for vector in combinations:
            weights, update = calculate(vector, weights)
            updateSum = updateSum + update
        # Check if we have gone through an epoch without any error
        if updateSum == 0:
            break
    writeOutput(f, weights)
    f.close()

main()
