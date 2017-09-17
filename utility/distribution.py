import random


def uniform_dist_generator(n, count):
    """
    Generates random n bit data of count following uniform distribution
    :param n: number of inputs
    :param count: number of data to generate
    :return: array of n bit vectors
    """
    input_data = list()
    for i in range(1, count+1):
        input_1 = list()
        for j in range(1, n+1):
        #Create 1 input vector of size 'n'
            input_1.append(random.randint(0, 1))
        # Create 'count' no. of input samples
        input_data.append(input_1)
    return input_data

def spherical_dist_generator(n, count):
    """
    Generates random n bit data of count following spherical distribution
    :param n: number of inputs
    :param count: number of data to generate
    :return: array of n bit vectors
    """
    input_data = list()
    for i in range(0, count):
        input_1 = list()
        row_sqrt = 0
        for j in range(0, n):
            # Find a random float term
            term = random.random()
            input_1.append(term)
            #Calculate the sum of squares of all terms to normalize the input
            row_sqrt += term ** 2
            #print("term {}-->{}".format(j, term))
        #print("Row squared sum --> {}".format(row_sqrt))
        row_sqrt = row_sqrt ** (1/2.0)
        #print("Row sq root sum --> {}".format(row_sqrt))

        #Normalize the vector
        for j in range(0, n):
            input_1[j] = input_1[j]/row_sqrt

        input_data.append(input_1)
    return input_data

def test():
    print("** Spherical distribution **")
    print (spherical_dist_generator(3, 10))
    print("** Uniform boolean distribution **")
    print (uniform_dist_generator(3, 10))

#test the distribution functions
test()

