import numpy as np

# Assignment 1
# Exercise 1: Creating an array
arr = np.arange(12)
print("Original Array:", arr)

# Exercise 2: Reshaping
new_arr = arr.reshape(3, 4)
print("Reshaped Array:")
print(new_arr)

# Exercise 3: Checking shape
print("Shape:", new_arr.shape)

# Exercise 4: Finding values
numbers = np.array([15, 45, 23, 89, 12, 67])

print("Maximum:", numbers.max())
print("Minimum:", numbers.min())
print("Index of Maximum:", numbers.argmax())
print("Index of Minimum:", numbers.argmin())

# Exercise 5: Checking data type
print("Data Type:", numbers.dtype)








# Exercise 1: Creating an array
arr = np.arange(12)
print(arr)

# Exercise 2: Reshaping
new_arr = arr.reshape(3, 4)
print(new_arr)

# Exercise 3: Checking shape
print(new_arr.reshape(1,12).shape)

# Exercise 4: Finding values
numbers = np.array([15, 45, 23, 89, 12, 67])

print(numbers.max())
print(numbers.min())
print(numbers.argmax())
print(numbers.argmin())

# Exercise 5: Checking data type
data_type=np.arange(20)
print(data_type.dtype)

# Assignment 2
#beginner




number=np.arange(0,20)
print(number)

print(number.max())
print(number.min())
number=np.arange(20)
print(number.size)

#exercise 1

number=np.arange(0,23)
print(number)

number=np.arange(24)
print(number)
number=number.reshape(4,6)
print(number)
print(number.shape)
print(number.size)

#exercise 2

scores=np.array([67,82,49,95,73,58,88])
print(scores)
print(scores.max())
print(scores.min())
print(scores.argmax())
print(scores.argmin())
print(scores.size)

#data analysis

scores=np.array([75, 82, 91, 68,
    88, 76, 95, 84,
    62, 79, 85, 90,
    93, 87, 74, 81,
    69, 96, 83, 77])
print(scores)
scores=scores.reshape(5,4)
print(scores)
print(scores.shape)
print(scores.size)

print(scores.max())
print(scores.min())
print(scores.argmax())
print(scores.argmin())
print(scores.shape)
print(scores.size)
print(scores.ndim)
print(scores.dtype)

scores=scores.reshape(4,5)
print(scores)

numbers = np.array([15, 25, 35, 45, 55, 65, 75, 85])
print(numbers)
print(numbers[0])
print(numbers[4])
print(numbers[1:5])
print(numbers[0:3])

#broadcasting assignment
numbers = np.array([5, 10, 15, 20, 25, 30, 35, 40])
new_numbers=numbers.copy()
new_numbers[:]=100
print("original:", numbers)
print("copy:", new_numbers)

scores = np.array([50, 60, 70, 80, 90, 100])
selected_scores=scores.copy()
selected_scores[0:3]=0
print("original:", scores)
print("selected:", selected_scores)


marks = np.array([20, 40, 60, 80, 100])
new_mark=marks.copy()
new_mark[0:2]=99
print("original:", marks)
print("copy:", new_mark)
