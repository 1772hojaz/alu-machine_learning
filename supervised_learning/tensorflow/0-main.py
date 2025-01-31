#!/usr/bin/env python3

import tensorflow as tf

create_placeholders = __import__('0-create_placeholders').create_placeholders

x, y = create_placeholders(784, 10)
print(x)
print(y)
ubuntu@alexa-ml:~/tensorflow$ ./0-main.py 
Tensor("x:0", shape=(?, 784), dtype=float32)
Tensor("y:0", shape=(?, 10), dtype=float32)
