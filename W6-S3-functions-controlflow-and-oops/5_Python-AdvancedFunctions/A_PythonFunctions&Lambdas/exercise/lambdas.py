# One argument lambda
addOne = lambda x: x+1
# Multi argument lambda
multiply = lambda x,y: x*y

print(addOne(9))
print(multiply(2,3))

# Map provides a series of inputs for your function, and provides a list/array output

addOneOutputs = list(map(addOne, [2,4,10,10,2,10,6,100]))
outputs = list(map(multiply, [2,3,4,5], [10,100,1000,10000]))

print(outputs)

# Filter will return only true results for the lambda function
inputNumbers = [20, 300, 4000, 50000]
numbersOver100  = list(filter(lambda x: x > 100, inputNumbers))
print(numbersOver100)

# Sorting can be customised by key or by value
sorted_by_key = sorted([(1, 'banana'), (2, 'apple'), (3, 'cherry')], key=lambda x: x[0])
sorted_by_value = sorted([(1, 'banana'), (2, 'apple'), (3, 'cherry')], key=lambda x: x[1])
print(sorted_by_key)
print(sorted_by_value)