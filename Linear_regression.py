import tensorflow as tf
# X and Y data
#x_train = [1,2,3]
#y_train = [1,2,3]
#use PlaceHold

W = tf.Variable(tf.random_normal([1]), name = 'weight')

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Our hypothesis W*X
hypothesis = W * X

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#Minimize
#Black Box
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

#Launch the graph in a session.
sess = tf.Session()
#Initializes global variable in the graph.
sess.run(tf.global_variables_initializer())

#Fir the Line
for step in range(2001):
	cost_val, W_val, _ = \
		sess.run([cost, W,train],
			feed_dict={X: [1, 2, 3, 4, 5],\
				 Y: [2, 4, 6, 8, 10]})
	if step % 20 == 0:
		#Print step and Cost val, W val
		print(step,cost_val,W_val)
#Over training Print hypothesis when X is 7
print(sess.run(hypothesis, feed_dict={X:[7]}))
