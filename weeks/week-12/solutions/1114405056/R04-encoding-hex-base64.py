"""R04: hex and base64 encode/decode basics."""

import base64
import binascii

data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"

hex_str = binascii.b2a_hex(data)
print("b2a_hex:", hex_str)

hex_str2 = data.hex()
print(".hex():", hex_str2)

restored = binascii.a2b_hex(hex_str)
print("a2b_hex:", restored)

restored2 = bytes.fromhex(hex_str2)
print("fromhex:", restored2)

assert restored == data
assert restored2 == data

msg = b"Python Cookbook"
encoded = base64.b64encode(msg)
print("\nb64encode:", encoded)

decoded = base64.b64decode(encoded)
print("b64decode:", decoded)

url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe:", url_encoded)
