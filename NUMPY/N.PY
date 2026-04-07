import numpy as np

def array(*args, **kwargs):
    return np.array(*args, **kwargs)
def zeros(*args, **kwargs):
    return np.zeros(*args, **kwargs)
def ones(*args, **kwargs):
    return np.ones(*args, **kwargs)
def arange(*args, **kwargs):
    return np.arange(*args, **kwargs)
def linspace(*args, **kwargs):
    return np.linspace(*args, **kwargs)
def reshape(*args, **kwargs):
    return np.reshape(*args, **kwargs)
def transpose(*args, **kwargs):
    return np.transpose(*args, **kwargs)
def dot(*args, **kwargs):
    return np.dot(*args, **kwargs)
print("Numpy functions have been imported and are ready to use.")
print("You can use array(), zeros(), ones(), arange(), linspace(), reshape(), transpose(), and dot() functions from this module.")
print("Example usage:")
print(array([1, 2, 3]))
print(zeros((2, 3)))
print(ones((3, 4)))
print(arange(0, 10, 2))
print(linspace(0, 1, 5))
print(reshape(array([1, 2, 3, 4]), (2,
    2)))                    
print(transpose(array([[1, 2], [3, 4]])))
print(dot(array([[1, 2], [3, 4]]), array([[5
, 6], [7, 8]])))        

    