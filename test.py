import tensorflow as tf
print(tf.__version__)
sess = tf.Session()
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
c = a * b
print(sess.run(c))
sess.close()