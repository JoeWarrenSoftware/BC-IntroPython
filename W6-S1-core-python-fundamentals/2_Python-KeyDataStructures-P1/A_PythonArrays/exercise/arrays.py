# Make an array
fruits = ["apple", "banana", "cherry", "lemon"]

# Show an element of the array
print(f"First fruit of the array is: {fruits[0]}\n")

# Show a range of elements of the array by slicing
print(f"2nd and 3rd fruits of the array are: {fruits[1:3]}\n")

# Modify the array
fruits[1] = "lime"
print(f"Change value of 2nd element of fruits is: {fruits[1]}\n")

# Add an element to the end of the array
fruits.append("strawberry")
print(f"Last element of the array is: {fruits[4]}\n")

# Remove all occurences of a certain value
fruits.remove("cherry")

# Show all values of the array
y = ""
for x in fruits:
    y += x + " "

print(f"Fruits found: {y}\n")

# Get the number of "apple" found in the array
print(fruits.count("apple"))

# Get the number of elements in the array
print(len(fruits))

# Print the whole array
print(fruits)
