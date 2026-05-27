# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass / 多型

from __future__ import annotations
from typing import List

# ------------------------------------------------------------
# 基底類別（父類別）
# ------------------------------------------------------------
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        # 基底類別的預設行為
        return f"{self.name} 發出聲音"

    def __repr__(self) -> str:
        # repr 方便除錯或開發者檢視
        return f"{self.__class__.__name__}({self.name!r})"


# ------------------------------------------------------------
# 子類別：覆寫方法
# ------------------------------------------------------------
class Dog(Animal):
    def speak(self) -> str:
        # 覆寫 Animal.speak()，提供 Dog 專屬行為
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self) -> str:
        # 覆寫 Animal.speak()，提供 Cat 專屬行為
        return f"{self.name} 說：喵～"


# ------------------------------------------------------------
# 子類別：使用 super() 呼叫父類別方法
# ------------------------------------------------------------
class GuideDog(Dog):
    def __init__(self, name: str, owner: str) -> None:
        # super().__init__() 先呼叫 Dog 的 __init__，再由 Dog 呼叫 Animal.__init__
        super().__init__(name)
        self.owner = owner

    def speak(self) -> str:
        # super().speak() 直接呼叫父類別 Dog.speak()
        base = super().speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立實例並展示覆寫與 super()
d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())


# ------------------------------------------------------------
# isinstance / issubclass：類型判斷
# ------------------------------------------------------------
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False


# ------------------------------------------------------------
# 多型（Polymorphism）
# ------------------------------------------------------------
def make_sounds(animals: List[Animal]) -> None:
    # 透過同一個接口呼叫 speak()，依實例類別執行不同行為
    for a in animals:
        print(a.speak())


make_sounds([d, c, g])
