# Create dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(f"my_dict: {my_dict}")

# Query value for a key
print(f"Value for key 'city': {my_dict["city"]}")

# Add a new key and value to the dictionary
my_dict["email"] = "example@example.com"
print(f"Adding new key-value for 'email': {my_dict}")

# Remove a key-value pair
my_dict.pop("city")
print(f"Key-Value pair for 'city' removed: {my_dict}")
my_dict["city"] = "New York"

del my_dict["age"]
print(f"Key-Value pair for 'age' removed: {my_dict}")
my_dict["age"] = 25

#  Query if an existing key is found:
print(f"Contains Key 'name': {my_dict.__contains__("name")}")
print(f"Contains Key 'ZZZZ': {my_dict.__contains__("ZZZZ")}")