numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)

def ShowNumbers(count):
    try:
        for i in count:
            print(f"Next Number: {next(iterator)}")
    except Exception:
        print(f"Exceeded iteration")

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Error: Gone too far")

# List Comprehensions:
squareNums = [x**2 for x in range(1,5)]
print(squareNums)

# Creates a dictionary mapping numbers to their squares
squareDict = [(x,x**2) for x in range(1,5)]
print(squareDict)

#uniqueChars = [x for y in "ThisIsAStringwithsometext" if x[y] == True]