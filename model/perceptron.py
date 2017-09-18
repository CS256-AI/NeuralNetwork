import activation
import utility.vector_utils as vutil


class Perceptron:

    def __init__(self, n, epsilon=0.2, learning="PERCEPTRON", activation = "THRESHOLD"):
        self.n = n
        self.learning = learning.upper()
        self.activation = activation.upper()
        self.epsilon = epsilon

        # Activation function object selection
        if self.activation == "THRESHOLD":
            self.activation_fn = activation.threshold_activation
        elif self.activation == "TANH":
            self.activation_fn = activation.tanh_activation
        elif self.activation == "RELU":
            self.activation_fn = activation.relu_activation

    def train(self, train_data, theta=0, alpha=0):
        """
        Trains the perceptron by using the learning and activation specified in the model.
        :param train_data: array of training data vectors. Each vector of length 'n'
        :param theta: required for winnow training method
        :param alpha: required for winnow training method
        :return: weight vector and theta.
        """
        print("Training method")

        # Training method selection
        if self.learning == "PERCEPTRON":
            self._perceptron_train(train_data)
        else:
            self._winnow_train(train_data, theta, alpha)

    def test(self, observation):

        """
        Tests the given observation against the perceptron model and returns the activation result
        :param observation: test vector of length 'n'
        :return: activation function result
        """
        print("Testing method")
        stout_format = "{}:{}:{}:{}"
        total_error = 0
        for test_data in observation:
            prediction = self.activation_fn(vutil.dot_product(test_data, self.w), self.theta)
            actual = activation.ground_truth(test_data)  # Should be replaced with actual ground truth function
            error = abs(actual-prediction)
            total_error += error
            print(stout_format.format(",".join(test_data), prediction, actual, error))

        average_error = (total_error*1.0)/len(test_data)
        print("Average Error : ", average_error)
        print("Epsilon : ", self)
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

            if actual == 0 and prediction == 1:
                # False Positive
                self.w = vutil.vector_difference(self.w, x)
                self.theta += 1
                print(stout_format.format(",".join(x), prediction, "update"))
            elif actual == 1 and prediction == 0:
                # False Negative
                self.w = vutil.vector_sum(self.w, x)
                self.theta -= 1
                print(stout_format.format(",".join(x), prediction, "update"))
            else:
                # Correct prediction
                print(stout_format.format(",".join(x), prediction, "no update"))


    def _winnow_train(self, train_data, theta, alpha):
        """
        Winnow update rule implementation
        :return: Updated weight vector and theta
        """
        # Initialization
        self.w = [0.2] * self.n
        self.theta = theta
        self.alpha = alpha
        stout_format = "{}:{}:[{}]"
        for data in train_data:
            prediction = self.activation_fn(vutil.dot_product(data, self.w), self.theta)
            actual = activation.ground_truth(data)  # Should be replaced with actual ground truth function

            if actual == 0 and prediction == 1:
                # False Positive
                self.w = vutil.vector_difference(self.w, data)
                self.theta += 1
                print(stout_format.format(",".join(data), prediction, "update"))
            elif actual == 1 and prediction == 0:
                # False Negative
                self.w = vutil.vector_sum(self.w, data)
                self.theta -= 1
                print(stout_format.format(",".join(data), prediction, "update"))
            else:
                # Correct prediction
                print(stout_format.format(",".join(data), prediction, "no update"))
