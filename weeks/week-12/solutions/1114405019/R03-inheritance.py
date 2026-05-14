# R03-inheritance.py
# 示範繼承、super()、方法覆寫及多型（isinstance）

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        # 使用 super() 呼叫父類別建構子
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # 方法覆寫 (Override)
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    # 多型示範: 不同物件對同一方法的不同反應
    if isinstance(animal, Animal):
        print(f"{animal.name} says: {animal.speak()}")
    else:
        print("這不是一個 Animal 實例")

if __name__ == "__main__":
    print("=== 繼承與多型示範 ===")
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Kitty")
    
    make_animal_speak(dog)
    make_animal_speak(cat)
    
    print(f"dog 是否為 Dog? {isinstance(dog, Dog)}")
    print(f"dog 是否為 Animal? {isinstance(dog, Animal)}")
