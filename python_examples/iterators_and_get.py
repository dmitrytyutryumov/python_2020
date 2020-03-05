import sys


class IteratorEx:
    def __init__(self, *args):
        self.container = args
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_value = self.container[self._idx]
            self._idx += 1
            return next_value
        except IndexError as e:
            self._idx = 0
            raise StopIteration


class GetIter:
    """
    генератор считает значения на лету
    """
    __slots__ = ['container']

    def __init__(self, *args):
        self.container = args

    def __iter__(self):
        for i in self.container:
            yield i


def get_generator():
    name = yield 'smth'
    print(f'Hey {name}')
    yield True


if __name__ == '__main__':
    for i in IteratorEx(*[1, 2, 3, 4]):
        print(i)

    for i in GetIter(*[1, 2, 3, 4]):
        print(i)

    iters = IteratorEx(*range(1000))
    gen = GetIter(*range(1000))

    print(iters, gen)

    iters = iter(iters)
    gen = iter(gen)

    print(iters, gen)
    print(sys.getsizeof(iters), sys.getsizeof(gen))

    gen = get_generator()
    a = gen.send(None)
    gen.send('Dima')
    gen.throw(Exception)
    gen.close()
