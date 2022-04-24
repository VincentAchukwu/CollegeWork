# tensor tutorial

import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data, "\n")

# numpy to tensor
np_array = np.array(data)
print(np_array, "\n")
x_np = torch.from_numpy(np_array)
print(x_np, "\n")

# retains the properties of x_data
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

# overrides the datatype of x_data
x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

# shape is a tuple of tensor dimensions. In the functions below, 
# it determines the dimensionality of the output tensor
shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# Tensor attributes describe their shape, datatype, and the device on which they are stored.
tensor = torch.rand(3, 4)

print(f"Shape of tensor: \n {tensor.shape} \n")
print(f"Datatype of tensor: \n {tensor.dtype} \n")
print(f"Device tensor is stored on: \n {tensor.device} \n")

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
    print(f"Device tensor is stored on: \n {tensor.device} \n")

# Standard numpy-like indexing and slicing
tensor = torch.ones(4, 4)
tensor[:,1] = 0
print(tensor, "\n")

# use torch.cat to concatenate a sequence of tensors along a given dimension
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1, "\n")

# multiplying tensors
# This computes the element-wise product
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
# Alternative syntax:
print(f"tensor * tensor \n {tensor * tensor} \n")

# This computes the matrix multiplication between two tensors
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# Alternative syntax:
print(f"tensor @ tensor.T \n {tensor @ tensor.T} \n")

# Operations that have a _ suffix are in-place operations. 
# For example: x.copy_(y), x.t_(), will change x.
print(tensor, "\n")
tensor.add_(5)
print(tensor, "\n")

# Tensor to NumPy array
t = torch.ones(5)
print(f"t: {t} \n")
n = t.numpy()
print(f"n: {n} \n")

# A change in the tensor reflects in the NumPy array.
t.add_(1)
print(f"t: {t} \n")
print(f"n: {n} \n")

# again, numpy to tensor
n = np.ones(5)
t = torch.from_numpy(n)

# changes in numpy reflected in tensor
np.add(n, 1, out=n)
print(f"t: {t} \n")
print(f"n: {n} \n")
