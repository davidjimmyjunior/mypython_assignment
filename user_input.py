"""
Task: Write a program that asks the user for their name, age, and location and then prints out a personalized message.

Instructions:

Create a new Python file and name it "user_input.py"
Use the input() function to ask the user for their name and store it in a variable called "name".
Use the input() function to ask the user for their age and store it in a variable called "age".
Use the input() function to ask the user for their location and store it in a variable called "location".
Print out a personalized message 
using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
Save and run the program to see the output.


name = input("What is your name:")
age = input("How old are you:")
location = input("What is your location:")
print("Hello", (name), "I am" ,(age),"years old and live in" ,(location))

# 1. Program to accept user input to create a list of integers and compute the sum:
Accept user input to create a list of integers
# user_input = input("Enter a list of integers separated by space: ")
int_list = [int(x) for x in user_input.split()]

# Compute the sum of all integers in the list
sum_integers = sum(int_list)

print("Sum of integers in the list:", sum_integers)


# Program to create a tuple of favorite books and print each book name on a separate line:
# 2. Create a tuple of favorite books
favorite_books = ("Book1", "Book2", "Book3", "Book4", "Book5")

# Print each book name on a separate line using a for loop
for book in favorite_books:
    print(book)

# Program to store information about a person in a dictionary and print the dictionary:
# Create an empty dictionary to store person's information
person_info = {}

# Ask user for input to populate the dictionary
person_info['name'] = input("Enter the person's name: ")
person_info['age'] = input("Enter the person's age: ")
person_info['favorite_color'] = input("Enter the person's favorite color: ")

# Print the dictionary containing person's information
print(person_info)

#4. Program to create a new set containing common elements from two sets of integers:
# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter integers for set 2 separated by space: ").split()))

# Create a new set containing common elements from both sets
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)



# 5. Program to filter words with odd number of characters using list comprehension:
# Store a list of words
words = ["apple", "banana", "orange", "pear", "grape"]

# Use list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)

# my_list = []
my_list = (10,20,30,40)
my_list.append(1, 15)
print(my_list)
"""

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60, 70])
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
index_30 = my_list.index(30)
print(index_30)
