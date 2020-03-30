import pytest


class TestWiki:
	def test_main_page(self, object_like):
		assert  1 == 1

	def test_login(self, ):
		pass

	@pytest.mark.parametrize("url,code", [
			('https://www.google.com/', 200), 
			('https://www.google.com/asdasdasdsd', 404)
	])
	def test_sites(self, url, code, requests_session):
		assert requests_session.get(url).status_code == code
