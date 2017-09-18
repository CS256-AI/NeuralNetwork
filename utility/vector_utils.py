def dot_product(x, y):
    product = 0
    if len(x) == len(y):
        for i in range(len(x)):
            product += x[i] * y[i]

    return product


def vector_sum(x, y):
    vsum = [0]*len(x)
    if len(x) == len(y):
        for i in range(len(x)):
            vsum[i] = x[i] + y[i]

    return vsum


def vector_difference(x, y):
    vdiff = [0]*len(x)
    if len(x) == len(y):
        for i in range(len(x)):
            vdiff[i] = x[i] - y[i]

    return vdiff