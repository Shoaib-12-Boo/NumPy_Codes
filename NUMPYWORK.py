# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 04:41:55 2021

@author: SHOAIB SHAFIQUE
"""

# In[01]:


import numpy as np


# # type


# In[02]:


arr=np.array([1,2,3,4,5])
print (arr)
print(type(arr))  #type(): This built-in Python function tells us the type of the object passed to it.


# # 0-D Arrays
##################################


# In[03]:


arr=np.array(42)
print(arr)


# # 1-D Array
##############################

# In[04]:


arr=np.array([1,2,3,4,5])
print(arr)

################################


# In[05]:


a=np.array(42)
b=np.array([1,3,4,5])
c=np.array([[1,2,3,4],[6,7,8,8]])
d=np.array([[[6,7,7,8], [3,6,6,7]], [[5,5,6,7], [6,5,3,5]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#######################################

# In[06]:


at=np.array([1,2,4,5], ndmin=5)
print(at)
print(at.ndim)


# # Array indexing

#########################################

# In[07]:


arr=np.array([1,2,3,4,5,6])
print(arr[0])


# # Accessing 2-dimentional 

########################## 


# In[08]:


arr=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr[0,1])

#################

# In[09]:


a=np.array([[0,1,2],[3,4,5],[6,7,8]])
b=np.array([[0,2,4],[6,8,10],[12,14,16]])
print(np.concatenate((a,b),axis=1))

############

# In[10]:


a=np.array([[0,1,2,45],[3,4,5,7],[6,7,8,8]])
b=np.array([[0,2,4,47],[6,8,10,9],[12,14,16,7]])
print(np.dstack((a,b)))

################

# In[11]:


a=np.array([[0,1,2],[3,4,5],[6,7,8]])
b=np.array([[0,2,4],[6,8,10],[12,14,16]])
print(np.vstack((a,b)))

##############

# In[12]:


a=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(np.hsplit(a,3))

############################

# In[13]:


a=np.arange(10).reshape(2,-1)
b=np.repeat(1,10).reshape(2,-1)
print(np.concatenate([a,b],axis=0))

#####################

# In[14]:


a=np.arange(10).reshape(2,-1)
b=np.repeat(1,10).reshape(2,-1)
print(np.vstack([a,b]))

#######################

# In[15]:


arr=np.array([0,1,2,3,4,5,6,7,8,9])
arr[arr%2==1]=-1
print(arr)

####################

# In[16]:


print(np.arange(9,-1,-1))

#########################

# In[17]:


arr=np.arange(10)
arr_slice=arr[8:5]
arr_slice[:]=69
print(arr)

################################

# In[18]:


a=np.array([[0,1,2],[3,4,5],[6,7,8]])
b=np.array([[0,2,4],[6,8,10],[12,14,16]])
print(np.concatenate((a,b),axis=0))

##################################

# In[19]:


arr=np.array([67.98,-10.25,-22.06,0.5,12.90,10.10])
print(arr.astype(np.int32))

########################################

# In[20]:


a=np.array([[0,1,2],[3,4,5],[6,7,8]])
b=np.array([[0,2,4],[6,8,10],[12,14,16]])
print(np.concatenate((a,b),axis=1))

###############################


# In[21]:


arr=[0.3490,-1.4545,1.204,-97152,11.43,-0.8439]
arr.sort()
print(arr)

######################################


# In[22]:


arr=np.array([1,2,3,4,5,6,7,8,9])
arr=np.arange(10)
print(arr.reshape(2,-1))

#######################################

# In[23]:


a=np.array([0,1])
b=np.array([0,2])
print(np.column_stack((a,b)))

################################

