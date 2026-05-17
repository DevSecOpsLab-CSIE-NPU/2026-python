# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────
# 【詳解】
# 「繼承」讓子類別重用父類別的程式碼，建立「is-a」關係（Dog is-a Animal）。
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# 【詳解】
# 「覆寫」（override）：在子類別定義與父類別同名的方法。
# Dog 繼承 Animal，但覆寫 speak() 提供自己的實作。
# 不定義 __init__ 表示繼承使用父類別的版本。
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
# 【詳解】
# super().__init__(name) 呼叫父類別的建構子。
# super().speak() 呼叫父類別的方法，然後在子類別上擴充。
# 好處：不重複寫程式碼，父類別改變時子類別自動跟著更新。
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name) # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    def speak(self):
        base = super().speak() # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# 【詳解】
# isinstance(obj, Class) 檢查 obj 是否為 Class 或其子類別的實例。
# issubclass(SubClass, ParentClass) 檢查繼承關係。
print(isinstance(d, Dog)) # True
print(isinstance(d, Animal)) # True（Dog 繼承 Animal）
print(isinstance(d, Cat)) # False

print(issubclass(Dog, Animal)) # True
print(issubclass(Cat, Dog)) # False

# ── 多型（Polymorphism）──────────────────────────────────
# 【詳解】
# 「多型」：同一函式呼叫，根據實際型別有不同行為。
# make_sounds(animals) 接受任何 Animal 的 list，
# 呼叫 a.speak() 時 Python 自動選擇正確的版本（Dog 或 Cat）。
# 這樣無需寫 if isinstance(a, Dog) ... elif instanceof(a, Cat) ...
def make_sounds(animals: list):
    for a in animals:
        print(a.speak()) # 各自呼叫自己的 speak()

make_sounds([d, c, g])
