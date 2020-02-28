# coding=utf-8

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
		pass

	def test_sets(*args):
		pass

	def tests_tuples(*args):
		pass

	def tests_dicts(*args):
		pass

	def test_bool(*args):
		pass

	def test_None(*args):
		pass
