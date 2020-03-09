import traceback


class MyExceptionObject(Exception):
    pass


class MyError(MyExceptionObject):
    def __init__(self, *args):
        self.msg = 'My own error'
        super().__init__(*args)


def main():
    try:
        print('try block')
        # raise MyError
        # raise MyExceptionObject
        raise Exception('i see', 'dead people')
    except MyError as error:
        print(error.msg)
    except MyExceptionObject as obj:
        print('We found my exc obj,\n {}'.format(obj.__dict__))
        try:
            assert obj.__dict__ is None
        except (AssertionError, RuntimeError) as e:
            print('we\'ve got assert error')
            print(e)
            print(traceback.extract_stack())
    except Exception as e:
        print('General exception')
        print(e.args)
    else:
        print('else')
    finally:
        print('Logic will work always')


if __name__ == '__main__':
	main()
