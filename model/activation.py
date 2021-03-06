import math

def tanh_activation(val, theta):
    """
    tanh activation implementation. Returns activation signal based on val.
    :param val: activation parameter
    :return: Boolean activation result.
    """
    result = math.tanh(val-theta)
    return result
    # return threshold_activation(result, 0)


def relu_activation(val, theta):
    """
    relu activation implementation. Returns activation signal based on val.
    :param val: activation parameter
    :return: Boolean activation result.
    """
    result = max(0, val-theta)
    return result
    # return threshold_activation(result, 0.2)


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
