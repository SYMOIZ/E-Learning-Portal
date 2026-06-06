class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof"

dog = Dog("Rex")
print(dog.name, dog.speak())
