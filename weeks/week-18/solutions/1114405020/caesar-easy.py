import sys


def encrypt_caesar(text: str, shift: int = 1) -> str:
    """【AI 教學版】凱撒密碼加密

    包含詳細繁體中文註解，適合教學與初學者閱讀。
    """
    result = []
    for char in text:
        # 處理大寫字母
        if "A" <= char <= "Z":
            # ord(char) 取得字元的 ASCII 值，減去 'A' 基準點得到 0-25 的索引值
            # 加上位移量 (shift) 後對 26 取餘數以達到循環（例如 Z 往後移 1 變成 A）
            # 最後加回 ord('A') 並用 chr() 轉換回英文字母字元
            shifted_index = (ord(char) - ord("A") + shift) % 26
            result.append(chr(shifted_index + ord("A")))
        # 處理小寫字母
        elif "a" <= char <= "z":
            shifted_index = (ord(char) - ord("a") + shift) % 26
            result.append(chr(shifted_index + ord("a")))
        # 非英文字母直接原樣保留（標點符號、空格、中文、數字等）
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    # 透過 sys.stdin 讀取標準輸入，會自動分行且完美處理 EOF (Ctrl+D 或檔案結尾)
    for line in sys.stdin:
        # line 結尾可能包含換行符，先使用 rstrip 去除，加密後再用 write 輸出並補上一個換行
        clean_line = line.rstrip("\r\n")
        encrypted = encrypt_caesar(clean_line, 1)  # 學號末碼為 0，SHIFT = 1
        sys.stdout.write(encrypted + "\n")
