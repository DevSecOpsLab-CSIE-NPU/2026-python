# R03. 繼承與 super()（8.7）
# 主題：繼承 / 方法覆寫 / super() / isinstance / issubclass
# 註解語言：繁體中文（臺灣 zh-TW），並補充物件設計與多個實例變數的使用

# ── 基底類別 ─────────────────────────────────────────────
# 這裡用 `Animal` 當作基底類別（父類別）。
# 子類別會繼承它的共同屬性與方法，並在必要時進行擴充或覆寫。
class Animal:
    # `__init__` 用來初始化動物的基本資料。
    # 這次除了 name，還加入 species、age、sound、color 等實例變數，
    # 讓物件可以記錄更完整的狀態。
    def __init__(self, name, species="未知", age=0, sound="...", color="未知"):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.color = color

    # 基底方法：由子類別視需要覆寫。
    def speak(self):
        return f"{self.name} 發出聲音：{self.sound}"

    # 提供開發者使用的字串表示。
    # `self.__class__.__name__` 可以取得目前實例的實際類別名稱，
    # 這樣即使是子類別實例，也能顯示正確名稱。
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, species={self.species!r}, age={self.age!r})"

    # 提供使用者可讀的字串表示。
    def __str__(self):
        return f"{self.name}（{self.species}，{self.age} 歲，顏色：{self.color}）"

    # 額外方法：回傳更完整的資訊摘要。
    def info(self):
        return f"名稱：{self.name}｜種類：{self.species}｜年齡：{self.age}｜顏色：{self.color}"


# ── 子類別：覆寫方法 ──────────────────────────────────────
# Dog 繼承 Animal，並把自己的預設聲音改成「汪汪！」
class Dog(Animal):
    def __init__(self, name, age=0, color="黑色", breed="米克斯"):
        # `super().__init__()` 會呼叫父類別 Animal 的初始化方法，
        # 讓 name、species、age、sound、color 等共用欄位先建立好。
        super().__init__(name, species="狗", age=age, sound="汪汪！", color=color)
        # 新增子類別專屬的實例變數：品種
        self.breed = breed

    def speak(self):
        # 覆寫父類別方法，讓狗叫聲更符合真實情境。
        return f"{self.name}（{self.breed}）說：汪汪！"

    def __repr__(self):
        return f"Dog({self.name!r}, age={self.age!r}, color={self.color!r}, breed={self.breed!r})"

    def __str__(self):
        return f"狗狗 {self.name}｜品種：{self.breed}｜年齡：{self.age}｜顏色：{self.color}"


class Cat(Animal):
    def __init__(self, name, age=0, color="白色", indoor=True):
        super().__init__(name, species="貓", age=age, sound="喵～", color=color)
        # 內外室屬性：True 表示家貓，False 表示較常出門
        self.indoor = indoor

    def speak(self):
        return f"{self.name} 說：喵～"

    def __repr__(self):
        return f"Cat({self.name!r}, age={self.age!r}, color={self.color!r}, indoor={self.indoor!r})"

    def __str__(self):
        place = "室內貓" if self.indoor else "戶外貓"
        return f"貓咪 {self.name}｜{place}｜年齡：{self.age}｜顏色：{self.color}"


# ── super()：呼叫父類別方法 ───────────────────────────────
# GuideDog 繼承 Dog，也就間接繼承 Animal。
# 這裡示範如何在子類別中先使用父類別初始化，再加入自己的專屬屬性。
class GuideDog(Dog):
    def __init__(self, name, owner, age=0, color="金色", breed="拉布拉多", trained=True):
        super().__init__(name, age=age, color=color, breed=breed)
        self.owner = owner
        self.trained = trained
        self.role = "導盲犬"

    def speak(self):
        # 先呼叫父類別的 speak()，再加上導盲犬資訊。
        base = super().speak()
        return f"{base}（{self.role}，主人：{self.owner}）"

    def __repr__(self):
        return (
            f"GuideDog({self.name!r}, owner={self.owner!r}, age={self.age!r}, "
            f"color={self.color!r}, breed={self.breed!r}, trained={self.trained!r})"
        )

    def __str__(self):
        status = "已受訓" if self.trained else "未受訓"
        return f"{self.role} {self.name}｜主人：{self.owner}｜{status}｜品種：{self.breed}"


# ── 建立實例 ──────────────────────────────────────────────
d = Dog("小黑", age=3, color="黑色", breed="柴犬")
c = Cat("咪咪", age=2, color="白色", indoor=True)
g = GuideDog("阿金", "王伯伯", age=5, color="金色", breed="拉布拉多", trained=True)

# 印出各自的 speak() 結果，觀察多型與方法覆寫的效果
for animal in [d, c, g]:
    print(animal.speak())

print("\n=== 物件資訊 ===")
print(repr(d))
print(str(c))
print(g.info())
print(g)

# ── isinstance / issubclass ───────────────────────────────
# `isinstance()` 用來判斷「某個物件是不是某個類別的實例」。
# `issubclass()` 用來判斷「某個類別是不是另一個類別的子類別」。
print("\n=== 型別判斷 ===")
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）
print(isinstance(d, Cat))       # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False
print(issubclass(GuideDog, Dog))

# ── 多型（Polymorphism）──────────────────────────────────
# 多型的核心概念：同一個方法名稱，對不同物件會表現出不同結果。
def make_sounds(animals: list):
    for a in animals:
        print(a.speak())        # 各自呼叫自己的 speak()

print("\n=== 多型示範 ===")
make_sounds([d, c, g])

# ── 額外操作：修改實例變數 ────────────────────────────────
# 物件建立後，仍然可以修改某些實例變數，這會直接影響該實例的狀態。
d.age = 4
c.indoor = False
g.trained = False
print("\n=== 修改後狀態 ===")
print(d)
print(c)
print(g)

# ── 常見提醒 ─────────────────────────────────────────────
# - 父類別放「共用」的資料與行為，子類別放「特定」的資料與行為。
# - 子類別如果有相同名稱的方法，可以覆寫（override）父類別的方法。
# - `super()` 可用來呼叫父類別的初始化或一般方法，避免重複寫相同邏輯。
# - `__repr__` 適合除錯，`__str__` 適合顯示給使用者看。
# - 多個實例變數可以同時存在於同一個物件中，例如 name、species、age、color、breed。
