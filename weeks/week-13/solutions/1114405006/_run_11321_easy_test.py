import importlib.util, os
p = r'd:\0520-1114405006\2026-python\weeks\week-13\1114405006\question_11321-easy.py'
spec = importlib.util.spec_from_file_location('qe', p)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

cases = [ (3,3,[(0,1),(1,1),(2,1)]), (1,1,[(0,0)]), (2,2,[(0,0),(1,0)]) ]
for L,M,proposals in cases:
    print('case',L,M,proposals,'->', mod.simulate_traps_easy(L,M,proposals))
