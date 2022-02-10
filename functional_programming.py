"""
Created on Fri Feb 19 11:22:56 2021

@author: Pranav Kumaar
@pranavkumaarofficial

This file Contains:
    LAMBDA
    MAP
    REDUCE
    FILTER
    ZIP
    List COMPREHENSION
"""
'''
FUNCTIONAL PROGRAMMING

methods to make functions easier and effective

'''

#Lambda
#map()
#filter()
#Reduce()

################################################################################
'''
Lambda function :
    It is an anonymous function
    Wherever only one statement is to be executed
    there lambda function is useful
we basically make the concept of functions a bit easier
we need not use 'def' and stuff like that
Just make the lambda equal to a variable
That variable will be a function
eg :
    b=lambda a,b : a+b
    print(b(10,20))

Note : lambda keyword L is lower case
       And no brackets for lambda function
'''
b=lambda a,b:a+b
print(b(10,20))

output= lambda s:print('output :'+s)
output("Yes")

#to upper case
toUpper= lambda s:print(s.upper())
toUpper("hello ppl ")

################################################################################

'''
MAP function:
    It is a built in function
map function applies a 'passed in' function to each item in an iterable object
and returns a list containing all function call results
    Takes in 2 arguments:
        the callable and the iterable
    It is Lazy Function meaning we need to call it explicitly
    Thats why we use list(map()) and syntax it like that

    NOTE:::::
    Number of input elements is always equal to number of output elements



    It performs and keeps it to itself it doesnt give it to us
    syntax:
        map(function,argument)

        See here the function can be any function like len max min str.upper etc

        #the function needs to be predefined or user defined

'''



counters=[1,2,3,4]
def inc(x):
    return x+10
print(list(map(inc,counters)))
print()
#can also be written as:
print(list(map(lambda x:x+10,counters)))

################################################################################


print(list(map(lambda x:x**3 , counters)))



'''
*******************************************
Filter :
    Map takes in number of input elements ::::Output is the same number of elements as input

    Filter helps in getting out only required number of output

    syntax:
        filter(callable,iterable)

    Filter as the name suggests it filters out the elements and gives a required output

    Generally one callable is mostly a lambda function
'''
#to print even numbers from 0 to 5
print(list(filter(lambda x:x%2==0,range(5))))
'''
#NOTEEEE::::
    If filter is changed to map we get output as true and false as the map function maps all the elements to the callable
    '''
l=(list(range(-5,5)))
print(l)
print(list(filter(lambda x:x>0,l)))
#callable needs to be a true false type
#here the lambda returns the true statements for x>0 ie the positive
#integers in the list

################################################################################


'''
REDUCE :
    accepts iterator but it isnt an iterator itself
    we need to import from functools

    reduces the iterator into a 2 membered object
    refer notes for the syntax as to how it executes

reduce(callable,iterable)
'''

import operator,functools

from functools import reduce

print(reduce((lambda x,y:x+y),[1,2,3,4]))
print(reduce((lambda x:print(x)),[20]))#iterable stored in list form
#it doesnt take integer iterables


l=[1,2,3,4,5,6]
print(reduce(operator.add,l))

l=functools.reduce(operator.add,[2,4,6])
print(l)
l=functools.reduce(int.__add__,[2,4,6])
print(l)

l=[1,2,3,4,5,6]

print(reduce(lambda x,y:x*y,l))

#good question
#Can be asked

l1=["Raja","Ram","Mohan","Roy"]

print(reduce(lambda x,y:str(x)+str(" ")+str(y),l1,"sir"))#sir gets added in the first

print(reduce(lambda x,y:x if len(x)>len(y) else y,l1))
#print(reduce(max(key=lambda:len(x))))
#print(reduce(max(l1,key=len),l1))

#user defined reduce
def MyReduce(func,seq,initial):
    if initial==None:
        res=seq[0]
    else:
        res=initial
        res=func(res,seq[0])


    for i in seq[1:]:
        res=func(res,i)

    return res

'''

def Myreduce(func,seq):

    for i in seq:

        res=func(res,i)

    return res
'''
l=[1,2,3,4,5]


print(MyReduce(int.__add__,l,None))
#print(Myreduce(int.__add__,l))

print(reduce(int.__add__,l))


################################################################################


"""
Created on Fri Feb 19 12:48:59 2021

@author: Pranav Kumaar
@pranavkumaarofficial
"""

'''
ZIP
'''
'''
Zip function :

    For zip one argument is mandatory rest isnt

    merges 2 lists, tuples, i.e iterables in general

    As usual as expected zip is also a lazy mf
    so we need to store it like a list or some thing else to extract

    syntax:
        zip(iterable1,iterable2,.....)
'''

print(zip([1,2,3],[2,3,4]))#lazy so we get only location which nobody cares
'''<zip object at 0x0AF829A8>'''

print(list(zip([1,2,3],[2,3,4])))#list used to get the output

#look how it zips takes in elements together as per indexing

print(list(zip([1,2,3,4,5,6],[2,3,4])))#thats all doesnt take more elements
#only the common indexes are taken

print(list(zip([1,2,3,4,5,6],[2,3,4,5,6])))

################################################################################

#LIST COMPREHENSION
#first interpret the syntax and try to figure out what needs to be done
#Write in a simple effective manner in a single line for the list to be obtained
#write the whole code in square braces[] and use () for multiline code

l=[x*x for x in range(5)]
print(l)

l=[x*x*x for x in range(5)]
print(l)

l1=["Raja","Ram","Mohan","Roy"]

l2=[len(x) for x in l1]
print(l2)


l2=[(x,len(x)) for x in l1]
print(l2)
#notice the brackets being used here
#we do this to give multiple statements
