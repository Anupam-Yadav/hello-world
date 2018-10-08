import tensorflow as tf
hello=tf.constant("Hello World")
sess=tf.session()
print(sess.run(hello))
print('done')
##Don't forget to load tensorflow files first. This program is only to check whether Tensorflow is installed in your system or not.
