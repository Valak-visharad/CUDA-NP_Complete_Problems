
# coding: utf-8

# In[1]:


import numpy as np
from numba import cuda


# In[2]:


#INITIALIZER
x = 1024
#x = 20480
n = x * x #total elements in an integer array

original_array = np.arange(n).reshape(x, x).astype(np.float32)
#original_array


# In[3]:


threads_per_block = 128
blocks = int(x / threads_per_block)

arr = cuda.to_device(original_array)
res = cuda.to_device(np.zeros((1)))


# In[4]:


def cpu_func_(arr, m, n):
    sol = 0
    for i in range(m):
        for j in range(n):
            sol += arr[i][j]
    return sol


# In[5]:


@cuda.jit
def gpu_func_(sol, arr, x):
    idx = cuda.grid(1)
    for i in range(x):
        val = arr[i][idx]
        cuda.atomic.add(sol, 0, val)


# In[6]:


sum_from_cpu = cpu_func_(original_array, x, x)


# In[7]:


gpu_func_[blocks, threads_per_block](res, arr, x)
cuda.synchronize()

sum_from_gpu = res[0]


# # FOR CPU

# In[8]:


get_ipython().magic('timeit cpu_func_(original_array, x, x)')


# # FOR GPU

# In[9]:


get_ipython().magic('timeit gpu_func_[blocks, threads_per_block](res, arr, x)')


# # COMPARING RESULTS

# In[10]:


sum_from_cpu == sum_from_gpu


# In[11]:


print("CPU sum = ", sum_from_cpu)
print("GPU sum = ", sum_from_gpu)

