import numpy as np


# Lesson 01 arrays

number= np.arange(0,10)
print(number)

#start,stop,step
#start where to begin, stop where to stop, step increment

summer= np.arange(0,56,4)
print(summer) 

#field with zeros
green= np.zeros(10)
print(green)

#zeros 2d array
red = np.zeros((6,8))
print(red)

#linspace
blue= np.linspace(0,10,3)
print(blue)

# eye identical matrices 
eyes= np.eye(4)
print(eyes) 

#ones create array file with ones
yellow= np.ones((3,5))
print(yellow) 

#random.rand generate random decimal number btw 0(inclusive) and 1(exclusive)
white= np.random.rand(3)
print(white)

#randn generate number from a standard normal distribution
black=np.random.randn(3)
print(black)

#randint generate random whole number
grey=np.random.randint(1,10,5)
print(grey) 

pink=np.arange(0,20,5)
print(pink) 

purple=np.linspace(0,20,5)
print(purple)

#attribution and arrays

print(np.random.randint(1,100,20))
#1,100,20 *1 smallest possible number *100 upper limit  *20 number to be generated


# Understanding data types
# How NumPy decides the type of data stored in an array
arr=np.arange(20)
print(arr.dtype)
# result was 64 means array store 64-bit integers.
#numpy can store different type of data 
a=np.array([1,2,3])
b=np.array([1.5,2.5,3.5])
c=np.array([True,False,True])
print(a.dtype)
print(b.dtype)
print(c.dtype)
#common Numpy datatype
#Datatype	Meaning	         Example
#int64	  Whole numbers	   1, 5, 100
#float64	Decimal numbers	 2.5, 3.14
#bool	    Boolean values	 True, False


# Lesson 02 array methods

# Finding maximum and minimum values and their indices
# max(), min(), argmax(), and argmin()
renarr=np.array([29,17,30,78,47,39,1,12])
print(renarr.max())
print(renarr.min())
# if you want to know where the highest value is located
print(renarr.argmax())
# if you want to know where the lowest value is located
print(renarr.argmin())


# Lesson 03 reshape

# Reshape changes the arrangement without changing the data
# Changing the arrangement of the array without changing its data 
arr=np.arange(30)
print(arr)
arr=arr.reshape(5,6)
print(arr)
#step one
number=np.arange(100)
print(number)
#step two
number=number.reshape(10,10)
print(number)


# Understanding shape
# Shape tells us the arrangement of an array
arr=np.arange(25)
print(arr.shape)
print(arr.reshape(1, 25).shape)
print(arr.reshape(25,1).shape)
#shape is an attribute why reshape is a method


# Lesson 04 indexing

# Indexing and slicing

arr=np.arange(0,11)
print(arr)
print(arr[8])
print(arr[10])

#understanding indexing
scores=np.array([50,60,70,80,90])
print(scores[2])
scores=np.arange(0,11)
print(scores[8])
# understanding slicing
scores=np.array([50,60,70,80,90])
print(scores[1:4])
arr=np.arange(0,11)
print(arr[1:4])

# NumPy broadcasting

number=np.array([10,20,30,40,50])
number[0:3]=50
print(number)

arr=np.arange(0,11)
arr[0:5]=100
print(arr)

arr=np.array([10,20,65,79])
print(arr +100)

arr=np.arange(0,12)
print(arr + 10)

#understanding views and copies
arr=np.arange(0,10)
slice_of_arr=arr[0:5]
print(arr)
print(slice_of_arr)

slice_of_arr[:]=99
print(slice_of_arr)
print(arr)

arr=np.arange(0,10)
new_arr=arr.copy()
new_arr[:]=50
print("original:", arr)
print("copy:", new_arr)
