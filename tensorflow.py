import tensorflow as tf // defined tf obj of tensorflow lib
hello=tf.constant("Hello World")
print('start')
sess=tf.session()
print(sess.run(hello))
print('done')
##Don't forget to load tensorflow files first.
##This program is only to check whether Tensorflow is installed in your system or not.
