#!/usr/bin/env python
# coding: utf-8

# In[1]:
Task 1:

a=int(input('Enter number'))
b=int(input('Enter number'))
print(a+b)
Enter number1
Enter number2
3


# In[2]:

Task 2:
a=input('ENter String:')
b=input('Enter String:')
print('Combined String:',a+b)
O/P:
ENter String:avane
Enter String:eesh
Combined String: avaneeesh


# In[3]:

Task 3:
File = open("task.txt",'w')
print(File)  #To check if the file exists or not. IF the file dosen't exist it will throw a error
File.write("Docker \n")
File.write("Ansible \n")
File.write("Linux")
File.close()

File = open("task.txt", "r+")
O/P:<_io.TextIOWrapper name='task.txt' mode='w' encoding='cp1252'>

# In[4]:

Task 4:
a=input('Enter string:')
for i in range(len(a)-1,-1,-1):
    print(a[i])
O/P:
Enter string:abcd
d
c
b
a

# In[5]:

Task 5:
a=input('Enter 10 characters:')
for i in range(len(a)):
    if i==2:
        print(a[i])
    if i==7:
        print(a[i])
 
O/P:
Enter 10 characters:abcdefghij
c
h


# In[ ]:





# In[ ]:




