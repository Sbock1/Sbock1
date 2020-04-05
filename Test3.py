class Dog:
    dogs = []                       #List

    def __init__(self, name):
        self.name = name            #Normal variable
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(m):
        """bark m times"""
        for _ in range(m):
            print("Bark!")

Tim = Dog("Tim")

print(Dog.num_dogs())