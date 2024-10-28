#Example of Try-Catch

try:
    print("Do some stuff")
    print("Do some more stuff")
    raise Exception("I crashed!")
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Code completed!")


# Example of a base class

class Animal:
    def __init__(self, name):
        self.name = name

    def presentName():
        print(f"My name is {self.name}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def Meow(self):
        print("Meow!")