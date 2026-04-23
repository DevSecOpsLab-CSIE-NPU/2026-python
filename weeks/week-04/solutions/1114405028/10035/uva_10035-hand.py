# Hand version
a, b = '123', '456'
carry = 0
count = 0
i = len(a) - 1
j = len(b) - 1
while i >= 0 or j >= 0:
    x = int(a[i]) if i >= 0 else 0
    y = int(b[j]) if j >= 0 else 0
    if x + y + carry >= 10:
        count += 1
        carry = 1
    else:
        carry = 0
    i -= 1
    j -= 1
print("No carry operation." if count == 0 else f"{count} carry operation{'s' if count > 1 else ''}.")