import warnings
def old(): warnings.warn('Deprecated!', DeprecationWarning, stacklevel=2)
if __name__ == '__main__':
    warnings.simplefilter('always')
    old()
