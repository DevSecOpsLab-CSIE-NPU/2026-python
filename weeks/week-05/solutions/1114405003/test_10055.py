import unittest


def process_operations(function_count, operations):
    # 0 代表遞增，1 代表遞減；題目一開始全部都是遞增。
    state = [0] * (function_count + 1)
    answers = []

    for operation in operations:
        kind = operation[0]
        if kind == 1:
            index = operation[1]
            state[index] ^= 1
        else:
            left, right = operation[1], operation[2]
            # 複合函數的單調性只看區間內遞減函數的奇偶性。
            answers.append(sum(state[left : right + 1]) % 2)

    return answers


class TestUVA10055(unittest.TestCase):
    def test_toggle_and_query(self):
        # 這組測資同時檢查：切換一次、切換兩次、以及區間查詢。
        operations = [
            (2, 1, 5),
            (1, 3),
            (2, 1, 5),
            (1, 3),
            (2, 2, 4),
            (1, 2),
            (1, 4),
            (2, 2, 4),
        ]
        self.assertEqual(process_operations(5, operations), [0, 1, 0, 0])

    def test_multiple_updates_same_index(self):
        # 同一個函數翻轉兩次後，狀態應該回到原本的遞增。
        operations = [
            (1, 1),
            (1, 1),
            (2, 1, 1),
        ]
        self.assertEqual(process_operations(1, operations), [0])


if __name__ == "__main__":
    unittest.main()