# Import this piece of code to check if your tensorflow is running on a GPU 
# (if you have multiple GPUs you can check if it's running on GPU you want it to run on)

import tensorflow as tf

x = tf.random.uniform([3, 3])

print("Is there a GPU available: "),
print(tf.config.list_physical_devices("GPU"))

print("Is the Tensor on GPU #0:  "),
print(x.device.endswith('GPU:0'))