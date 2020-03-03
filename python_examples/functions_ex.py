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


@do_smth('Hi')
def func(*args):
	print(args)
	return True


# def with_session(model, db='fatboy'):
#     def wrapper(func):
#         def _wrapper(self, **kwargs):
#             with switch_db(model, db) as e:
#                 return func(self, **kwargs)
#         return _wrapper
#     return wrapper

# model = None

# @with_session(model)
# def delete(self, **kwargs):
#     self.self._get_entity(config_id, entity)




if __name__ == '__main__':
	regular_func(*[1, 2, 3, 4], **{'cell': 'jey'})
	regular_func(1, 2, 3, 4, cell='key')
