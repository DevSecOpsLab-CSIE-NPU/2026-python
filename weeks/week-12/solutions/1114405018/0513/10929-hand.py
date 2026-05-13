def is_multiple_of_11(number_text):
  
    odd_sum = 0     
    even_sum = 0     
    position = 1   
    
    for digit_char in reversed(number_text):
        digit = int(digit_char)
        
        if position % 2 == 1:
            odd_sum += digit
        else:
            even_sum += digit
        
        position += 1
    
    difference = odd_sum - even_sum
   
    return difference % 11 == 0

def main():
  
    while True:
       
        n = input().strip()
        
        if n == "0":
            break
       
        result = "is a multiple of 11." if is_multiple_of_11(n) else "is not a multiple of 11."
        
        print(f"{n} {result}")


if __name__ == "__main__":
    main()
