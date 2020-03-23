# coding=utf-8
import abc
from typing import Union


class Human:
    """
    Human factory
    """

    creator = 'Big band'
    actions = ['breathe', 'eat', 'watch']  # хмм

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(
            self, name, surname, sex=None, **kwargs
    ) -> None:  # конструктор класса
        self._name = name  # private
        self._surname = surname
        self._sex = sex
        self._parents = []
        self.__set_properties(**kwargs)  # protected

    def __call__(self, *args, **kwargs):
        print('do smth')
        return True

    def __getitem__(self, item):
        print('__getitem__ {}'.format(item))
        return self.__dict__.get(item)

    def __setattr__(self, key, value):
        print('__setattr__ {} + {}'.format(key, value))
        return super(Human, self).__setattr__(key, value)

    def __getattribute__(self, item):
        print('__getattribute__ {}'.format(item))
        return super(Human, self).__getattribute__(item)

    def __del__(self):
        print('__del__{}'.format(str(self)))
        del self

    def __str__(self):
        return self.name

    @property
    def parents(self):  # public
        return self._parents

    @property
    def name(self) -> str:  # динамическое свойство
        return self._name

    @property
    def is_intact_family(self) -> bool:  # публичный метод класса
        return self._is_intact_family()

    def _is_intact_family(self) -> bool:  # приватный метод класса
        if len(self.parents) == 2:
            return True
        return False

    @property
    def parent_names(self) -> Union[str]:
        names = []
        for parent in self.parents:
            names.append(parent._name)
        return names

    def __set_properties(self, **kwargs):  # why???? 
        for name, value in kwargs.items():
            name = name.strip().strip('_')
            existed_property = self.__dict__.get(name)
            if not existed_property:
                setattr(self, f'_{name}', value)

    def _surname(self):
        return self._surname

    @staticmethod
    def tell_me_the_story():
        pass

    @classmethod
    def tell_me_the_story_about_people(cls):
        print('We are all humans')
        print(cls.creator)
        return cls


class AI:
    @property
    def name(self):
        return 'AI'

    @property
    def parents(self):
        print('You\'re gonna die for this joke')
        return None


class Robot(AI, Human):
    pass


class Terminator:
    __slots__ = ['_name']

    def __init__(self, _name):
        self._name = _name


class Terminator2:
    def __init__(self, _name):
        self._name = _name


class AbsClass(abc.ABC):

    @abc.abstractmethod
    def do_smth(self):
        pass


class MyAbc:
    def do_smth(self):
        raise NotImplemented('implement')


if __name__ == '__main__':
    dad = Human('D', 'Tyutryumov', 'm')
    mom = Human('M', 'Tyutryumova', 'f')
    me = Human('Dmitry', 'Tyutryumov', 'm', parents=[dad, mom])

    print(me.parents)
    print(me.parent_names)

    print(id(dad))
    print(id(mom))
    print(id(me))

    print(Human.__dict__, end='\n\n')
    print(me.__dict__, end='\n\n')

    print(dir(Human), end='\n\n')
    print(dir(me), end='\n\n')

    me.creator = '+'.join(me.parent_names)
    print(me.creator)
    print(Human.creator)

    me.actions.append('coding')
    print(me.actions)
    print(Human.actions)

    print(me._surname)
    print(Human._surname)

    Human.tell_me_the_story()
    Human.tell_me_the_story_about_people()

    robot = Robot('Electronic', 'AI', None, parents=[me])
    print(robot.name)
    print(robot.parents)
    print(robot.__class__.__mro__)

    setattr(robot, 'model', 'ai')
    print(robot.model)
    print(getattr(robot, 'model', None))
    print(hasattr(robot, 'model'))
    print(robot['model'])

    terminator = Terminator('T')
    print(terminator._name)

    terminator2 = Terminator2('T')
    print(terminator2._name)

    assert sys.getsizeof(terminator) == 48
    assert sys.getsizeof(terminator2) == 56

    print(me.__doc__)
    print(me.__class__)
    print(me.__dict__)
    print(me.__sizeof__())
    print(me.__class__.__mro__)

    AbsClass().do_smth()
    MyAbc().do_smth()
