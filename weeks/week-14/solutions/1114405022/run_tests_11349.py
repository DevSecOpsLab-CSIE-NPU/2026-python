"""
Run unittest and write human-readable log to test_log_11349.txt
"""
import io
import sys
import unittest

loader = unittest.defaultTestLoader
suite = loader.loadTestsFromName('weeks.week-14.solutions.1114405022.test_11349_symmetric')

buf = io.StringIO()
runner = unittest.TextTestRunner(stream=buf, verbosity=2)
result = runner.run(suite)

with open('test_log_11349.txt', 'w', encoding='utf-8') as f:
    f.write(buf.getvalue())

# Exit with non-zero code if tests failed
sys.exit(0 if result.wasSuccessful() else 1)
