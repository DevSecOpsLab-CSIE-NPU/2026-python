"""R03. 繼承與 super()（8.7）

說明（繁體中文詳細註解）：
- 繼承（inheritance）可以重用父類別的屬性與方法，並在子類別中覆寫（override）行為。
- `super()` 用來呼叫父類別的方法，常用於建構子初始化與延伸父類別邏輯。
- `isinstance()` 與 `issubclass()` 可用來檢查物件/類別之間的繼承關係。
"""


# 基底類別：提供共同介面與預設行為
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # 預設行為：不知道怎麼叫時給一個通用描述
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # 使用 self.__class__.__name__ 可讓子類別自動顯示自己的類別名
        return f"{self.__class__.__name__}({self.name!r})"


# 子類別：覆寫父類別方法，提供更具體的行為
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# super()：在子類別中呼叫父類別的實作，再加上自己的內容
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)      # 呼叫上一層（Dog → Animal）的初始化
        self.owner = owner

    def speak(self):
        base = super().speak()      # 先取得 Dog.speak() 的結果
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())


# isinstance / issubclass：判斷物件是否屬於某類別、類別是否為子類別
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False


# 多型（Polymorphism）：同一個介面，不同物件有不同實作
def make_sounds(animals: list):
    for a in animals:
        # 呼叫同名方法，實際執行的是各自類別覆寫後的版本
        print(a.speak())


make_sounds([d, c, g])
