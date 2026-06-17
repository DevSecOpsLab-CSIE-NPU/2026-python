"""R03: inheritance, override, super, isinstance, issubclass."""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says: woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: meow~"


class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def speak(self):
        base = super().speak()
        return f"{base} (guide dog for {self.owner})"



def make_sounds(animals):
    for animal in animals:
        print(animal.speak())


if __name__ == "__main__":
    d = Dog("Blacky")
    c = Cat("Mimi")
    g = GuideDog("Goldie", "Wang")

    for animal in [d, c, g]:
        print(animal.speak())

    print(isinstance(d, Dog))
    print(isinstance(d, Animal))
    print(isinstance(d, Cat))

    print(issubclass(Dog, Animal))
    print(issubclass(Cat, Dog))

    make_sounds([d, c, g])
