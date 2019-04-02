import tensorflow as tf

X = tf.placeholder(tf.int32, [None, 5])

with tf.Session() as sess:
    with tf.device("/cpu:0"):
        sess.run(tf.global_variables_initializer())
        print(sess.run(X, feed_dict={X: [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]}))

print(X)
