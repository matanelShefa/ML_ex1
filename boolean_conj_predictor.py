import numpy as np
import sys


def hypothesis_fix(hypothesis_to_fix, current_example):

    # Check the hypothesis and fix it if needed.
    for i in range(0, d - 1):
        i_bit = current_example[i]
        if (i_bit == 0) & (1 in hypothesis_to_fix[i]):
            hypothesis_to_fix[i].remove(1)
        if (i_bit == 1) & (0 in hypothesis_to_fix[i]):
            hypothesis_to_fix[i].remove(0)


# Get the input.
inputFile = str(sys.argv[1])
training_examples = np.loadtxt(inputFile)
print "input:\n", training_examples

# Get 'd' - the number of the variables in the examples.
d = len(training_examples[0])

# The examples list
xMatrix = []
# The tags list
yVector = []

# Create the lists from the input.
for example in training_examples:
    xMatrix.append(np.array(example[0 : d - 1]))
    yVector.append(np.array(example[d - 1]))

# Print - debug. TODO - remove.
print "xMatrix:"
for example in xMatrix:
    print example

# Print - debug. TODO - remove.
print "yVector:"
for example in yVector:
    print example

# Generate the all-negative-hypothesis.
hypothesis = []
for i in range(1, d):
    variable = []
    variable.append(1)  # Xi
    variable.append(0)  # NOT Xi
    hypothesis.append(variable)

print "hypothesis: ", hypothesis

# The consistency algorithm
for i in range(0, len(yVector)):

    print 'xMatrix[i] = ', xMatrix[i]
    print 'yVector[i] = ', yVector[i]
    # The current example's classification is 0 - continue.
    if yVector[i] == 0:
        continue

    # The current example's classification is 1 - Fix the hypothesis if needed.
    hypothesis_fix(hypothesis, xMatrix[i])

    print 'hypothesis: ', hypothesis

# Build the final hypothesis.
finalHypothesis = ''
i = 1
for variable in hypothesis:
    if 0 in variable:
        finalHypothesis = finalHypothesis + 'x' + str(i)
        if i != len(hypothesis):
            finalHypothesis = finalHypothesis + ','
    if 1 in variable:
        finalHypothesis = finalHypothesis + 'not(x' + str(i) + ')'
        if i != len(hypothesis):
            finalHypothesis = finalHypothesis + ','

    i = i + 1


# Print to the output file.
outputFile = open('./output.txt', 'w+')
outputFile.write(finalHypothesis)
outputFile.close()