from copy import copy, deepcopy


def test_numbers():
	a = 1
	b = a
	b += 1
	a += 2
	return a, b


def test_string():
	a = 'string'
	b = a
	b += '_new'

	return a[5:-1], b


def test_list():
	a = [1, 2, 3]
	b = a.copy()
	b.append(4)
	a.append(5)

	return a, b


def test_list_1():
	a = [1, 2, 3]
	b = [3, 2, 1]

	a.extend(b)
	b *= 2
	return a, b


def test_dict():
	a = {1: 1}
	b = dict()
	a.update(b)
	b[3] = 2
	return a, b


def test_dict_1():
	a = {1: 1}
	b = {2: None, 3: None, 4: None}
	a = b
	b = deepcopy(a).update({4: 4})
	return a, b


def test_dict_2():
	a = {1: 2, 3: {4: 5}, 7: [1, 3, 4]}
	b = a[7]
	b.pop(0)
	return a, b


def test_tuple():
	a = 1, 2, 3,
	b = tuple([1, 2, 3])
	return a==b


def test_tuple_1():
	a = (1, 2, 3,)
	b = a 
	a = (1, 2, )
	return a, b


def test_set():
	a = {1, 2, 3}
	b = set([1, 2, 3])
	return a == b, a is b


def test_bool():
	return True == 1 == bool(set([1, 2]))


def test_false():
	return False == 0 == bool({})


def test_None():
	return None == {}.get(1)


if __name__ == '__main__':
	print('test_numbers', test_numbers())
	print('test_string', test_string())
	print('test_list', test_list())
	print('test_list_1', test_list_1())
	print('test_dict', test_dict())
	print('test_dict_1', test_dict_1())
	print('test_dict_2', test_dict_2())
	print('test_tuple', test_tuple())
	print('test_tuple_1', test_tuple_1())
	print('test_set', test_set())
	print('test_bool', test_bool())
	print('test_false', test_false())
	print('test_None', test_None())
