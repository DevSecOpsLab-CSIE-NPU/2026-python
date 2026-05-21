# 測試檔：test_R01_function_signatures.py
# 目的：針對 R01-function-signatures.py 的函式彈性簽章概念撰寫單元測試
#
# 說明：
# 1) 使用 Python 內建 unittest。
# 2) 以詳細繁體中文註解說明每個測試案例的目的與預期。
# 3) 原始教學檔在匯入時會有示範 print，屬正常現象，不影響測試正確性。

import importlib.util
import os
import unittest


def load_r01_module():
    """動態載入 R01 教學檔，回傳模組物件。"""
    module_path = os.path.join(os.path.dirname(__file__), "R01-function-signatures.py")
    spec = importlib.util.spec_from_file_location("r01_function_signatures", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R01 = load_r01_module()


class TestR01FunctionSignatures(unittest.TestCase):
    """測試 R01 的核心主題：*args、**kwargs、keyword-only 與混合參數簽章。"""

    def test_add_all_with_multiple_inputs(self):
        # 驗證 add_all(*args) 能處理多個位置參數。
        self.assertEqual(R01.add_all(1, 2, 3, 4, 5), 15)

    def test_add_all_with_single_input(self):
        # 單一參數時，結果應等於該值本身。
        self.assertEqual(R01.add_all(10), 10)

    def test_add_all_with_empty_args(self):
        # 空參數是重要邊界案例：sum(()) 應回傳 0。
        self.assertEqual(R01.add_all(), 0)

    def test_make_student_collects_kwargs_into_dict(self):
        # make_student(**kwargs) 應原樣回傳 dict 結構與內容。
        student = R01.make_student(name="王小明", grade=85, seat=12)
        self.assertEqual(student["name"], "王小明")
        self.assertEqual(student["grade"], 85)
        self.assertEqual(student["seat"], 12)

    def test_send_score_accepts_keyword_only_arguments(self):
        # send_score(student_id, *, subject, score)
        # subject 與 score 必須具名呼叫；此案例應可順利執行。
        R01.send_score("411234001", subject="數學", score=90)

    def test_send_score_raises_type_error_when_positional(self):
        # 若錯把 keyword-only 參數用位置方式傳入，應拋出 TypeError。
        with self.assertRaises(TypeError):
            R01.send_score("411234001", "數學", 90)

    def test_report_runs_with_and_without_scores(self):
        # report(title, *scores, prefix="成績") 主要是輸出函式，
        # 這裡重點驗證不同呼叫型態都能正確執行且不拋例外。
        R01.report("期中考", 80, 90, 70)
        R01.report("期末考", 95, 85, 75, 100, prefix="最終")
        R01.report("補考")  # 空 scores 情況也應可執行（平均值邏輯為 0）


if __name__ == "__main__":
    unittest.main(verbosity=2)
