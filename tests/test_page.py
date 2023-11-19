import pytest
import requests
import os
from bs4 import BeautifulSoup
from openbooksearch import page as obs_page


@pytest.fixture
def goodreads_homepage():
    if not os.path.exists("tests/test_files"):
        os.makedirs("tests/test_files")
    if not os.path.exists("tests/test_files/goodreads_homepage.txt"):
        response = requests.get("https://goodreads.com").text
        with open("tests/test_files/goodreads_homepage.txt", "w") as f:
            f.write(response)
        return response
    with open("tests/test_files/goodreads_homepage.txt") as f:
        return f.read()


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


def test_page_reads_entire_html(goodreads_homepage):
    soup = BeautifulSoup(goodreads_homepage, "html.parser")
    assert soup is not None
    assert soup.find(id='signInUsingContent') is not None
