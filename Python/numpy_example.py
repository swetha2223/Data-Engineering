
import numpy as np

# Create a one-dimensional array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Reshape to a 2x3 array
reshaped_arr = np.arange(6).reshape(2, 3)
print("Reshaped Array:\n", reshaped_arr)

# Element-wise addition
arr_add = arr + 10
print("Added 10 to each element:", arr_add)

# Element-wise multiplication
arr_mul = arr * 2
print("Multiplied each element by 2:", arr_mul)

# Slicing arrays
sliced_arr = arr[1:4]
print("Sliced Array:", sliced_arr)



