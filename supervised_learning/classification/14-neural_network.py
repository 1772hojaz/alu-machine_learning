    def train(self, X, Y, iterations=5000, alpha=0.05):
        '''
            Trains the neural network using gradient descent
        '''
        if type(iterations) is not int:
            raise TypeError('iterations must be an integer')

        if iterations < 1:
            raise ValueError('iterations must be a positive integer')

        if type(alpha) is not float:
            raise TypeError('alpha must be a float')

        if alpha < 0:
            raise ValueError('alpha must be positive')

        costs = []
        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            cost = self.cost(Y, A2)
            costs.append(cost)
            self.gradient_descent(X, Y, A1, A2, alpha)

        # evaluate the gradient descent
        evaluation = self.evaluate(X, Y)
        return evaluation
