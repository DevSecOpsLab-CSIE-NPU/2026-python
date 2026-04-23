import importlib.util

# Test 272-easy
spec = importlib.util.spec_from_file_location("easy272", "272-easy.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("Test 272-easy quote logic:")
result = mod.process_tex_quotes('"Hello"')
print(f'  "Hello" -> {result}')
assert result == "``Hello''", f"Expected ``Hello'' but got {result}"
result = mod.process_tex_quotes('"To be or not to be," quoth the bard, "that is the question."')
print(f'  Multiple quotes processed: OK')
assert result == "``To be or not to be,'' quoth the bard, ``that is the question.''"
print("✓ 272-easy PASS\n")

# Test 299-easy
spec = importlib.util.spec_from_file_location("easy299", "299-easy.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("Test 299-easy bubble sort logic:")
result = mod.count_swaps([1, 3, 2])
print(f'  count_swaps([1, 3, 2]) = {result}')
assert result == 1, f"Expected 1 but got {result}"
result = mod.count_swaps([3, 2, 1])
print(f'  count_swaps([3, 2, 1]) = {result}')
assert result == 3, f"Expected 3 but got {result}"
result = mod.count_swaps([1, 2, 3])
print(f'  count_swaps([1, 2, 3]) = {result}')
assert result == 0, f"Expected 0 but got {result}"
result = mod.count_swaps([4, 3, 2, 1])
print(f'  count_swaps([4, 3, 2, 1]) = {result}')
assert result == 6, f"Expected 6 but got {result}"
print("✓ 299-easy PASS\n")

print("=" * 50)
print("All logic verification PASSED!")
print("=" * 50)
