import io, unittest
loader = unittest.defaultTestLoader
suite = loader.discover('.', pattern='test_question_11332_easy.py')
stream = io.StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
result = runner.run(suite)
with open('test_results_11332_easy.txt', 'w', encoding='utf-8') as f:
    f.write(stream.getvalue())
print('WROTE test_results_11332_easy.txt')
