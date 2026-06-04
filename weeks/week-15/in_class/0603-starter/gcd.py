import os
import importlib.util

here = os.path.dirname(__file__)
# from starter (weeks/week-15/in_class/0603-starter) go up two levels to reach week-15
root = os.path.abspath(os.path.join(here, '..', '..', 'solutions', '1114405006'))
target = os.path.join(root, 'gcd.py')

spec = importlib.util.spec_from_file_location('solutions_gcd', target)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sum_of_gcd = mod.sum_of_gcd
