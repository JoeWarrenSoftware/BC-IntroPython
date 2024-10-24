import json

# Create a JSON string and load it into a dictionary
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_string)
print(f"JSON using datas: {data}")

# Modify some data
data["email"] = "example@example.com"

# Output the format back to a JSON string
json_string = json.dumps(data)
print(f"JSON using json.dumps: {json_string}")


# Write the JSON to a file

try:
    with open("testFile.json", "w") as file: # Similar to .NET using, the "with" keyword deconstructs the file after it's used in this indented block
        json.dump(data, file, indent=4) # Writes the dictionary object "data" into the file stream setup, where indentation uses 4 spaces
except Exception as e:
    print(e)

# Read JSON from an existing file

try:
    with open("testFile.json", "r") as file:
        readData = json.load(file)
except FileNotFoundError as e:
    print("File Not Found!")
except Exception as e:
    print(e)

print(f"JSON from read file: {readData}")