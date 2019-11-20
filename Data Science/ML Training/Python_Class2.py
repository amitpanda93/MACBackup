# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 07:30:03 2019

@author: Adminstrator
"""
25/03
#Literals 
#numbers, strings 
23, -78, 176.765
'Hello'
'Python'
'M'
'7667'
"Hello"
"Python Session"
7, 9, 465, -875
89.76,54.323,-875.65 #10-308 to 10308 with 16 digits of precision
a+bi, -3+7i
float(8)
int(6.7)
10+7
12*10
96/12
(-30 * 4) + 500
#quotient and remainder
78 % 5
#15*5 + 3 
78 // 5

152.78 // 3.0
5**3
8**2
#strings 
#'' or ""
print('Hello world')
'''Good morning everyone.
"welcome to world of 'Python'."
Happy learning.'''

#Gives error
'Good morning
We are learning Python'

print('Good morning' '......' 'Happy learning')
print('Good morning' + '......' + 'Happy learning')

print("Hello" + 2)
print("Hello " * 4)
print("Hello\n" * 4)


print(4 + 20)

print('What's your name?')
print('What\'s your name?')
print("The boy replies, \"My name is Aditya\"")

print('''Today is 15th Aug. \n India became
independent on \n this day''')

print('''Today is 15th Aug. \t India became
independent on \n this day''')

print('''Today is 15th Aug. \
 India became independent on this day''')

#Escape sequences
print("\\")    #\\ - Prints \
print("\'")    #prints ' 
print("\"")    #prints " 
#\a
print("\a")
#\n
#\t
#\f
print("Hello\fworld")     

#27/03     
#variable assignment
#multiple assignment
#operators in Python
#Decision control statements
var = 'Hello'
print("the value is", var)
print("the value is " + var)     

var = 'Good morning'     

sums = flag = a = b = 0     
sums, flag, a, b, c = 0,1,2,3,4

#Boolean
bool_var = True
print(bool_var)

20 == 30
20 >= 30
30 == 30.5
20 != 20
87 >= 87.0

#input func
strs = input('Pl enter your name')
num = int(input('Pl enter your age'))
age = input('Pl enter your age')
num - 10
print("your name is "+strs+" and your age is "+age)
print("your name is "+strs+" and your age is ",num)

#Operators
#Arithmetic Operators
+, -, *, /, %, //, ** 
#Comparison Operators
==, !=, >, <, >=, <= 
#Assignment Operators
=, +=, -=, *=, /=, %=, //=, **= 
i = 0
i += 1 #Incrementing the i by 1 each time

i = 40
i %= 7  
#same as
i = i % 7
i = 40
i //= 6
#Logical Operators
Logical AND - &&
Logical OR - ||
Logical NOT - ! 
a = 10,b
b != a
!a = 0  #Cannot apply this on vars
#Membership operators 
in
not in
lst = [1,2,3,4,5]
6 in lst
1 not in lst
4 in lst
strs
'z' in strs
'v' in strs
'V' in strs

#Identity operators
is 
is not 

#operator precedence 
** - Exponentiation
*,/,%,// - Multiply, Divide, Modulo, Floor division
+, - - Addition, Substraction
<=,<,>,>= - Comparison operators
<>,==,!= Equality operators
=,%=,/=,//=,-=,+=,*=,**=  Assignment operators
is, is not identity operators
in, not in membership operators
not, or, and Logical operators

10 + 30 * 5
40 + 20 * 30 / 10
(40 + 20)/ 30 * 10
40 + (20 + 30) // 10 / 4

#Decision Control statements
#if
#if-else
#if-elif-else (elif can be repeated multiple times)
#while
#for
#break
#continue

#program to tell whether a person is eligible to vote 
age = int(input("Enter your age: "))
if(age > 18):
    print("You are eligible!")

#Program to increment a number by 10 if it is postive
num = int(input("Enter a num: "))
if(num > 0):
    num += 10
    print("After increment: ",num)

#program to tell whether a person is eligible to vote if not display the diff
age = int(input("Enter your age: "))
if(age > 18):
    print("You are eligible!")
else:
    print("You have ", 18 - age, " years to be eligible")

#if-elif-else
#program to check whether a num is zero, neg, or pos
num = int(input("enter a num: "))
if(num > 0):
    print(num,"is pos")
elif(num < 0):
    print(num,"is neg")
else:
    print("you entered zero")

#program to tell whether entered char is vowel or not
ch = input("enter a character: ")
if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(ch,"is a vowel")
elif(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(ch,"is a vowel")
else:
    print(ch,"is not a vowel")

#program to find out greater among 3 numbers
a = int(input("enter num1: "))
b = int(input("enter num2: "))
c = int(input("enter num3: "))
if(a > b and a > c):
    print(a," is greater")
elif(b > a and b > c):
    print(b,"is greater")
elif(c > a and c > b):
    print(c,"is greater")
elif(a == b and a > c):
    print(a," is greater")
elif(a == b and c > a):
    print(c,"is greater")
elif(b == c and b > a):
    print(b," is greater")
elif(b == c and a > b):
    print(a,"is greater")
elif(a == c and a > b):
    print(a," is greater")
elif(a == c and b > a):
    print(b,"is greater")
else:
    print("All are equal")


#while
i = 0
while(i <=10):
    print(i, end = " ")
    i += 1

#program to calculate sum and avg of first 10 numbers
i = 1
sums = 0
while(i <= 10):
    sums = sums + i
    i += 1
print("sum is: ", sums, "and avg is", sums/(i-1))


#program to calculate sum and avg of first n numbers
num = int(input("enter n: "))
i = 1
sums = 0
while(i <= num):
    sums = sums + i
    i += 1
print("sum is: ", sums, "and avg is", sums/(i-1))


#program to print factorial
#program to print sum and avg from m to n

#program to tell whether a given year is a leap year or not
#leap year - 

#program to reverse a number
num = int(input("enter a num: "))
print("The reversed number is: ",)
while(num!=0):
    temp = num % 10
    print(temp, end = "")
    num = num // 10

#for
#we will use range() function
for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)

#program to display multiplication table of any num
num = int(input("enter a num: "))
for i in range(1,11):
    print(num,"*",i," = ",num*i)

#classify  a num as prime or not
num = int(input("enter a num: "))
flag = 0
for i in range(2,num):
    if(num % i == 0):
        flag = 1
        break
        #rint("not a prime")
if(flag == 1):
    print(num, "is not prime")
else:
    print(num, "is a prime")

#break
i = 1
while(i <= 10):
    print(i, end =  " ")
    if(i == 5):
        break
    i = i + 1
print("\nencountered break!")


#continue
for i in range(1,11):
    if(i == 5):
        continue
    print(i, end = " ")
    print("\nthis statement is seen only 9 times")
print("\nCompleted!")


#Data Strcutures
#Data type - problem 
i = 20
f = 34.23
ch = "Hello"
#Name, ID, Sal, Exp
#1.string
#2.list
#3.tuple
#4.Dictionary 
ch = "Hello"
#in Python, Index pos starts from 0
ch[0]
#ch[0,length-1]
ch[3]
ch[3] = 't'  #strings are not mutable, nonmutable,immutable

ch[0:3]
ch[2:4]
ch[:]
ch[2:]
ch[:2]

#list 
#[]
lst1 = [34,25.24,'Hello']
lst1[2]
lst1[2] = 'Hello World' #lists are mutable 
lst1

#tuple
#()
tup1 = (23,34.56,12,45.78,'Hellow World')
type(tup1)

tup1[3]
tup1[3] = 23.47  #tuple is not mutable


#Dict
#{}
Dict = {"Item" : "Chocolate", "Price" : 100}
print(Dict["Item"])
print(Dict["Price"])

#Functions and Modules
def func():
    print("First Function!")

func()

def add(x,y):
    print("Addition is: ",x+y)

add(4,5)
add(29,49)

def largest(x,y):
    if(x > y):
        print(x, " is greater")
    else:
        print(y, " is greater")

largest(9,10)
largest(286,273)

def prime(x):
    flag = 0
    for i in range(2,x):
        if(x % i == 0):
            flag = 1
            break
    if(flag == 1):
        print(x, " is not prime")
    else:
        print(x, " is prime")

prime(13333)

#Scope
def outer_func():
    outer_var = 10
    def inner_func():
        global inner_var
        inner_var = 20
        print("1st print","Outer var = ", outer_var)
        print("2nd print","Inner var = ", inner_var)
    inner_func()
    print("3rd print","Outer var = ", outer_var)
    print("4th print","Inner var = ", inner_var)

outer_func()

#funcs in lists, strings 
#REMEMBER    

#Reverse a string
str = input("Enter a string: ")
r_str = ""
for i in str:
    #print(i)
    r_str = i + r_str
    #print(r_str)
print(r_str)

#Length of a string

st = 'Hello'
cnt = 0
for i in st:
    cnt += 1
print(cnt)

def display(name, age, salary):
    print("Name: ", name)
    print("Age: ", age)
    print("Salary: ", salary)

n = "Aadi"
a = 35
s = 100000
display(salary = s,name = n, age = a)    

def grad(name,course = "BTech"):
    print("Name: ",name)
    print("Course: ",course)

grad(course = "MBA",name = "Aadi")
grad(name = "Aadi")


#Variable length arguments
def func(name, *fav_sub):
    print("\n",name,"likes subjects ")
    for subject in fav_sub:
        print(subject)

func("Aadi","Mathematics","Science")
func("Krish","C","C++","Java","Python")
func("Ram")

#Lambda Functions or Anonymous functions
#lambda 
#need not use def keyword
#syntax for lambda func
#lambda arguments:expression
sums = lambda x,y:x+y
#this is same as
def sums(x,y):
    return x+y

print("Sum = ",sums(3,5))
#Lambda functions have no name
#can take any number of arguments
#returns only one value as an expression
#do not have explicit return statement
#they cannot access any variables global or local 
#program to find out samller of 2 numbers using lambda funcs
def small(a,b):
    if(a < b):
        return a
    else:
        return b

sums = lambda x,y : x+y   #Lambda func to add 2 numbers
diff = lambda x,y : x-y   #Lambda func to subtract 2 numbers
#pass lambda as an argument
print("smaller of 2 numbers = ", small(sums(-3,-2),diff(-1,2)))

#how to use lambda func with an ordinary func
def inc(y):
    return (lambda x:x+1)(y)

a = 100
print("a = ",a)
print("a after increment = ")
b = inc(a)
print(b)

#construct1
print((lambda x:x*2)(9))

#construct2
var = (lambda x:x*2)
print(var(9))

#Construct1 and Construct2 are same

#program to calculate sum of first 10 numbers using lambda func
#print(sum(range(1,11)))
x = lambda:sum(range(1,11))
print(x())

#program to add and multiply 2 numbers using lambda func recursively
add = lambda x,y : x+y
multiply_and_add = lambda x,y,z:x*add(y,z)
print(multiply_and_add(3,4,5))

#strings and lists in-depth 
#in-built funcs
#String 

#modules - Python 
#pandas, numpy, visualization


import os

os.chdir("C:\Modules")  #Setting the current working directory

os.getcwd()    #getting the current working directory
#Creating custom modules
import MyModule
prime(23)
display("Sid",25,250000)

from MyModule import outer_func
outer_func()


#strings revisited  
print("THis is Python Class" , "And its a sunday" + "mornig")

#format sequences
name = "Arun"
age = 18
print("name: ",name + "age: ",age)

print("Name = %s and Age = %d" %(name,age))
print("Name = %s and Age = %d" %("Ankita",20))

#FORMAT sequences
#character - %c
#string - %s
#integer - %d
#float - %f

#in-built functions in string
strs = "helloworld"
print(strs.capitalize())

str = "hello"
print(str.center(10,'*'))

str = "he"
message = "helloworldhellohellohe"
print(message.count(str,0,len(message)))

str = "The world is beautiful"
print(str.startswith("Th",0,len(str)))

str = "The world is beautiful"
print(str.endswith("ful",0,len(str)))

message = "he is my best friend"
print(message.find("my",0,len(message)))

#rfind
#rindex

#isalnum()
#isalpa()
#isdigit()
#islower()
#isspace()
#isupper()
#len(string)

#ljust and rjust
str = "hello"
print(str.ljust(10,"*"))
print(str.rjust(10,"*"))
print(str.center(10,"*"))

#zfill
#automatically left padding of zeros to the  string
str = "1234"
print(str.zfill(10))

#lower()
#upper()

#lstrip()
#rstrip(
#strip()

str = "   Hello"
print(str.lstrip())

str = "Hello       "
print(str.rstrip())

str = "    Hello     "
print(str.strip())

#max(string)
#min(string)

#replace()
str = "hello hello hello"
print(str.replace("he","fo"))

#title()
str = "The world is beautiful"
print(str.title())

#swapcase()
print(str.swapcase())

#most imp
#split() and join()
str = "abc,def, ghi,jkl"
print(str.split(','))

print('-'.join(['abc', 'def', ' ghi', 'jkl']))
str = ','.join(['abc', 'def', ' ghi', 'jkl'])
print(str)


'.'.join(['Vijayraj','Tumma'])

#enumerate()
str = "Hello World"
print(list(enumerate(str)))

#format()
str1 = "{},{},and {}".format('Sun','Moon','Stars')
print("\n default order of arguments is:" + str1)

str2 = "{1},{0},and {2}".format('Sun','Moon','Stars')
print("\n positional order of arguments is:" + str2)

str3 = "{c},{b} and {a}".format(a='Sun',b='Moon',c='Stars')
print("\n keyword sequence of arguments is:" + str3)


#slice operations
str = "Welcome to the world of Python"
str[::3]

#lists
#methods
#append()
num_list = [6,3,7,8,9,4,1]
num_list.append(4)
print(num_list)

#count()
num_list.count(4)
#index() - returns the lowest index of the obj we give as parameter
#insert() pop() remove() reverse() sort()
#inserts the obj at specified index in the list
num_list.insert(3,100)
print(num_list)

num_list.pop()
print(num_list)

num_list.pop(0)
num_list.remove(0)

#remove()
#reverse()
#sort()

#extend()
num_list1 = [1,2,3,4]
num_list2 = [5,6,7,8]
num_list1.extend(num_list2)
print(num_list1)

#num_list1 = num_list1 + num_list2

list1 = ['1','a',"abc",'2','B',"Def",'%','$','#']
list1.sort()
print(list1)
#program to demonstrate queue using list datastructure
queue = [1,2,3,4,5,6]
print("Original queue: ",queue)
queue.append(7)
print("Queue after insertion: ", queue)
queue.pop(0)
print("Queue after deletion: ", queue)


#list comprehension
#imp topic
cubes = []
for i in range(11):
    cubes.append(i**3)
print("cubes of numbers from 1-10: ",cubes)

#using list comprehension
cubes = [i**3 for i in range(11)]
print(cubes)

#program to combine and print elements of two lists using lc

print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!= y])










