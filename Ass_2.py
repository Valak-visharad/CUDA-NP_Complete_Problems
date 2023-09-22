
# coding: utf-8

# In[1]:


import numpy as np
from numba import cuda


# In[2]:


#INITIALIZER
n = 2048 #total elements in an integer array

a = range(1000)
original_array = np.random.choice(a, n).astype('int32')

print(original_array)


# In[3]:


threads_per_block = 64
blocks = 256

res = cuda.to_device(np.array([original_array[0], original_array[0]], dtype = np.int32))
arr = cuda.to_device(original_array)


# In[4]:


def cpu_func_(arr, n):
    sol = [arr[0], arr[0]]
    for i in range(n):
        if (sol[1] > arr[i]): #sol[1] is to hold min
            sol[1] = arr[i]
        elif(sol[0] < arr[i]): #sol[0] is to hold max
            sol[0] = arr[i]
    return [sol[0], sol[1]]


# In[5]:


@cuda.jit
def gpu_func_(sol, arr, n):
    i = cuda.grid(1)
    stride = cuda.gridsize(1)
    for i in range(i, n, stride):
        cuda.atomic.max(sol, 0, arr[i])
        cuda.atomic.min(sol, 1, arr[i])


# In[6]:


max1_, min1_ = cpu_func_(original_array, len(original_array))

gpu_func_[blocks, threads_per_block](res, arr, len(original_array))
cuda.synchronize()

max2_ = res[0]
min2_ = res[1]


# # FOR CPU

# In[7]:


get_ipython().magic('timeit cpu_func_(original_array, len(original_array))')


# # FOR GPU

# In[8]:


get_ipython().magic('timeit gpu_func_[blocks, threads_per_block](res, arr, len(original_array))')


# # COMPARING RESULTS

# In[9]:


max2_ == max1_


# In[10]:


min2_ == min1_


# In[11]:


print("MAXIMUM = ", max1_, max2_)
print("MINIMUM = ", min1_, min2_)

