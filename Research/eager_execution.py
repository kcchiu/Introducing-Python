# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:43:23 2018

@author: kcchi
"""

import tensorflow as tf
import tensorflow.contrib.eager as tfe

#tfe.enable_eager_execution()

#x = [[2.]]
#m = tf.matmul(x,x)
#
#print(m)
#
#print(m + 2)
#print(tf.add(m, 2))
#
#def square(x):
#    return tf.multiply(x,x)
#
#grad = tfe.gradients_function(square)
#gradgrad = tfe.gradients_function(grad)
#
#print(square(3.))
#t = grad(3.)
#print(t)
#print(gradgrad(3.))

class MNISTModel(tfe.Network):
  def __init__(self):
    super(MNISTModel, self).__init__()
    self.layer1 = self.track_layer(tf.layers.Dense(units=10))
    self.layer2 = self.track_layer(tf.layers.Dense(units=10))
  def call(self, input):
    """Actually runs the model."""
    result = self.layer1(input)
    result = self.layer2(result)
    return result

# Let's make up a blank input image
model = MNISTModel()
batch = tf.zeros([1, 1, 784])
print(batch.shape)

result = model(batch)
print(result)

def loss_function(model, x, y):
  y_ = model(x)
  return tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)

for (x, y) in tfe.Iterator(batch):
  grads = tfe.implicit_gradients(loss_function)(model, x, y)
  optimizer.apply_gradients(grads)