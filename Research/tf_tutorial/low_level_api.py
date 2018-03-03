# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:39:06 2018

@author: kcchi
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

my_data = [
    [0, 1,],
    [2, 3,],
    [4, 5,],
    [6, 7,],
]

#my_data = np.random.uniform(size=[10,2])

def map_function(x):
    return x + 1

slices = tf.data.Dataset.from_tensor_slices(my_data)
slices = slices.map(map_function)
next_item = slices.make_one_shot_iterator().get_next()

x = tf.constant([[1], [2], [3], [4]], dtype=tf.float32)
y_true = tf.constant([[0], [-1], [-4], [-9]], dtype=tf.float32)

y_pred = tf.layers.dense(x, units=1, activation=tf.nn.sigmoid)
y_pred = tf.layers.dense(y_pred, units=1)

#y_pred = linear_model(x)

loss = tf.losses.mean_squared_error(labels=y_true, predictions=y_pred)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(loss)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(20000):
    _, t_loss = sess.run((train,loss))
    print(t_loss)
    
print(sess.run(y_pred))

#print(sess.run(y, {x:[[1, 2, 3],[4, 5, 6]]}))

#print(sess.run(next_item))

#while True:
#  try:
#    print(sess.run(next_item))
#  except tf.errors.OutOfRangeError:
#    break


writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())