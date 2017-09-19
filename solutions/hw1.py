from model.perceptron import Perceptron
from utility import gen_data
from utility import constants

ground_file = 'D:\SJSU\Fall17\CS256\NeuralNetwork\sample_function_2'
train_data = gen_data.generate_data(ground_file, 30, 'bool')
test_data = gen_data.generate_data(ground_file, 15, 'bool')

#perceptron = Perceptron(3, activation=constants.THRESHOLD, learning=constants.WINNOW, epsilon=0.2, alpha=1.5, theta=1.5)
perceptron = Perceptron(3, activation=constants.THRESHOLD, learning=constants.PERCEPTRON, epsilon=0.2)

perceptron.train(train_data)
perceptron.test(test_data)


