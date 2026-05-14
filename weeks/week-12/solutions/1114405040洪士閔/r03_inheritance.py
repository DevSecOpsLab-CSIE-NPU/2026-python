"""R03. 繼承與 super()。

這份版本示範基底類別、子類別、方法覆寫、super()、isinstance、issubclass，
並加上較完整的繁體中文註解方便理解物件導向繼承。
"""


# 基底類別：所有動物共同擁有的屬性與行為。
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # 用類別名稱動態表示，子類別也會顯示自己的名稱。
        return f"{self.__class__.__name__}({self.name!r})"


# 子類別：覆寫 speak()，讓不同動物有自己的說法。
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# 再往下延伸一層，示範 super() 可以先呼叫父類別的行為。
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)      # 先交給上一層完成 name 的初始化。
        self.owner = owner

    def speak(self):
        base = super().speak()      # 先取得 Dog.speak() 的內容。
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())


# isinstance：檢查物件是不是某個類別或其子類別的實例。
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 繼承 Animal）
print(isinstance(d, Cat))       # False


# issubclass：檢查類別之間的繼承關係。
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False


# 多型：同樣呼叫 speak()，不同物件會產生不同結果。
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())


make_sounds([d, c, g])
