import time
import random

def ScientificToDecimal(x):
    y = ""
    x = str(x).split('e')

    if(len(x) > 1):
        absExponent = int(abs(float(x[1])))

        for i in range(absExponent):
            if (i == 0):
                y += '0.'
            else:
                y += '0'

        x[0] = x[0].replace('.','')
        y += x[0]
    elif(len(x) == 1):
        y = x[0]
    else:
        print(f'Faulty value {x} in ScientificToDecimal, x seems to be 0 or null')
        y = 0

    return y

def QuadraticAlgorithm(x):
    n = len(x)
    maxSoFar = 0.0

    for l in range(1, n+1):
        for u in range(l, n+1):
            sum = 0.0
            for i in range(l, u+1):
                sum += x[i-1]
            maxSoFar = max(maxSoFar, sum)

    return maxSoFar

def SquareAlgorithm1(x):
    n = len(x)
    maxSoFar = 0.0

    currentSum = 0.0
    for i in range(n):
        currentSum = max(x[i], currentSum + x[i])
        maxSoFar = max(maxSoFar, currentSum)
    return maxSoFar

def SquareAlgorithm2(x):
    n = len(x)
    cumArray = [0] * (n+1) 

    for i in range(1, n+1):
        cumArray[i] = cumArray[i-1] + x[i-1]

    maxSoFar = 0.0

    for l in range(1, n+1):
        for u in range(l, n+1):
            sum = cumArray[u] - cumArray[l - 1]
            maxSoFar = max(maxSoFar, sum)

    return maxSoFar


def AlgorithmTester(algorithm, xLength, numRuns, maxX):
    x = [0]*xLength

    totalTime = 0
    maxX = abs(maxX)

    for i in range(numRuns):

        for k in range(len(x)):
            x[k] = random.randint(-maxX, maxX)

        print(f'progress {round((i / numRuns)*100)}% ({i}/{numRuns})')

        t = time.time()

        AlgorithmOutput = algorithm(x)

        t = time.time() - t
        totalTime = totalTime + t

        print('-'* 20)
    print(f'progress 100% ({numRuns}/{numRuns})')
    print(ScientificToDecimal(totalTime / numRuns))
    print('-'*20)
    return totalTime / numRuns

xLen    = 50
numRuns = 100000
maxX    = 100


print(f'The following results are for an array with the length {xLen}. Each algorithm was tested {numRuns} times.')
quadraticAlgorithmResult = AlgorithmTester(QuadraticAlgorithm, xLen, numRuns, maxX)
squareAlgorithm1Result   = AlgorithmTester(SquareAlgorithm1,   xLen, numRuns, maxX)
squareAlgorithm2Result   = AlgorithmTester(SquareAlgorithm2,   xLen, numRuns, maxX)
print(f'QuadraticAlgorithm took an average of {ScientificToDecimal(quadraticAlgorithmResult)} sec.')
print(f'SquareAlgorithm1 took an average of   {ScientificToDecimal(squareAlgorithm1Result)} sec.')
print(f'SquareAlgorithm2 took an average of   {ScientificToDecimal(squareAlgorithm2Result)} sec.')
print(f'The fastest was {max(squareAlgorithm1Result, squareAlgorithm2Result, quadraticAlgorithmResult) / min(squareAlgorithm1Result, squareAlgorithm2Result, quadraticAlgorithmResult)} times faster than the slowest')


