import unittest

def decode_mad_man(text, shift=3):
    """
    這是解碼的核心邏輯：
    text: 要解碼的文字
    shift: 向左位移的格數（根據你的題目敘述為 3）
    """
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    text = text.lower()
    result = []
    
    for char in text:
        if char == ' ' or char == '\n':
            result.append(char)
        else:
            idx = keyboard.find(char)
            if idx != -1:
                # 執行位移
                result.append(keyboard[idx - shift])
            else:
                result.append(char)
    
    return "".join(result)

# --- 以下為測試用程式 ---

class TestDecodeMadMan(unittest.TestCase):

    def test_basic_words(self):
        """測試基本單字位移 (左移 3 位)"""
        # 假設 r 往左移三格是 q (根據你的敘述)
        # r(13) -> e(12) -> w(11) -> q(10)
        self.assertEqual(decode_mad_man("r"), "q")
        self.assertEqual(decode_mad_man("4"), "1")

    def test_sentence(self):
        """測試整個句子與空格"""
        # 輸入 "r t y" 應該得到 "q 1 2"
        self.assertEqual(decode_mad_man("r t y"), "q 1 2")

    def test_uva_standard(self):
        """
        測試標準 UVA 10222 邏輯 (左移 2 位)
        如果你的題目其實是標準 UVA，請將參數改為 2
        """
        input_str = "k[ i d"
        # k(左移2) -> h, [(左移2) -> o, i(左移2) -> y, d(左移2) -> a
        self.assertEqual(decode_mad_man(input_str, shift=2), "how a")

if __name__ == "__main__":
    # 執行測試
    unittest.main()