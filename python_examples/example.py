from typing import Union


class Human(object):
	def __init__(name, surname, sex=None, *args, **kwargs) -> None:
		super().__init__(name, surname, *args, **kwargs)
		self._name = name
		self._surname = _surname
		self._parents = []
		self._sex = sex

	@property
	def parents(self) -> Union[Human]:
		return self._parents

	@property
	def name(self) -> str:
		return self._name

	@property	
	def is_intact_family() -> bool: 
		if len(self.parents) == 2:
			return True
		return False

	@property	
	def parent_names() -> Union[str]:
		names = []
		for parent in parents:
			names.append(parent._name)
		return names


def get_public_methods(type_):
	[print('{}.{}()'.format(type_.__name__, i)) for i in dir(type_) if not i.startswith('__')]


if __name__ == '__main__':
	pass
