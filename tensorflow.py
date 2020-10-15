from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow method
try:
  # %tensorflow_version only exists in Colab.
  %tensorflow_version 2.x
except Exception:
  pass

##import tensorflow as tf

import tensorflow as tf ## defined tf obj of tensorflow lib
hello=tf.constant("Hello World")
print('start')
sess=tf.session()
print(sess.run(hello))
print('done')
##Don't forget to load tensorflow files first.
##This program is only to check whether Tensorflow is installed in your system or not.
