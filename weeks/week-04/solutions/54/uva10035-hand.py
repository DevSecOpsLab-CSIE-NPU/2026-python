def count_carries(num1_str, num2_str):
    carries = 0
    carry = 0
    
    num1_str = num1_str[::-1]
    num2_str = num2_str[::-1]
    
    max_len = max(len(num1_str), len(num2_str))
    
    for i in range(max_len):
        d1 = int(num1_str[i]) if i < len(num1_str) else 0
        d2 = int(num2_str[i]) if i < len(num2_str) else 0
        
        sum_digits = d1 + d2 + carry
        if sum_digits >= 10:
            carries += 1
            carry = 1
        else:
            carry = 0
    
    return carries

while True:
    line = input().split()
    a, b = line[0], line[1]
    
    if a == '0' and b == '0':
        break
    
    result = count_carries(a, b)
    if result == 0:
        print("No carry")
    elif result == 1:
        print("1 carry operation")
    else:
        print(f"{result} carry operations")
