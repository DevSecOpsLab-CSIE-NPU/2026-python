# R02-property.py
# 使用 @property 實作封裝、getter/setter 驗證及計算屬性

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = 0  # 私有變數慣例
        self.price = price  # 會觸發 setter

    @property
    def price(self):
        """Getter: 取得價格"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: 設定價格並包含邏輯驗證"""
        if value < 0:
            print("錯誤：價格不能為負數，設定為 0")
            self._price = 0
        else:
            self._price = value

    @property
    def discounted_price(self):
        """計算屬性: 自動根據目前價格算出折扣價"""
        return self._price * 0.8

if __name__ == "__main__":
    print("=== @property 封裝示範 ===")
    p = Product("Laptop", 1000)
    print(f"品名: {p.name}, 價格: {p.price}")
    
    p.price = 1200
    print(f"調漲後價格: {p.price}, 折扣價: {p.discounted_price}")
    
    p.price = -50  # 測試驗證邏輯
    print(f"嘗試設定負數後價格: {p.price}")
