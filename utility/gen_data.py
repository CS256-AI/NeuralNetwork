import re
import sys
import random
import vector_utils


def bool_dist_generator(n):
    """
    Generates a 'n' element vector following uniform boolean distribution
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
    Generates a 'n' element vector following spherical distribution
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
    """
    Parses the ground file to return a nbf or threshold function
    :param file_name: name of file containing the ground function
    :return: returns tuple (func_type, operands, operators) for nbf and (func_type, terms, threshold) for threshold funciton
    """
    result = ''
    in_file = open(file_name)
    line = in_file.readline().strip()
    # print("Input line 1 --> {}".format(line))
    if line == 'NBF':
        #print("Parsing nested boolean function")
        func_type = 'NBF'
        line = in_file.readline().strip()
        if not line:
            return(func_type, None, None)
        # print("Input line 2 --> {}".format(line))
        func = re.search(re.compile('([+|-]\d+(\s+(AND|OR)\s+[+|-]\d+)*)?'),line).group(0)
        # print("Ground function -->{}".format(func))
        if func:
            pattern_operands = re.compile('\s*([+|-]\d+)\s*')
            pattern_operators = re.compile('\s*(AND|OR)\s*')
            operands = re.findall(pattern_operands, func)
            #print("operands = {}".format(operands))
            for i in range(len(operands)):
                try:
                    operands[i] = int(operands[i])
                except ValueError:
                    # Handle the exception
                    print('Please enter integer terms for NBF function')
            operators = re.findall(pattern_operators, func)
            #print("operators = {}".format(operators))
            result = (func_type, operands, operators)
            print("ground function(function type, operands, operators) = {}".format(result))
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
                    try:
                        terms[i] = float(terms[i])
                    except ValueError:
                        # Handle the exception
                        print('Please enter numeric terms for TF function')
                # print("terms = {}".format(terms))
                result = (func_type, terms, threshold)
                # print("ground function(function type, terms, threshold) = {}".format(result))
                return result
            else:
                result = None
    else:
        result = None
    return result


def cal_thresh_fn(input_x, terms, threshold):
    """
    Calculate the value of the threshold function 'y'
    :param input_x: input values
    :param terms: coefficients of the threshold function
    :param threshold: threshold value
    :return: 'y' value as per threshold function
    """
    # print("input_x --> {}".format(input_x))
    # print("terms --> {}".format(terms))
    lhs = vector_utils.dot_product(input_x,terms)
    if lhs >= threshold:
        return 1
    else:
        return 0

def find_no_terms_nbf(operands):
    """
    Finds number of inputs as per nbf in the ground function
    :param operands: The indices of the operands
    :return: No. of inputs
    """
    max_index = 0
    for operand in operands:
        if max_index < abs(operand):
            max_index = abs(operand)
    return max_index


def cal_nbf_fn(input_x, operands, operators):
    """
    Calculate the value of the threshold nbf 'y'
    :param input_x: input values
    :param terms: coefficients of the threshold function
    :param threshold: threshold value
    :return: 'y' value as per nbf function
    """
    print("input_x = {}".format(input_x))
    no_terms = len(operands)
    expression = '(' * (no_terms-1)
    #print("no_terms {}".format(no_terms))
    for i in range(no_terms):
        print("i = {}".format(i))
        #print("operands[i] = {}".format(operands[i]))
        if operands[i] == 0:
            sys.exit("NOT PARCEABLE")
        if operands[i] > 0:
            term = input_x[operands[i] - 1]
        else:
            term = 1 - input_x[abs(operands[i]) - 1]
        if i < no_terms - 1:
            expression += str(term)
            if i != 0:
                expression += ")"
            expression += " " + str(operators[i]).lower() + " "
        else:
            expression += str(term) + ")"
    #print("expression --> {}".format(expression))
    #print("result -- {}".format(eval(expression)))
    return eval(expression)

def generate_data(ground_file, count, dist):
    """
    Generates data for training and testing
    :param ground_file: name of file containing the ground funciton
    :param count: no. of examples required
    :param dist: distribution followed by the inputs
    :return: list of data examples with each example being a tuple ([x],y)
    """
    result = parse_ground_file(ground_file)
    data = list()
    if result:
        type = result[0]
        if type == 'NBF':
            print('parsed nbf')
            type, operands, operators = result
            if not operands and not operators:
                #Asssuming 5 terms in case of always 0 function
                no_inputs = 3
                for i in range(count):
                    # Ignore the distribution value
                    input_x = bool_dist_generator(no_inputs)
                    data.append((input_x, 0))
            else:
                no_inputs = find_no_terms_nbf(operands)
                print("no of inputs = {}".format(no_inputs))
                for i in range(count):
                    # Ignore the distribution value
                    input_x = bool_dist_generator(no_inputs)
                    data.append((input_x, cal_nbf_fn(input_x, operands, operators)))
            print("Data : {}".format(data))
            return data
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


# generate_data('sample_function', 10, 'bool')



