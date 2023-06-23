#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
'''
def keyboard is used to  create function
In Python, a function is a block of code that performs a specific task or a group of related tasks.
You can define your own functions in Python using the def keyword. 

syntax for function creation
def function_name(parameters):
    """docstring"""
    statement(s)
    
Here is what each part of the function definition means:
def: This keyword tells Python that you are defining a function.

function_name: This is the name of your function.You can choose any name you like as long as it follows the rules for naming variables in Python.

parameters: These are the inputs to your function. You can have zero or more parameters.

#docstring: This is an optional string that describes what your function does. It should be included immediately after the function definition and enclosed in triple quotes.

statement(s): These are the statements that make up the body of your function. They should be indented by four spaces.
'''

def odd_num(a,b):
    l=[]
    for i in range (int(a),int(b)+1,1):
        if (i%2)!= 0:
            l.append(i)
        else:
            continue
    return l
#calling function for output
odd_num(1,25)


# In[2]:


#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
"""Special Symbols Used for passing arguments in Python:
*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
1:- args
The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function.
It is used to pass a non-keyworded, variable-length argument list. 
The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, 
run some higher-order functions such as map and filter, etc
Exapmple """
print("Example of * args")
def addition(*num):
    sum_ = 0
    
    for n in num:
        sum_ = sum_ + n

    print("Sum:",sum_)

addition(3,5)
addition(4,5,6,7,8)
addition(1,2,3,5,9,12)

"""
The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list.
We use the name kwargs with the double star.
The reason is that the double star allows us to pass through keyword arguments (and any number of them).

#A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{}  {}".format(key,value))

intro(Firstname="Ajeet", Lastname="Singh", Age=25, Phone=9473535356)
intro(Firstname="John", Lastname="Wood", Email="johnwood@gmail.com", Country="usa", Age=27, Phone=889999797)


# In[5]:


"""Q3.  What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration.
Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
"""

print("answers")

"""
An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets . 
The Python iterators object is initialized using the iter() method. It uses the next() method for iteration .

The __iter__() method is called for the initialization of an iterator. This returns an iterator object .
The __next__() method returns the next value for the iterable .

Here is an example of how to use an iterator in Python:

"""
# Define a list
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Get an iterator object
my_iterator = iter(my_list)

# Iterate over the list using the iterator
for i in range(5):
    print(next(my_iterator)) # Output: 1



# In[6]:


#Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator function
"""In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
Generators are useful when we want to produce a large sequence of values,
  but we don't want to store all of them in memory at once.
In Python, similar to defining a normal function, we can define a generator function using the def keyword, 
but instead of the return statement we use the yield statement.
def generator_name(arg):
    # statements
    yield something
    
Here, the yield keyword is used to produce a value from the generator.
When the generator function is called, it does not execute the function body immediately. 
Instead, it returns a generator object that can be iterated over to produce the values.

The yield keyword is used to produce a value from the generator 
and pause the generator function's execution until the next value is requested.
"""
def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(10):

    # print each value produced by generator
    print(value)


# In[4]:


#Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers
def prime(a,b):
        
    for i in range(a,b):
        if i==2 or i==3 :
            yield i
        else:
            n=(i+1)/2
            flag = False
            for j in range(2,int(n)):
                if i%j==0 :
                    flag=False
                    break
                else:
                    flag=True
            if flag==True:
                yield i
primme=prime(1,1000)
for i in range(20):
    print(next(primme),end=" ,")
    
    


# In[13]:


#Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
n=1
a=1
b=0
feb=0
while n <= 10:
    print(feb,end=" ,")
    feb=a+b
    b=a
    a=feb
    n+=1
    


# In[16]:


#Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’. Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
x="pwskills"
list1=[x for x in x]
print(list1)


# In[31]:


#Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.
def check_palindrome(n):
    #converting n  into string
    x=str(n)
    i=1
    flag=False
    while i <= (len(x)//2):
        #comparing 1st and last element
        if x[i-1]==x[-i]:
            flag=True
        else:
            flag=False
        i+=1
    return flag

#checking condition
print(check_palindrome(132432))
print(check_palindrome(12321))


# In[33]:


#Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
#Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter out odd numbers.

num=[x for x in range(1,101)]
print(num)
odd=[x for x in num if x%2 !=0]
print(odd)


# In[ ]:




