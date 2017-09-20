import activation as a
import utility.vector_utils as vutil
from utility import constants


class Perceptron:

    def __init__(self, n, learning=constants.PERCEPTRON, activation=constants.THRESHOLD, epsilon=0.2, alpha=0, theta=0):
        self.n = n
        self.learning = learning.upper()
        self.activation = activation.upper()
        self.epsilon = epsilon
        self.alpha = alpha
        self.theta = theta

        # Activation function object selection
        if self.activation == constants.THRESHOLD:
            self.activation_fn = a.threshold_activation
        elif self.activation == constants.TANH:
            self.activation_fn = a.tanh_activation
        elif self.activation == constants.RELU:
            self.activation_fn = a.relu_activation

    def train(self, train_data):
        """
        Trains the perceptron by using the learning and activation specified in the model.
        :param train_data: array of training data vectors. Each vector of length 'n'
        :return: weight vector and theta.
        """
        print(" ===Training=== ")

        # Training method selection
        if self.learning == constants.PERCEPTRON:
            self._perceptron_train(train_data)
        elif self.learning == constants.WINNOW:
            self._winnow_train(train_data)

    def test(self, observation):

        """
        Tests the given observation against the perceptron model and returns the activation result
        :param observation: test vector of length 'n'
        :return: activation function result
        """
        print(" ===Testing=== ")
        stout_format = "{}:{}:{}:{}"
        total_error = 0
        for x, actual in observation:
            prediction = self.activation_fn(vutil.dot_product(x, self.w), self.theta)
            error = abs(actual-prediction)
            total_error += error
            print(stout_format.format(vutil.vector_to_string(x), prediction, actual, error))

        average_error = (total_error*1.0)/len(observation)
        print("Average Error : ", average_error)
        print("Epsilon : ", self.epsilon)
        if average_error <= self.epsilon:
            print("TRAINING SUCCEEDED")
        else:
            print("TRAINING FAILED")

    def _perceptron_train(self, train_data):

        # Initialization
        self.w = [0]*self.n
        self.theta = 0
        stout_format = "{}:{}:[{}]"
        for x, actual in train_data:
            prediction = self.activation_fn(vutil.dot_product(x, self.w), self.theta)

            if (prediction - actual) > 0:
                # False Positive
                self.w = vutil.vector_difference(self.w, x)
                self.theta += 1
                print(stout_format.format(vutil.vector_to_string(x), actual, "update"))
            elif (prediction - actual) < 0:
                # False Negative
                self.w = vutil.vector_sum(self.w, x)
                self.theta -= 1
                print(stout_format.format(vutil.vector_to_string(x), actual, "update"))
            else:
                # Correct prediction
                print(stout_format.format(vutil.vector_to_string(x), actual, "no update"))

            #print("Summary of iteration:\n Weight: {}\n Theta{}\n".format(vutil.vector_to_string(self.w), self.theta))

    def _winnow_train(self, train_data):
        """
        Winnow update rule implementation
        :return: Updated weight vector and theta
        """
        # Initialization
        self.w = [1] * self.n
        if self.theta < 0 or self.alpha < 1:
            print("Alpha and Theta values should be greater than 1 for winnow training")
        else:
            stout_format = "{}:{}:[{}]"
            for x, actual in train_data:
                prediction = self.activation_fn(vutil.dot_product(x, self.w), self.theta)

                if (prediction - actual) > 0:
                    # False Positive
                    negative_exp = [self.alpha ** -xi for xi in x]
                    self.w = vutil.vector_product(self.w, negative_exp)
                    print(stout_format.format(vutil.vector_to_string(x), actual, "update"))
                elif (prediction - actual) < 0:
                    # False Negative
                    negative_exp = [self.alpha ** xi for xi in x]
                    self.w = vutil.vector_product(self.w, negative_exp)
                    print(stout_format.format(vutil.vector_to_string(x), actual, "update"))
                else:
                    # Correct prediction
                    print(stout_format.format(vutil.vector_to_string(x), actual, "no update"))
                #print("Summary of iteration:\n Weight: {}\n Theta{}\n".format(vutil.vector_to_string(self.w), self.theta))


