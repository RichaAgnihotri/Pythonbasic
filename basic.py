#single line comment
"""
multi
line
comments
"""
"""
variables:-- storage memory space which keeps on changing
rules:
1. variables cannot be digit or special character
2. variables can be alpha-numeric
3. variables cannot be the keywords
4. variables should be related to the program
5. variables in python are case sensitive

data type defines the values being stored in variables
"""
"""
value = 10
print(value)
print(type(value))

value = 10.34
print(value)
print(type(value))

value = "apple"
print(value)
print(type(value))

value = 'a'
print(value)
print(type(value))

value = True
print(value)
print(type(value))

value = 7+8j
print(value)
print(type(value))
"""
# input function-- makes the user to insert value at at run time of the program
"""
input function by default takes string input hence we do typecasting
typecasting--- changing of the values datatype from one to another

"""
"""
value = int(input("Enter values\n"))
print(value)
print(type(value))

"""
"""
operators are the one which helps to perform operation over values

types:
Arithmetic operator: +,-,*,/,%(remainder),//(floor or quiotent),**(expotential)

conditional operators: >, <,>=,<=,==,!=

relational operators: and, or , not

assignment operators: =, +=,-=,*=,/=
"""
"""
a = 10
print(a)

num= int(input("Enter num:\n"))
print(num)

num= float(input("Enter num:\n"))
print(num)
"""
"""
num1=int(input("Enter num:\n"))
print(num)

#Arithmetic operators
print(num+num1)
print(num-num1)
print(num*num1)
print(num/num1)
print(num//num1)
print(num**num1)

if(num>num1):
    print(num,"is greater")
else:
    print(num1,"is greater")

for i in range(1,11,1):
    print(i)

#strings-- collection of characters
name="Udita"
print(name)
print(type(name))

name=input("Enter name:")
print(name)
print(type(name))


#traversing

for i in name:
    print(i)

#concatenation:

print("Hello"+name+str(32))

#repeation

print(3*name)

#membership (in/not in)
ch=input("Enter letter:\n")
print(ch in name)


print(ch not in name)


print(name[2])

print(name[:])
print(name[:3])
print(name[1:])
print(name[1:4])

for i in range(4,0,-1):
    name=input("Enter name")
    print(name)

for i in range(1,4,1):
    name=input("Enter name")
    print(name)


# WAP to calulate no of vowels and consonants in given string
name=input("Enter string:\n")
vc=0
cc=0
space=0
for x in name:
    if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
        vc+=1
    elif(x==" "):
        space+=1
    else:
        cc+=1
print("Total vowels:",vc)
print("Total consonants",cc)


#Wap to calculate no of spaces given in string


name=input("Enter string:\n")
cs=0
for i in name:
    if(i==" "):
        cs+=1
print("Total Spaces:",cs)


#functions of string
#captialize(): to converts the first letter of string to capital case

name=input("Enter string:\n")
print(name.capitalize())

#len(string): to return length of the string

name=input("Enter string:\n")
print(len(name))



#split(): to divide string into parts based on split condition
name=input("Enter string:\n")
words=name.split(" ")
for i in words:
    print(i)
    print(len(i))
 

#strip(): to remove spaces from the beginning and end of the string
name="*****Udita*****"
print(name.strip("*"))
print(name.lstrip("*"))
print(name.rstrip("*"))


#replace(current string,replaces string)
name=input("Enter string:\n")
for i in name:
    if(i=="a"):
        name=name.replace(i,"*")
print(name)

#upper(): uppercase
name=input("Enter string:\n")
print(name.upper())

#lower():lowercase
name=input("Enter string:\n")
print(name.lower())

#swapcase(): swapping of cases
name=input("Enter string:\n")
print(name.swapcase())

#list: collection similar to array=[]
#list creation:
#by literal:

list_1=[1,2,3,4,5,6,7,1,2,3,4,5]
print(list_1)
print(type(list_1))


# indexing:
"""
"""
(0)1,(1)2,(2)3,4,5,6

Slicing--- :
[start(included): stop(excluded)]
[2:6]
"""
"""
print("the value at position [6]=",list_1[6])

print(list_1[:])
print(list_1[3:])
print(list_1[:9])
print(list_1[3:11])

for i in list_1:
    print(i)
    
# to add to new element in list
#append--- adds values in end of the list


a=int(input("Enter a:\n"))92
list_1.append(a)
print(list_1)

#insert--- adds values to specific position

a=int(input("Enter a:\n"))56
list_1.insert(1,a)
print(list_1)

# to delete value from list

# by index
del list_1[2]
print(list_1)


# from end of list
list_1.pop()
print(list_1)

#by value
a=int(input("Enter element to delete:\n"))
list_1.remove(a)
print(list_1)
"""
"""

list_1=[]

n=int(input("Enter n:\n"))5

for i in range(0,n,1):
    data=int(input("Enter value:\n"))1,2,3,4,5
    list_1.append(data)
print(list_1)

sum=0;
for i in list_1:
    sum=sum+i
print("sum of list:",sum)

"""

# functions
"""
a=int(input("Enter a:\n"))
print(a)

#user defined functions

#function definition
def addition(a,b):
    sum=a+b
    print(sum)

#function call
a=int(input("Enter a:\n"))
print(a)
b=int(input("Enter b:\n"))
print(b)
addition(a,b)
"""    
"""
File: Collection of recorded data and information
File Handling: operation performed over file in order to create, update, 
read and modify

operations:
create
read
write
update
delete

open and close are mandatory operations
Syntax:
open(location of the file with name,mode of operation) 
close()


mode of operation:
x ---> create
w --->write
r ---> read
a ---> append
r+ ---> read first then write
w+ ---> write first and then read

"""
"""
fp = open("D:/dump1.txt","w")
if fp:
    print("File open successfully")
    data=input("Enter data:\n")
    fp.write(data)
else:
    print("File not found")
fp.close()
"""
"""
fp = open("D:/dump1.txt","r")
if fp:
    
# reading till specific position
    #data= fp.read(13)
    #print(data)
    
# reading one line of file
    #data= fp.readline()
   # print(data)
    
# reading entire file
    data= fp.read()
    print(data)
      
else:
    print("File not found")
fp.close()
"""

"""
fp=open("D:/dump1.txt","r")
vc=0
cc=0
sc=0
data=fp.read()
for i in data:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vc+=1
    elif(i==" "):
        sc+=1
    else:
        cc+=1
print("Vowel count",vc)
print("Consonant count",cc)
print("Space count",sc)
fp.close()
"""
"""
fp=open("D:/one.txt","w")
if fp:
    data=input("Enter:\n")
    fp.write(data)
fp.close()

fp=open("D:/two.txt","w")
if fp:
    data=input("Enter:\n")
    fp.write(data)
fp.close()

fp=open("D:/third.txt","w")
if fp:
    f1=open("D:/one.txt","r")
    data=f1.read()
    
    f2=open("D:/two.txt","r")
    data1=f2.read()
    
    fp.write(data+data1)
fp.close()

fp=open("D:/third.txt","r")
if fp:
    data=fp.read()
    print(data)
fp.close()
"""


fp= open("D:/dump1.txt","r")
if fp:
    data=fp.read()
    print(data)
    
fp.close()

fp= open("D:/dump1.txt","a")
if fp:
    fp.write(" "+"how are u???")
    
fp.close()


fp= open("D:/dump1.txt","r")
if fp:
    data=fp.read()
    print(data)
    
fp.close()



    
