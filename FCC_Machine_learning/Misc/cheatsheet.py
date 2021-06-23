import tensorflow as tf
# print(tf.version)

# Level 0 tensor (scalar, or just a singular value)
lvl0_tensor = tf.Variable("This is a shit tensor", tf.string)

# Level 1 tensor (basically an array (vector))
lvl1_tensor = tf.Variable([323, 231, 334], tf.int16)

# Level 2 tensor (a matrix (arrays inside an array))
lvl2_tensor = tf.Variable([[23.43, 34.23], [12.2, 1.56], [23.9, 43.5]], tf.float64)

# Determining level and type of a tensor
print(tf.rank(lvl0_tensor))

# Tensor shape - tells us how many elements we have in our tensor [lists, elements_per_list]
# ~ can also be more than 2 values depending on depth of the tensor
lvl2_tensor.shape

tensor1 = tf.ones([1, 2 ,3])    # create a tensor in a shape [1, 2, 3] and populate it with ones (1)
tensor2 = tf.reshape(tensor1, [1, 3, 2])    # makes a new shape
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension at that position (this becomes [3, 2])

# tensor can reshape only if the product of all shape numbers is same as tensor shape product, etc. [3, 2, 1] == [3, 2] == [6]
# or [2, 4, 1] == [2, 2, 2] == [8], also this product tells us the number of elements in the tensor

# Types of tensors: Variable, Constant, Placeholder, SparseTensor

# Evaluating tensors - getting the values of the tensor, which will need to run a session (not a case in TF2!!!)
with tf.compat.v1.Session() as sess:
    tensor1.eval()