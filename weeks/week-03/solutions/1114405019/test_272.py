import unittest

def process_line(line):
    result = []
    quote_count = 0
    for char in line:
        if char == '"':
            quote_count += 1
            if quote_count % 2 == 1:
                result.append('``')
            else:
                result.append("''")
        else:
            result.append(char)
    return ''.join(result)

class Test272(unittest.TestCase):

    def test_process_line(self):
        self.assertEqual(process_line('"Hello"'), '``Hello\'\'')
        self.assertEqual(process_line('"To be or not to be," quoth the bard, "that is the question."'),
                         '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\'')

if __name__ == '__main__':
    unittest.main()