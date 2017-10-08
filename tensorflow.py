import tensorflow as tf
hello=tf.constant("Hello World")
sess=tf.session()
print(sess.run(hello))
