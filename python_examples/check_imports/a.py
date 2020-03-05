import b
from c import atrrubute_from_c

atrrubute_from_a = 1
print(__name__)

# b.atrrubute_from_b
# Traceback (most recent call last):
#   File "a.py", line 1, in <module>
#     import b
#   File "/home/dmitry/Documents/BSUIR/python_2020/python_examples/check_imports/b.py", line 1, in <module>
#     import a
#   File "/home/dmitry/Documents/BSUIR/python_2020/python_examples/check_imports/a.py", line 7, in <module>
#     b.atrrubute_from_b
# AttributeError: module 'b' has no attribute 'atrrubute_from_b'

if __name__ == '__main__':
	print('Start a')
