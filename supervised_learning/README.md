
What is a model?
A model is a mathematical or algorithmic representation of a process, system, or relationship between variables. In machine learning, it's used to make predictions or decisions based on input data.

What is supervised learning?
Supervised learning is a type of machine learning where the model is trained on a labeled dataset, meaning each training example is paired with the correct output or label. The goal is to learn a function that maps input to output based on example input-output pairs.

What is a prediction?
A prediction is the output of a model when given new input data. It's the model's best guess of what the outcome should be, based on what it has learned from training data.

What is a node?
In the context of neural networks, a node (or neuron) is a basic computational unit that receives inputs, processes them, and passes on an output. Nodes are arranged in layers.

What is a weight?
A weight is a parameter within a neural network that adjusts how much influence one node has on another. It's multiplied by the input to modify its effect on the output of a node.

What is a bias?
A bias is another parameter in neural networks, added to the weighted sum of inputs before passing through an activation function. It allows the model to fit data better, essentially by shifting the activation function.

What are activation functions?
Activation functions determine whether a neuron should be activated or not. They introduce non-linearity into the output of a neuron, allowing the network to model complex patterns.
Sigmoid: S-shaped curve or logistic function, outputs values between 0 and 1, useful for binary classification.
Tanh: Similar to sigmoid but outputs values between -1 and 1, centered around zero, often used in hidden layers.
ReLU (Rectified Linear Unit): Outputs the input directly if positive, otherwise outputs zero. It's computationally efficient and helps mitigate the vanishing gradient problem.
Softmax: Used in multi-class classification to convert a vector of numbers into a probability distribution, ensuring the sum of all elements equals one.

What is a layer?
A layer in a neural network is a collection of nodes (neurons) that work together. Data flows through layers, each potentially transforming the data in some way.

What is a hidden layer?
A hidden layer is any layer between the input and output layers where the computations are performed, but the results are not directly seen (hence "hidden").

What is Logistic Regression?
Logistic Regression is a statistical model used for binary classification problems, where the output is transformed into a probability using the sigmoid function.

What is a loss function?
A loss function measures how well the model's predictions match the actual data. It quantifies the error for a single example.

What is a cost function?
A cost function is generally the average of the loss functions over all training examples. It's used to assess model performance across the entire dataset.

What is forward propagation?
Forward propagation is the process of computing the output of a neural network by moving forward through the layers from input to output.

What is Gradient Descent?
Gradient Descent is an optimization algorithm used to minimize the cost function by adjusting the weights and biases of the network through iterations based on the gradient of the cost function.

What is back propagation?
Back propagation is the method by which the neural network learns. It calculates the gradient of the loss function with respect to each weight by the chain rule, moving backwards from the output to the input layers.

What is a Computation Graph?
A Computation Graph is a visual way to represent how data flows through a neural network, showing how operations are connected from inputs to outputs.

How to initialize weights/biases
Initialization of weights and biases can be done in various ways (e.g., random, Xavier/Glorot initialization, He initialization) to avoid issues like vanishing or exploding gradients.

The importance of vectorization
Vectorization allows operations to be performed on entire arrays at once, significantly speeding up computations and making training more efficient, especially with large datasets.

How to split up your data
Data is typically split into:
Training set: For learning the model.
Validation set: For tuning hyperparameters and model selection.
Test set: For final evaluation of the model's performance.

What is multiclass classification?
Multiclass classification deals with more than two class labels, where the model predicts one label among several.

What is a one-hot vector?
A one-hot vector is a representation where all elements are 0 except for one, which is 1. It's used to encode categorical variables, especially in neural networks for classification.

How to encode/decode one-hot vectors
Encoding: Convert a categorical label into a one-hot vector where the index corresponding to the category is set to 1, others to 0.
Decoding: Convert the one-hot vector back to its categorical label by finding the index of 1.

What is the softmax function and when do you use it?
Softmax is used in the output layer for multi-class classification to turn logits into probabilities. It's applied when you need to assign probabilities to classes.

What is cross-entropy loss?
Cross-entropy loss measures the performance of a classification model whose output is a probability value between 0 and 1. It's particularly useful when training a multi-class classifier.

What is pickling in Python?
Pickling in Python refers to the process of serializing and deserializing a Python object structure (like a model or list) into a byte stream, which can then be saved to a file or transmitted over a network. This allows for the preservation and later retrieval or transmission of complex data structures.

