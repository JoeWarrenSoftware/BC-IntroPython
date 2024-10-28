def greet():
    return "Hello, World!"

print(greet())

def add(a, b):
    return a + b

print(add(4,2))

def greetName(name="Guest"):
    return f"Hello, {name}!"

print(greetName())
print(greetName("Max"))

def print_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_info(1,2,3, name="Sarah", Age=27)
