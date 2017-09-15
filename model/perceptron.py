import activation as a
class Perceptron:
    def __init__(self, n, learning="PERCEPTRON", activation="TANH"):
        self.n = n
        self.learning = learning
        self.activation = activation

    def train(self, train_data):
        """
        Trains the perceptron by using the learning and activation specified in the model.
        :param train_data: array of training data vectors. Each vector of length 'n'
        :return: weight vector and theta.
        """
        print("Training method")

    def test(self, observation):
        """
        Tests the given observation against the perceptron model and returns the activation result
        :param observation: test vector of length 'n'
        :return: activation function result
        """
        print("Testing method")

    def _winnow_update(self):
        """
        Winnow update rule implementation
        :return: Updated weight vector and theta
        """

    def _perceptron_update(self):
        """
        Perceptron update rule implementation
        :return: Updated weight vector and theta
        """


