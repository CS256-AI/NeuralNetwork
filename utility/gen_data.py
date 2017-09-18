import re
import sys
import random
import vector_utils


def bool_dist_generator(n):
    """
    Generates random n bit data of count following uniform distribution
    :param n: number of inputs
    :return: returns a 'n' element boolean vector as a list
    """
    input_data = list()
    for i in range(0, n):
        #Create 1 input vector of size 'n'
        input_data.append(random.randint(0, 1))
    return input_data

def spherical_dist_generator(n):
    """
    Generates random n bit data of count following spherical distribution
    :param n: number of inputs
    :return: returns a vector of 'n' element spherical distribution as a list
    """
    input_data = list()
    sum_sqrt = 0
    for i in range(0, n):
        # Find a random float term
        term = random.random()
        input_data.append(term)
        #Calculate the sum of squares of all terms to normalize the input
        sum_sqrt += term ** 2
        # print("term {}-->{}".format(j, term))
    # print("Squared sum --> {}".format(sum_sqrt))
    sum_sqrt = sum_sqrt ** (1/2.0)
    #print("Sq root sum --> {}".format(sum_sqrt))
    #Normalize the vector
    for i in range(0, n):
        input_data[i] = input_data[i]/sum_sqrt
    return input_data

def parse_ground_file(file_name):
    result = ''
    in_file = open(file_name)
    line = in_file.readline().strip()
    # print("Input line 1 --> {}".format(line))
    if line == 'NBF':
        #print("Parsing nested boolean function")
        func_type = 'NBF'
        line = in_file.readline().strip()
        # print("Input line 2 --> {}".format(line))
        func = re.search(re.compile('([+|-]\d+(\s+(AND|OR)\s+[+|-]\d+)*)?'),line).group(0)
        # print("Ground function -->{}".format(func))
        if func:
            pattern_operands = re.compile('\s*([+|-]\d+)\s*')
            pattern_operators = re.compile('\s*(AND|OR)\s*')
            operands = re.findall(pattern_operands, func)
            #print("operands = {}".format(operands))
            operators = re.findall(pattern_operators, func)
            #print("operators = {}".format(operators))
            result = (func_type, operands, operators)
            #print("result = {}".format(result))
    elif line == 'TF':
        #print("Parsing threshold function")
        func_type = 'TF'
        line = in_file.readline()
        # print("Input line 2 --> {}".format(line))
        # Search for the threshold value
        threshold = re.search(re.compile('[+|-]\d+'), line).group(0)
        if threshold:
            threshold = float(threshold)
            # print("threshold = {}".format(threshold))
            line = in_file.readline()
            # print("Input line 3 --> {}".format(line))
            func = re.search(re.compile('([+|-]\d+(\s+[+|-]\d+)*)?'), line).group(0)
            if func:
                # print("Ground function -->{}".format(func))
                pattern_term = re.compile('\s*([+|-]\d+)\s*')
                terms = re.findall(pattern_term, func)
                for i in range(len(terms)):
                    terms[i] = float(terms[i])
                # print("terms = {}".format(terms))
                result = (func_type, terms, threshold)
                # print("ground funciton(function type, terms, threshold) = {}".format(result))
                return result
            else:
                result = None
    else:
        result = None
    return result


def cal_thresh_fn(input_x, terms, threshold):
    # print("input_x --> {}".format(input_x))
    # print("terms --> {}".format(terms))
    lhs = vector_utils.dot_product(input_x,terms)
    if lhs >= threshold:
        return 1
    else:
        return 0


def generate_data(ground_file, count, dist):
    result = parse_ground_file(ground_file)
    data = list()
    if result:
        type = result[0]
        if type == 'NBF':
            print('parsed nbf')
        elif type == 'TF':
            # print( 'parsed tf')
            type, terms, threshold = result
            no_inputs = len(terms)
            # print("no of inputs = {}".format(no_inputs))
            if dist == 'bool':
                dist_fn = bool_dist_generator
            elif dist == 'sphere':
                dist_fn = spherical_dist_generator
            for i in range(count):
                input_x = dist_fn(no_inputs)
                data.append((input_x, cal_thresh_fn(input_x, terms, threshold)))
            # print("Data : {}".format(data))
            return data
        else:
            sys.exit('NOT PARCEABLE')
    else:
        sys.exit('NOT PARCEABLE')
# print(bool_dist_generator(3))
# print(spherical_dist_generator(3))
# parse_ground_file('sample_function_2')
generate_data('D:\SJSU\Fall17\CS256\NeuralNetwork\sample_function_2', 10, 'bool')



