import time

# Creating the Decorator (function wrapper)
def simple_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper

def time_decorator(func):
        def wrapper():
            start_time = time.time()
            func()
            end_time = time.time()
            print(f"Time execution: {end_time-start_time}s")
        return wrapper

# Applying the decorator to an existing function
@simple_decorator
def greet():
    print("Hello!")

greet()

@time_decorator
def greetWithTime():
    time.sleep(2.5) # Sleep 2.5s
    print("Hello with Time!")

greetWithTime();

