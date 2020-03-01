# coding=utf-8

import collections
import math
import re
from unittest import TestCase


class TestBuiltIns(TestCase):
	
	def test_numbers(*args):
		assert 1 + 1 == 2
		assert 5 - 2 == 3

		assert 5 * 2 == 10
		assert 10 / 5 == 2
		assert 11 % 6 == 5
		assert 13 // 2 + 1 == 7
		
		assert 2**3 == 8
		assert pow(2, 3) == 8
		assert math.pow(2, 3) == 8

		assert abs(-111.123) == 111.123

		assert round(math.pi, 2) == 3.14
		assert round(2.5) == 2
		assert round(1.5) == 2
		
		assert math.ceil(2.5) == 3
		assert math.ceil(1.5) == 2

		assert math.sqrt(144) == 12

		assert int(123.333) == 123
		assert float(123) == 123.0


		assert (6 > 4) is True 
		assert (6 < 4) is False 
		assert (6 > 4 < 5) is True 
		assert (6 > 4 and 5.0 == 5) is True 
		assert 1j * 1J == (-1+0j)	

		# режим отображения чисел

		number = 0.78000000000000000000012
		assert number.__str__() == number.__repr__() == '0.78'
		assert str(number) == repr(number) == '0.78'

		#  str > __str__ -> читаемый вид
		#  repr > __repr__ -> отладочный вид

		assert number == 0.78000000000000000000012

	def test_string(*args):
		"""
		Описание функции. Док стринг тоже является строкой
		"""

		assert isinstance('s', str)
		assert isinstance("s", str)
		multi_line =  '''
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
			Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
			dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
			sunt in culpa qui officia deserunt mollit anim id est laborum.
		'''.strip()
		assert isinstance(multi_line, str)
		assert isinstance("""s""", str)
		assert isinstance(str(object), str)
		assert isinstance(repr(object), str)

		# срезы
		assert multi_line[0] == 'L'
		assert multi_line[-1] == '.'
		assert multi_line[::-1][1:8] == ''.join(reversed(multi_line))[1:8] == 'murobal'

		# конкатенация
		hey = 'hey'
		students = 'students'

		assert ('hey' ' ' 'students') == 'hey students'
		assert 'hey' + ' ' + 'students' == 'hey students'
		assert hey * 2 == 'heyhey'

		# cравнение
		assert 'hey' is 'hey'
		assert hey == hey
		assert (hey < students) == True

		assert 'e' in hey

		# форматирование строк
		assert ' '.join(['hey', 'students']) == 'hey students'
		assert f'{hey} {students}' == 'hey students'
		assert '{hey} {students}'.format(hey=hey, students=students) == 'hey students'
		assert '%s %s' %(hey, students) == 'hey students'

		# длина строки
		assert len(multi_line) == 465
		assert multi_line.__len__() == 465

		# методы
		assert 'labore'.capitalize()[0] == multi_line.title()[97] == 'l'.upper() == 'L'
		assert 'l' == 'L'.lower()
		assert 'asdasd'.split('s') == ['a', 'da', 'd']

		assert '/some/file/path'.replace('path', 'path.txt') == '/some/file/path.txt'
		assert re.sub(r'^/[a-z]*/', '/home/', '/some/file/path') == '/home/file/path'
		assert ''.join([i for i in multi_line if i == 'l']) == 'lllllllllllllllllllll'

		#экранирование
		'\s\t\n'

	def test_lists(*args):
		list_ex = ['1', 1, {}]
		list_ex = list_ex + [123]
		assert list_ex == ['1', 1, {}, 123]
		list_ex.append(123)
		assert list_ex == ['1', 1, {}, 123, 123]
		
		list_ex.clear()
		assert list_ex == []

		list_ex = [2]
		list_ex = list_ex * 2
		assert list_ex == [2, 2] 	
		
		assert list_ex.index(2) == 0
		assert list_ex[1] == 2
		list_ex.append(1)
		assert list_ex[::-1] == [1, 2, 2]
		list_ex.sort()
		assert list_ex == [1, 2, 2]
		list_ex.reverse() 
		assert list_ex == [2, 2, 1]
		assert list_ex[1:-1] == [2]
		assert list_ex.pop() == 1
		list_ex.extend([1, 2, 3])
		assert list_ex == [2, 2, 1, 2, 3]
		list_ex = [i for i in range(0, 5, 2)]
		assert list_ex == [0, 2, 4]

		assert 0 in list_ex

	def test_sets(*args):
		set_ex = {'1', 1, (1, )}
		set_ex.add(123)
		assert set_ex == {'1', 1, (1, ), 123}		

		set_ex.update({1, 2, 3})
		assert set_ex == {1, '1', 2, 3, (1,), 123}
		set_ex = set(i for i in range(0, 5, 2))
		assert set_ex == set(i for i in range(0, 5, 2))

		assert 0 in set_ex
		set_ex.clear()
		assert {1, 2, 3, 1, 1, 1, 1} == {1, 2, 3}

	def tests_tuples(*args):
		a = 1, 2, 3, 
		assert a == tuple([1, 2, 3]) == tuple(i for i in range(1, 4))
		assert a[1] == a.index(3) == 2
		assert a[::-1] == (3, 2, 1,) 

	def tests_dicts(*args):
		assert dict(one=1, two=2, three=3) == {'one': 1, 'two': 2, 'three': 3}
		assert dict([('two', 2), ('one', 1), ('three', 3)]) == dict(zip(['one', 'two', 'three'], [1, 2, 3])) 

		dict_ex = {'one': 1, 'two': 2}
		assert list(dict_ex) == list(dict_ex.keys()) == ['one', 'two']
		assert len(dict_ex) == 2
		assert 'one' in dict_ex

		assert list(dict_ex.values()) == [1, 2]
		assert dict_ex['one'] == 1  # если ключа нет -- KeyError 

		dict_ex.update({6: 1})
		assert dict_ex == {6: 1, 'one': 1, 'two': 2}
		assert dict_ex.pop(6) == 1
		assert dict_ex.popitem() == ('two', 2)
		dict_ex.clear()
		assert dict_ex == {}

		dict_ex[1] = 1
		assert dict_ex[1] == 1
		del dict_ex[1]
		assert dict_ex == {}

		dict_ex = {idx: str(v) for idx, v in enumerate(range(5))}
		assert dict_ex == {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

		dict_ex = collections.OrderedDict(sorted({1: 's', 5: 'a', 2: '5'}.items(), key=lambda x: x[0]))
		assert dict_ex == collections.OrderedDict([(1, 's'), (2, '5'), (5, 'a')])

		class Cache(dict):
			def __missing__(self, key):
				return 0

			def __getitem__(self, item):
				print('item')
				value = super(Cache, self).__getitem__(item)
				return value * 2

			def get(self, k, v=0):
				value = super(Cache, self).get(k, v)
				return value * 3

		ex = Cache({1: 1})
		assert ex[0] == 0
		assert ex[1] == 2
		assert ex.get(1) == 3

	def test_bool(*args):
		True is True 
		False is False
		assert True == bool({1, }) == bool([1, 2, ]) == bool({1:1})
		assert False == bool({}) == bool([])

	def test_files(*args):
		text = '''
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
			Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
			dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
			sunt in culpa qui officia deserunt mollit anim id est laborum.
		'''
		with open('./new_file.txt', 'w') as file:
			file.write(text)

		with open('./new_file.txt') as file:
			for line in file.readlines():
				assert line in text
			assert file.read() == ''
			file.seek(0)
			assert file.read() == text	
