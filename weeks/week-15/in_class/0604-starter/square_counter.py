import os
import importlib.util

here = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(here, '..', '..', 'solutions', '1114405006-0604'))
target = os.path.join(root, 'square_counter.py')

spec = importlib.util.spec_from_file_location('solutions_square_counter', target)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

count_squares = mod.count_squares
