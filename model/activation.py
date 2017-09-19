import math

def tanh_activation(val, theta):
    """
    tanh activation implementation. Returns activation signal based on val.
    :param val: activation parameter
    :return: Boolean activation result.
    """
    return math.tanh(val-theta)


def relu_activation(val, theta):
    """
    relu activation implementation. Returns activation signal based on val.
    :param val: activation parameter
    :return: Boolean activation result.
    """
    return max(0, val-theta)


def threshold_activation(val, theta):
    """
    theshold activation implementation. Returns activation signal based on val.
    :param val: activation parameter
    :param theta: threshold parameter
    :return: Boolean activation result.
    """
    if val >= theta:
        return 1
    else:
        return 0


def ground_truth(x):
    if (x[0] and x[2]) or x[1]:
        return 1
    else:
        return 0