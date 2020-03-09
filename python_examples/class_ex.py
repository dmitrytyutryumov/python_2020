# coding=utf-8

from typing import Union


class Human:
    """
    Human factory
    """

    creator = 'Big band'
    actions = ['breathe', 'eat', 'watch']  # хмм

    def __init__(
            self, name, surname, sex=None,
            **kwargs
    ) -> None:  # конструктор класса
        self._name = name  # private
        self._surname = surname
        self._sex = sex
        self._parents = []
        self.__set_properties(**kwargs)  # protected

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
        import this

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
