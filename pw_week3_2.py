#Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
p_runs=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
p_runs1=sorted(p_runs,key=lambda index:index[1])
print(p_runs1)


# In[27]:


#Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l= map(lambda x:x**2,n)
print(list(l))


# In[28]:


#Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
"""Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
"""
#list of integers
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#converting items of list from int to str
k=map(lambda x:str(x),l)
print(list(k))


# In[34]:


#Q4.  Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25
import functools
l=[x for x in range(1,26)]
m=functools.reduce(lambda a,b:a*b,l)
print(m)


# In[39]:


#Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function
l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x%6==0,l))


# In[55]:


#Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
#list decleration
l=['python', 'php', 'aba', 'radar', 'level']
#finding palindrome in given list
list(filter(lambda a:a==a[-1::-1],l))


# In[ ]:




