import random

# Making sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
setRandom = set(random.randint(1, 10) for _ in range(5))
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"SetRandom: {setRandom}")
print("\n")

# Combining Sets

unionSet = set1 | set2;
unionSetAlt = set1.union(set2)
intersectionSet = set1 & set2
intersectionSetAlt = set1.intersection(set2)

print(f"unionSet: {unionSet}")
print(f"unionSetAlt: {unionSetAlt}")
print(f"intersectionSet: {intersectionSet}")
print(f"intersectionSetAlt: {intersectionSetAlt}")
print("\n")

# Differencing sets

diffSet = set1 - set2
diffSetAlt = set1.difference(set2)
print(f"diffSet: {diffSet}")
print(f"diffSetAlt: {diffSetAlt}")
print("\n")

# Add elements

print(f"Set1 - Original: {set1}")
set1.add(12)
print(f"Set1 - With element 12 added: {set1}")

# Remove elements
print(f"Set1 - Original: {set1}")
set1.remove(12)
print(f"Set1 - With element 12 removed: {set1}")
print("\n")



