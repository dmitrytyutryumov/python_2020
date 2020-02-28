import math
from unittest import TestCase


class TestBuiltIns(TestCase):
	
	def test_numbers(a):
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
		assert round(2.5) == 3
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



	# def test_numbers():
	# 	base_dict = {}
	# 	base_list = []
	# 	base_set = set()
	# 	base_tuple = (1, 2, 3)
	# 	base_number = 1
	# 	base_string = 'Hello world!'
