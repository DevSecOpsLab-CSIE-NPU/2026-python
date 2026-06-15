# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass
#
# 繼承（Inheritance）讓子類別自動擁有父類別的屬性與方法，
# 同時可以「覆寫（override）」部分行為，達到程式碼複用。
# super() 讓子類別能主動呼叫父類別的方法，避免重複撰寫相同邏輯。

# ── 基底類別 ─────────────────────────────────────────────
# Animal 是所有動物的共同基礎，定義共用屬性（name）與預設行為（speak）
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # 預設的「發聲」行為，子類別通常會覆寫這個方法
        return f"{self.name} 發出聲音"

    def __repr__(self):
        # self.__class__.__name__ 動態取得「實際類別名稱」，
        # 所以即使子類別繼承此方法，印出的也是子類別名稱（如 Dog、Cat）
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# class Dog(Animal) 表示 Dog 繼承 Animal，
# 自動擁有 __init__ 和 __repr__，只覆寫 speak。
class Dog(Animal):
    def speak(self):   # 覆寫（override）父類別的 speak
        return f"{self.name} 說：汪汪！"


class Cat(Animal):
    def speak(self):   # 各自覆寫，行為不同
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────
# GuideDog 繼承 Dog，新增 owner 屬性，並在 speak 上擴充輸出。
class GuideDog(Dog):
    def __init__(self, name, owner):
        # super().__init__(name) 沿繼承鏈向上呼叫：
        # GuideDog → Dog → Animal，確保 self.name 被正確初始化
        super().__init__(name)
        self.owner = owner   # GuideDog 特有的屬性

    def speak(self):
        base = super().speak()   # 先取得 Dog.speak() 的結果
        # 在 Dog 的輸出基礎上附加導盲犬資訊，不重複撰寫相同邏輯
        return f"{base}（導盲犬，主人：{self.owner}）"


d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────
# isinstance 檢查「物件是否屬於某個類別（含子類別）」
print(isinstance(d, Dog))       # True  — d 是 Dog
print(isinstance(d, Animal))    # True  — Dog 是 Animal 的子類別，所以也算是 Animal
print(isinstance(d, Cat))       # False — Dog 與 Cat 是平行關係

# issubclass 檢查「類別之間的繼承關係」
print(issubclass(Dog, Animal))  # True  — Dog 繼承 Animal
print(issubclass(Cat, Dog))     # False — 兩者無繼承關係

# ── 多型（Polymorphism）──────────────────────────────────
# 多型的精髓：同一個函式介面，針對不同子類別物件，自動執行對應版本的方法。
# make_sounds 不需要知道 a 是 Dog 還是 Cat，只要它有 speak() 方法即可。
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())   # Python 動態分派：根據實際型別呼叫對應的 speak()

make_sounds([d, c, g])
