try: 1/0
except ZeroDivisionError as e: print(f'Caught expected error: {e}')
finally: print('Cleanup complete')
