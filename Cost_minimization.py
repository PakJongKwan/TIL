import tensorflow as tf
#set Data
x_data = [1,2,3]
y_data = [1,2,3]

W = tf.Variable(tf.random_normal([1]),name = 'weight')
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = X * W

cost = tf.reduce_sum(tf.square(hypothesis - Y))

#decide learning_rate
learning_rate = 0.1

gradient = tf.reduce_mean((hypothesis -Y) * X)
descent = W - learning_rate * gradient
#input descent at W
update = W.assign(descent)

sess = tf.Session()

sess.run(tf.global_variables_initializer())
for step in range(30):
    #run tensors
    sess.run(update, feed_dict={X: x_data, Y: y_data})
    print(step, sess.run(cost, feed_dict={X:x_data,Y:y_data}),sess.run(W))
