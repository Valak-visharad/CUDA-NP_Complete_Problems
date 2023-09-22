
# coding: utf-8

# In[49]:


import numpy as np
from numba import cuda


# In[5]:


threads_per_block = (64, 64)
blocks = (int(x / 64), int(x / 64))


# In[51]:


#INITIALIZER
x = 1024
#x = 20480
n = x * x #total elements in an integer array

original_array = np.arange(n).reshape(1024, 1024).astype(np.int32)
cpu_res = np.zeros_like(original_array).astype(np.int32)
gpu_res = np.zeros_like(original_array).astype(np.int32)

arr = cuda.to_device(original_array)
gpu_res = cuda.to_device(gpu_res)


# In[6]:


def cpu_func_(sol, arr, m, n):
    for i in range(m): #no. of rows
        for j in range(n): #no. of half columns
                       sol[i][j] = arr[i][n - j - 1]


# In[25]:


@cuda.jit
def gpu_func_(sol, arr, n):
    share = cuda.shared.array((64, 65), numba_types.int32) #shared memory bank conflict handled
    x, y = cuda.grid(2)
    share[y][x] = arr[y][x] #copying element wise into shared memory from global
    cuda.syncthreads()
    sol[y][n - x] = share[y][x] #copying back to output array via shared memory


# In[55]:


cpu_func_(cpu_res, original_array, x, x)


# In[26]:


gpu_func_[blocks, threads_per_block](gpu_res, arr, x)
cuda.synchronize()

sum_from_gpu = res[0]


# # FOR CPU

# In[45]:


get_ipython().magic('timeit cpu_func_(cpu_res, original_array, x, x)')


# # FOR GPU

# In[52]:


get_ipython().magic('timeit gpu_func_[blocks, threads_per_block](gpu_res, arr, x);')


# # COMPARING RESULTS

# In[53]:


cpu_res == gpu_res


# In[56]:


print("CPU swapped array = \n", cpu_res)
print("GPU swapped array = \n", gpu_res.copy_to_host())

