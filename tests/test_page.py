import pytest
import requests  
from openbooksearch import page as obs_page


def test_create_page():
    page = obs_page.Page()
    assert page is not None, "Could not create page"

def test_page_set_set_with_html_text(requests_mock):
    url = "https://goodreads.com"
    requests_mock.get(url, text="<html>test</html>")
    response = requests.get(url)
    body = response.text
    page = obs_page.Page(body)
    assert page is not None
    assert "html" in page._body