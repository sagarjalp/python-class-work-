#  Convert a float 7.9 into an integer and print both the value and its type.
x = 7.9
print(type(x))
result = int(x)
print(result)
print(type(result))

# Write a program that takes a string "123" and converts it into an integer, then adds 10.
x = "123"
print(x)
result = int(x) + 10
print(type(result))
print(result)

# Print a string that contains both single and double quotes using escape characters.
# print("hello sir , 'i have done  my home work' ")
# print("hello sir , \"i have done  my home work\"")
# print('hello sir , "i have done  my home work"')
print('hello sir , \'i have done  my home \'')

# Concatenate two strings "Python" and "Rocks" with a space in between.
num1 = "python"
num2 = "rocks"
result = num1 + " " + num2
print(result)

# Repeat the string "Hi! " five times.
x = "hi"
result = "hi" * 5
print(result)

# Slice the string "Programming" to get "gram".
x = "programming"
result = x[3:7]
print(result)

# Use negative indexing to print the last 3 characters of "HelloWorld".
x = "HelloWord"
result = x[-3:]
print(result)

# Write a program that:

# a.Takes the string " I love Python programming! "
x = " I love python programing! "
print(x)

# b. Strips whitespace
x = " I love python programing! "
result = x.strip()
print(result)

# Converts it to uppercase
x = "I love python programing!"
result = x.upper()       
print(result)
# d. Replaces "Python" with "Java"
x = "I love python programing!"
result = x.replace("python", "java")
print(result)

# e. Splits it into words
x = "I love python programing!"
result = x.split()
print(result)

# 9. Write a program that converts "hello world from python" into title case.
x = "hello world from python"
result = x.title()
print(result)

# 10. Convert "python is amazing" so that only the first character is uppercase.
x = "python is amazing"
result = x.upper()
print(result)

# 11. Count how many times the letter "o" appears in "Hello, Python Programming!".
x = "Hello, Python Programming!"
result = x.count("o")
print(result)

# 12. Replace "training" with "learning" in "Python training is fun" and print the result.
x = "python training is fun"
result = x.replace("training" , "learning")
print(result)

# 13. Slice "Data Science" to get "Sci" using negative indexes.
x = "Data science"
result = x[-7:-4]
print(result)

# 14. Slice "Artificial Intelligence" to get "Intelligence".
x = "Artificial Intelligence"
result = x[-12:]
print(result)

# 15. Generate a random float between 0 and 1 and print it.
import random
x = random.random()
print(x)

# 16. Generate a random integer between 50 and 100.
import random
x = random.randint(50 , 100)
print(x)

# 17. Create a list of 6 colors and randomly select one.


# 18. Shuffle a list of numbers [1,2,3,4,5,6,7,8,9] and print the result.


# 19. Pick 3 random numbers from the range 1–30 using random.sample().


# class = 4th practice question 


# Take the string "Programming" and slice it to get "gram" using positive indexes.
x = "programing"
result = x[3:7]
print(result)

# Use an f-string to print: "My name is Sunil, I am 27 years old.“
name = "sunil"
age = 27
result = f"my name is {name}, I am {age} year old"
print(result)

# Convert "hello world" into "HELLO WORLD" using a string method.
x = "hello world"
result = x.upper()
print(result)

# Take the string "Programming" and slice it using negative indexes to get "ing"
x = "Programming"
result = x[-3:]
print(result)

# Take the string "Programming" and extract “ram” using negative indexes.
x = "programming"
result = x[-7:-1]

x = "programming"
result = x[4:7]
print(result)
print(x[-12])