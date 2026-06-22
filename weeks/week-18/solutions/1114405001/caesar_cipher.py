"""
Caesar Cipher Implementation (SHIFT=2)
"""

SHIFT = 2


def caesar_cipher(text):
    """
    Implement Caesar Cipher with SHIFT = 2
    
    Only lowercase and uppercase letters are shifted.
    Special characters, digits, and spaces remain unchanged.
    
    Args:
        text (str): Input text to encrypt
        
    Returns:
        str: Encrypted text with SHIFT=2
    """
    result = []
    
    for char in text:
        if 'a' <= char <= 'z':
            # Shift lowercase letters (a-z)
            new_char = chr((ord(char) - ord('a') + SHIFT) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters (A-Z)
            new_char = chr((ord(char) - ord('A') + SHIFT) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Keep other characters unchanged
            result.append(char)
    
    return ''.join(result)
