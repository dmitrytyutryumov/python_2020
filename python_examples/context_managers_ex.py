import contextlib


class ContextManager(object):
    def __init__(self):
        print('Im class like ContextManager')

    def __enter__(self):
        print('Hi, how are you?')
        return self

    def __exit__(self, type, value, traceback):
        print('Thank you for coming, bye')
        if traceback:
            print('I see exception')
            return False
        return True

    def get_info(self):
        print(self.__class__.__name__)


def release_resource(*args, **kwargs):
    print('bye from def ct')
    return True


def acquire_resource(*args, **kwds):
    print('Hi im def ct')
    return True


@contextlib.contextmanager
def managed_resource(*args, **kwds):
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)


if __name__ == '__main__':
    with ContextManager() as ct:
        print(dir(ct))
        ct.get_info()
        # raise Exception

    with managed_resource() as ct:
        print(dir(ct))
        # raise Exception
