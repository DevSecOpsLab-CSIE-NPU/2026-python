import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ?ÆÂ?Ê∏¨Ë©¶Ôºö‰∏ªÈ°?12ÔºàÂ?‰∏≤Ê†ºÂºèÂ?Ôº?

import unittest
import sys
import importlib

# ?ïÊ?Â∞éÂÖ• 12_formal Ê®°Á?
formal_12 = importlib.import_module('12_hand')
format_price = formal_12.format_price
format_with_method = formal_12.format_with_method
format_precision = formal_12.format_precision
number_bases = formal_12.number_bases

class TestStringFormatting(unittest.TestCase):
    
    def test_format_price_fstring(self):
        """Ê∏¨Ë©¶ f-string ?ºÂ???""
        result = format_price('ACME', 91.1)
        self.assertEqual(result, 'ACME price = 91.10')
    
    def test_format_price_method(self):
        """Ê∏¨Ë©¶ format ?πÊ?"""
        result = format_with_method('ACME', 91.1)
        self.assertEqual(result, 'ACME price = 91.10')
    
    def test_format_precision(self):
        """Ê∏¨Ë©¶ÊµÆÈ??∏Á≤æÂ∫?""
        result = format_precision(3.14159, 2)
        self.assertEqual(result, '3.14')
    
    def test_number_bases(self):
        """Ê∏¨Ë©¶?≤‰??∂Ë???""
        result = number_bases(255)
        self.assertEqual(result['hex'], 'ff')
        self.assertEqual(result['binary'], '11111111')
        self.assertEqual(result['octal'], '377')

if __name__ == '__main__':
    unittest.main()
