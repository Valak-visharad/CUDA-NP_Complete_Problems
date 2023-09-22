
# coding: utf-8

# In[2]:


import numpy as np
from numba import cuda


# In[4]:


#INITIALIZER
n = 2048 #total elements in an integer array

a = range(n)
#x_array = np.random.choice(a, n).astype('int32')
x_array = range(n)

cpu_y_array = np.zeros_like(x_array)
gpu_x_array = cuda.to_device(x_array)
gpu_y_array = cuda.to_device(np.zeros_like(x_array))

print(x_array, len(x_array))
print(cpu_y_array, len(cpu_y_array))
print(gpu_y_array.copy_to_host(), len(gpu_y_array))


# In[5]:


threads_per_block = 64
blocks = int(n / 64)


# In[6]:


def cpu_func_(x_arr, y_arr, n):
    for i in range(n):
        a = 0
        for j in range(i + 1):
            a += x_arr[j]
        y_arr[i] = a


# In[7]:


@cuda.jit
def gpu_func_(sol, arr):
    idx = cuda.grid(1)
    print(idx)
    a = 0
    if idx <= len(arr):
        for i in range(idx + 1):
            print(i)
            a += arr[i]
    cuda.atomic.add(sol, idx, a)


# In[8]:


cpu_func_(x_array, cpu_y_array, n)

gpu_func_[blocks, threads_per_block](gpu_y_array, gpu_x_array)
cuda.synchronize()


# # FOR CPU

# In[ ]:


get_ipython().magic('timeit cpu_func_(x_array, cpu_y_array, n)')


# # FOR GPU

# In[ ]:


get_ipython().magic('timeit gpu_func_[blocks, threads_per_block](gpu_y_array, gpu_x_array)')


# # COMPARING RESULTS

# In[ ]:


cpu_y_array == gpu_y_array


# In[ ]:


print("cpu y array = ", cpu_y_array)
print("gpu_y_array = ", gpu_y_array.copy_to_host())


# In[ ]:


for i in gpu_y_array.copy_to_host():
    print(i)

