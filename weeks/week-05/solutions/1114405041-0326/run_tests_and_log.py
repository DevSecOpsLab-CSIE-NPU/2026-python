import io
import pathlib
import unittest

suite = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
buf = io.StringIO()
result = unittest.TextTestRunner(stream=buf, verbosity=2).run(suite)
text = buf.getvalue()
text += '\n' + '-' * 70 + '\n'
text += f'Ran {result.testsRun} tests\n'
text += 'OK\n' if result.wasSuccessful() else 'FAILED\n'
pathlib.Path('TEST_LOG.md').write_text(text, encoding='utf-8')
print(text)
raise SystemExit(0 if result.wasSuccessful() else 1)
