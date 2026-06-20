import unittest
import ast
import os
import tempfile
import json
from task1_csv_to_json import count_by_dept, write_json

class TestSecurity(unittest.TestCase):

    def test_import_os_at_top(self):
        for fname in ["task1_csv_to_json.py", "task2_json_to_xml.py"]:
            with open(fname, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            imports_in_func = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for child in ast.iter_child_nodes(node):
                        if isinstance(child, ast.Import) and any(a.name == "os" for a in child.names):
                            imports_in_func.append((node.name, child.lineno))
            self.assertEqual(len(imports_in_func), 0,
                             f"{fname}: import os 出現在函式內: {imports_in_func}")

    def test_count_by_dept_rejects_non_dict(self):
        with self.assertRaises(TypeError):
            count_by_dept(["not_a_dict"])

    def test_count_by_dept_keeps_empty_string(self):
        rows = [{"系所名稱": ""}, {"系所名稱": "電機系"}, {"系所名稱": ""}]
        result = count_by_dept(rows)
        self.assertIn("", result)
        self.assertEqual(result[""], 2)

    def test_write_json_uses_json_not_pickle(self):
        data = {"test": 1}
        tmp = tempfile.mktemp(suffix=".json")
        write_json(data, tmp)
        with open(tmp, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn('"test"', content)
        os.unlink(tmp)
        self.assertFalse(tmp.endswith(".pkl"))
