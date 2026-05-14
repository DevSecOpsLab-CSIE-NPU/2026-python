# R03. 繼承與 super()（8.7）
# 繼承 / 方法覆寫 / super() / isinstance / issubclass

# ── 基底類別 ─────────────────────────────────────────────

# class Animal：
# Animal 是基底類別（base class）
# 也稱為：
# 1. 父類別（parent class）
# 2. 超類別（superclass）

# Animal 定義所有動物共同的功能
class Animal:

    # __init__()：
    # 建構子

    # name：
    # 動物名稱
    def __init__(self, name):

        # self.name：
        # 儲存動物名字
        self.name = name

    # speak()：
    # 動物發出聲音的方法
    def speak(self):

        # f-string：
        # 組合字串
        return f"{self.name} 發出聲音"

    # __repr__()：
    # 提供開發者看的物件表示方式
    def __repr__(self):

        # self.__class__.__name__：
        # 取得目前物件的類別名稱

        # 例如：
        # Dog
        # Cat
        # GuideDog

        # !r：
        # 使用 repr() 格式輸出字串

        # 例如：
        # '小黑'
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別：覆寫方法 ──────────────────────────────────────

# class Dog(Animal)：
# Dog 繼承 Animal

# 繼承後：
# Dog 自動擁有：
# 1. __init__()
# 2. speak()
# 3. __repr__()

# 除非自己重新定義（覆寫）
class Dog(Animal):

    # 覆寫（override）speak()

    # 子類別提供自己的版本
    # 取代父類別原本方法
    def speak(self):

        # 狗自己的叫聲
        return f"{self.name} 說：汪汪！"


# Cat 類別
# 同樣繼承 Animal
class Cat(Animal):

    # 覆寫 speak()
    def speak(self):

        # 貓的叫聲
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────

# GuideDog：
# 導盲犬類別

# GuideDog 繼承 Dog
# Dog 又繼承 Animal

# 繼承鏈：
# GuideDog → Dog → Animal
class GuideDog(Dog):

    # GuideDog 自己的建構子
    def __init__(self, name, owner):

        # super()：
        # 取得父類別物件

        # super().__init__(name)：
        # 呼叫父類別的 __init__()

        # 這裡：
        # Dog 沒有自己的 __init__
        # 所以會往上找到 Animal.__init__

        # 等同：
        # Animal.__init__(self, name)
        super().__init__(name)      # 呼叫 Dog → Animal 的 __init__

        # owner：
        # 導盲犬主人
        self.owner = owner

    # 覆寫 speak()
    def speak(self):

        # super().speak()：
        # 呼叫父類別版本的 speak()

        # 這裡會呼叫：
        # Dog.speak()
        base = super().speak()      # 呼叫 Dog.speak()

        # 在父類別結果基礎上增加內容
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立 Dog 物件
d = Dog("小黑")

# 建立 Cat 物件
c = Cat("咪咪")

# 建立 GuideDog 物件
g = GuideDog("阿金", "王伯伯")

# list 中放入不同類別物件
for animal in [d, c, g]:

    # 雖然型態不同
    # 但都可以呼叫 speak()

    # Python 會自動使用：
    # 「該物件自己的 speak()」
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────

# isinstance(obj, 類別)：
# 檢查 obj 是否為某類別的實例

# d 是 Dog 物件
# 所以結果 True
print(isinstance(d, Dog))       # True

# Dog 繼承 Animal
# 所以 Dog 物件同時也是 Animal
print(isinstance(d, Animal))    # True（Dog 是 Animal 的子類別）

# d 不是 Cat
print(isinstance(d, Cat))       # False

# issubclass(子類別, 父類別)：
# 檢查是否有繼承關係

# Dog 繼承 Animal
print(issubclass(Dog, Animal))  # True

# Cat 沒有繼承 Dog
print(issubclass(Cat, Dog))     # False

# ── 多型（Polymorphism）──────────────────────────────────

# 多型（Polymorphism）：
# 不同類別物件
# 可以用相同方式操作

# make_sounds()：
# 接收動物 list
def make_sounds(animals: list):

    # 逐一處理動物
    for a in animals:

        # 不需要知道：
        # a 是 Dog、Cat 或 GuideDog

        # 只要有 speak() 方法即可

        # Python 會自動呼叫：
        # 各自類別自己的 speak()
        print(a.speak())        # 各自呼叫自己的 speak()

# 呼叫函式
make_sounds([d, c, g])