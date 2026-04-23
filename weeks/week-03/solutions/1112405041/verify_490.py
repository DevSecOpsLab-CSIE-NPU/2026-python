import importlib.util

# Test 490
spec = importlib.util.spec_from_file_location("easy490", "490-easy.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("Test 490 text rotation logic:")
result = mod.rotate_text(["HELLO", "WORLD"])
print(f'  Input: ["HELLO", "WORLD"]')
print(f'  Output: {result}')
expected = ["WH", "OE", "RL", "LL", "DO"]
assert result == expected, f"Expected {expected} but got {result}"
print("✓ 490-easy PASS\n")

# Now check formal version
spec = importlib.util.spec_from_file_location("formal490", "490.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("Test 490 formal rotation logic:")
rotator = mod.TextRotator()
result = rotator.rotate_90_clockwise(["HELLO", "WORLD"])
print(f'  rotate_90_clockwise: {result}')
assert result == expected, f"Expected {expected} but got {result}"

result = rotator.rotate_90_clockwise(["ABC"])
expected_single = ["A", "B", "C"]
print(f'  Single line ["ABC"]: {result}')
assert result == expected_single, f"Expected {expected_single} but got {result}"

result = rotator.rotate_90_clockwise([])
print(f'  Empty input: {result}')
assert result == [], f"Expected [] but got {result}"

print("✓ 490 formal PASS\n")

print("=" * 50)
print("All UVA 490 logic verification PASSED!")
print("=" * 50)
