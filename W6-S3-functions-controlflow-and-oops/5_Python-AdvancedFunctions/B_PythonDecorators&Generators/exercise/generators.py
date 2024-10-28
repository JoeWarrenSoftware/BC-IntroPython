def count_up_to(max):
    count = 1
    while count <= max:
        yield count # Provides a partial output of the function to the caller before the entire function has completed
        count += 1

#Sycn Call
print("Loop the yield funciton:")
for number in count_up_to(5):
    print(number)

# Async Call
print("Use the Next to iterate through the generator")
generator = count_up_to(3000000000000000000000000000000000000)
print(next(generator))
print(next(generator))
print(next(generator))