import io, unittest, datetime

loader = unittest.defaultTestLoader
suite = loader.discover('.', pattern='test_question_*.py')
stream = io.StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
result = runner.run(suite)

now = datetime.datetime.now().isoformat()
outfile = 'test_results_week13_full.txt'
with open(outfile, 'w', encoding='utf-8') as f:
    f.write(f'# Test run at {now}\n')
    f.write(stream.getvalue())

print('WROTE', outfile)
