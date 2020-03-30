import pytest


@pytest.yield_fixture(autouse=True)
def object_like()
	yield object
	print('Done')
