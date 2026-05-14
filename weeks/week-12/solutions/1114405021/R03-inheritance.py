# R03. 繼承與 super()（8.7）
# 本範例示範物件導向中很重要的幾個概念：
# 1. 繼承：子類別可以直接使用父類別的功能
# 2. 方法覆寫：子類別可以改寫父類別的方法
# 3. super()：用來呼叫父類別的方法
# 4. isinstance / issubclass：檢查物件與類別的關係
# 5. 多型：同一個介面，因物件不同而表現不同

# -----------------------------------------------------------------------------
# 一、基底類別：Animal
# -----------------------------------------------------------------------------
# Animal 是父類別（基底類別）。
# 下面的 Dog、Cat、GuideDog 都會繼承它。
class Animal:
    # 每個動物都有名字，所以在建立物件時先存入 name。
    def __init__(self, name):
        self.name = name

    # speak() 是動物發聲的共同介面。
    # 父類別先提供一個通用版本，子類別可以再根據需要改寫。
    def speak(self):
        return f"{self.name} 發出聲音"

    # __repr__ 用來顯示物件的開發者表示法。
    # 這裡使用 self.__class__.__name__ 可以自動顯示目前真正的類別名稱，
    # 即使是子類別物件，也會正確顯示 Dog、Cat 或 GuideDog。
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# -----------------------------------------------------------------------------
# 二、子類別：方法覆寫
# -----------------------------------------------------------------------------
# Dog 繼承 Animal，表示 Dog 也是一種 Animal。
# 但 Dog 的叫聲跟一般動物不同，所以直接覆寫 speak()。
class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"


# Cat 也繼承 Animal，並且同樣覆寫 speak()。
class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# -----------------------------------------------------------------------------
# 三、super()：呼叫父類別方法
# -----------------------------------------------------------------------------
# GuideDog 是 Dog 的子類別，代表導盲犬。
# 它除了有 Dog 的特性，還要多記錄主人資訊。
class GuideDog(Dog):
    # 在子類別的 __init__ 中，如果還想使用父類別的初始化邏輯，
    # 可以用 super().__init__(...) 呼叫上一層的初始化方法。
    # 這裡 super() 會先呼叫 Dog 的 __init__，而 Dog 沒有自己定義 __init__，
    # 所以最後會往上找到 Animal.__init__。
    def __init__(self, name, owner):
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__
        self.owner = owner

    # 這裡也覆寫 speak()，但不是完全取代父類別版本。
    # 而是先呼叫 super().speak() 取得 Dog 的叫聲，再加上額外資訊。
    def speak(self):
        base = super().speak()      # 呼叫 Dog.speak()
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立三個不同類別的物件。
# 雖然它們都屬於 Animal 家族，但實際表現會因子類別不同而不同。
d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

# 將不同類別的物件放在同一個串列中，然後逐一呼叫 speak()。
# 這正是多型的典型用法：同樣呼叫 speak()，但每個物件回傳的內容不同。
for animal in [d, c, g]:
    print(animal.speak())

# -----------------------------------------------------------------------------
# 四、isinstance / issubclass
# -----------------------------------------------------------------------------
# isinstance(obj, Class) 用來檢查物件是否屬於某個類別或其子類別。
# 這對型別判斷、條件分支、資料驗證都很有用。
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

# issubclass(Sub, Super) 用來檢查某個類別是否為另一個類別的子類別。
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False

# -----------------------------------------------------------------------------
# 五、多型（Polymorphism）
# -----------------------------------------------------------------------------
# 多型的意思是：同一個函式、同一個方法呼叫，
# 可以因為傳入的物件不同而產生不同的行為。
#
# make_sounds 不在乎傳進來的是 Dog、Cat 或 GuideDog，
# 它只要知道每個物件都有 speak() 就可以了。
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())        # 各自呼叫自己的 speak()


# 呼叫函式時，傳入不同種類的動物物件。
# 函式內部不需要特別分辨類別，物件自己會表現出正確的 speak() 行為。
make_sounds([d, c, g])

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# 繼承適合用在「is-a」關係，例如 Dog 是 Animal。
# 方法覆寫適合用在子類別需要不同實作時。
# super() 可避免重複寫父類別邏輯，也能保留父類別的初始化或共用功能。
# 多型則讓程式更彈性，避免大量 if/elif 判斷類別。
