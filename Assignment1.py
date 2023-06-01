q1= "Create one variable containing following type of data:"
print(q1)
print("q1 answers")
#i)	string
a="Ajeet"
print("1",type(a))

#(ii)	list
li=[1,2,3,4,"a","b"]
print("2",type(li))

#(iii)	float
d=3.5
print("3",type(d))

#(iv)	tuple
t=(1,2,3,4,5,6)
print("4",type(t))

#==============================================================================================
q2=" Given are some following variables containing data \n What will be the data type of the above given variable"
#(i)	var1 = ‘ ‘

#(ii)	var2 = ‘[ DS , ML , Python]’

##(iii)	var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]

#(iv)	var4 = 1
#What will be the data type of the above given variable

#answers

ans1= "1= string"
ans2= "2= string"
ans3= "3= list"
ans4="4= float"
print(q2)
print("answers q2")
print(ans1)
print(ans2)
print (ans3)
print(ans4)
#=======================================================================
"""
Q3. Explain the use of the following operators using an example:

(i)	/

(ii)	% 

(iii)	//

(iv)	**
"""
#==========================================================================
print("Q3. Explain the use of the following operators using an example:")
print("ansq3")
print("/ is division operator and provide float as output")
print("part 1  example  suppose x has 24 rs and want to know how much pencils can it purchase each cost 2 rs")
x=24
y=2
print("it can purchase ", x/y ,"pencils")
print()
print("% this modulo operator and used to get remainder of a devision ")
print("part 2 example suppose we want to know how much money is left with x on purchasing pencils of above example ")

print("answer", "he was left with ",x%y,"rs")
print()

print("part3  this is // is the floor division operator that returns an integer quotient by rounding down to the nearest integer")
print("let m=5 and n=2 ")
m=5
n=2
print(5//2)
print("5//2 will return 2  and 5/2 will return 2.5" ,)
print()
print("part 4 In Python, ** is used for exponentiation ")
print("let m=5 & n=2 what will be square of m")
print(m**n)
print()
#=========================================================================================
print("Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the element and its data type.")
print("ans q4")
l=[1,2.0,4+3j,["a","b"],(1,2,3),{1,2,3,3,4},{"a":1,"b":2},"ajeet" ,"singh",43]
for i in l:
    print(i,type(i))

#===========================================================
print()
print("Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.")
A=int(input())
B=int(input())
c=0
while A>=B:
    A=A-B
    c+=1
print(c)

print()
#==================================================================
print("Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not. ")
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(l)
for i in l:
    if (i%3==0):
        print(i," is divisible by 3  " )
    else:
        print(i ,"NOt divisible by 3")
print()
print("Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property")
""" Every variable in Python holds an instance of an object. 
There are two types of objects in Python i.e. Mutable and Immutable objects. 
Whenever an object is instantiated, it is assigned a unique object id. 
The type of the object is defined at the runtime and it can’t be changed afterwards.
 However, its state can be changed if it is a mutable object. 
 To summarise the difference, mutable objects can change their state or contents and immutable objects can’t change their state or content."""
l1=[1,2,3,4]
l1[1]=7
print("mutable ojects are list ,dictionary ,set etc ")
tu=(1,2,3,4)
s="ajrrt"
print("imutable data types string , tuple etc ")