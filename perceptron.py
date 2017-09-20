import sys
from model.perceptron import Perceptron
from utility import gen_data
from utility import constants

if len(sys.argv) < 8:
    print("Insufficient number of arguments.\nPattern : python perceptron.py activation training_alg ground_file distribution num_train num_test epsilon")
    sys.exit()
else:
    activation, learning, ground_file, distribution = sys.argv[1:5]
    num_train, num_test = [int(i) for i in sys.argv[5:7]]
    epsilon = float(sys.argv[7])

    train_data = gen_data.generate_data(ground_file, num_train, distribution)
    test_data = gen_data.generate_data(ground_file, num_test, distribution)

    perceptron = Perceptron(len(train_data[0]), activation=activation.upper(), learning=learning.upper(),
                            epsilon=epsilon, alpha=1.5, theta=1.5)
    perceptron.train(train_data)
    perceptron.test(test_data)


