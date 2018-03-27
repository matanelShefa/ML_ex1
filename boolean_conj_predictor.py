import numpy as np
import sys

# Get the input.
inputFile = str(sys.argv[1])
training_examples = np.loadtxt(inputFile)
print training_examples

# Get 'd' - the number of the variables in the examples.
d = len(training_examples[0])

# The examples list
xMatrix = []
# The tags list
yMatrix = []

# Create the lists from the input.
for example in training_examples:
    xMatrix.append(np.array(example[0:d-1]))
    yMatrix.append(np.array(example[d-1]))

# Print - debug. TODO - remove.
for example in xMatrix:
    print example

# Print - debug. TODO - remove.
for example in yMatrix:
    print example

