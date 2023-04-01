#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input('Enter number'))
b=int(input('Enter number'))
print(a+b)


# In[2]:


a=input('ENter String:')
b=input('Enter String:')
print('Combined String:',a+b)


# In[3]:


File = open("task.txt",'w')
print(File)  #To check if the file exists or not. IF the file dosen't exist it will throw a error
File.write("Docker \n")
File.write("Ansible \n")
File.write("Linux")
File.close()

File = open("task.txt", "r+")


# In[4]:


a=input('Enter string:')
for i in range(len(a)-1,-1,-1):
    print(a[i])


# In[5]:


a=input('Enter 10 characters:')
for i in range(len(a)):
    if i==2:
        print(a[i])
    if i==7:
        print(a[i])
    


# In[ ]:





# In[ ]:




