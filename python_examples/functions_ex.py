# coding=utf-8

example_name = 'FUNCTION_EX' # глобальная переменная


def regular_func(*args, **kwargs):
	return args, kwargs


def no_return_func() -> None:
	print('Help')


def one_arg_func(name: str)-> str:
	return name


def do_smth(fn):
	count = 1 # локальная переменная
	# global example_name
	example_name == 'new'
	def wrapper(*args, **kwargs):
		# nonlocal count
		# count +=1
		print(count)
		return fn()
	return wrapper


@do_smth
def func(*args):
	print(args)
	return True


def with_connection(db):
    def wrapper(func):  # создаеться в моме выполнения функции
        def _wrapper(self, **kwargs):
            with connect_to_db(db) as e:
                return func(self, **kwargs)
        return _wrapper
    return wrapper


def change_mut_type(data):
	if data.pop(1):
		return data
	data['smth'] = 'new'
	return data


def check_args(*args):
	print(args)


def check_kwargs(*kwargs):
	print(kwargs)

def check_named_args(name='Vasya'):
	print(name)

# def check_named_args(name='Katya'):
# 	print(name)

def saver(x=[]):
	x.append(1)
	print(x)

if __name__ == '__main__':
	regular_func(*[1, 2, 3, 4], **{'cell': 'jey'})
	regular_func(1, 2, 3, 4, cell='key')

	output_data = {1: 1, 2: 2}
	change_mut_type(output_data)
	assert output_data == {2: 2}

	check_args(*[1, 2, 3, 4])
	check_args(1, 2, 3, 4)

	check_kwargs(**{'name': 'Katya'})
	check_kwargs(name='Katya')

	check_named_args() == check_named_args('Vasya')

	saver([2])  # [2, 1]
	saver([1])  # [3, 1]
	saver()  # [1, 1] 
	saver()  # [1. 1. 1] 
