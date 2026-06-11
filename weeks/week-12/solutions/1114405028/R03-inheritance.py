# R03-inheritance.py
# 完整繁體中文註釋版：示範繼承、方法覆寫、super()、isinstance 與 issubclass

# 基底類別
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# 子類別覆寫 speak 方法
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# 使用 super() 呼叫父類別的建構式與方法
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)      # 呼叫 Dog.__init__，進而設定 name
        self.owner = owner

    def speak(self):
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

# isinstance / issubclass
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# 多型（Polymorphism）：不同類別實例各自執行自己的方法
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())

make_sounds([d, c, g])
