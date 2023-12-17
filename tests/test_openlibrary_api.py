import pytest
from openbooksearch import openlibrary_api as olapi


def test_uri_is_made_correctly():
    expected = "https://openlibrary.org/search.json?author=OL9145806A"
    ol_api = olapi.OpenLibraryAPI()
    actual = ol_api.get_uri(endpoint="search.json?author=OL9145806A")
    assert expected == actual


def test_search_is_run_with_parameters():
    ol_api = olapi.OpenLibraryAPI()
    query = {
        "key": "first_publish_year",
        "value": "2023"
    }
    actual = ol_api.get_search_uri(query)
    expected = "https://openlibrary.org/search.json?q=first_publish_year%3A2023"
    assert expected == actual


def test_set_limit_adds_limit_to_uri():
    ol_api = olapi.OpenLibraryAPI()
    ol_api.limit = 100
    query = {
        "key": "first_publish_year",
        "value": "2023"
    }
    actual = ol_api.get_search_uri(query)
    expected = "https://openlibrary.org/search.json?q=first_publish_year%3A2023&limit=100"
    assert expected == actual


def test_set_page_adds_page_to_uri():
    ol_api = olapi.OpenLibraryAPI()
    ol_api.page = 2
    query = {
        "key": "first_publish_year",
        "value": "2023"
    }
    actual = ol_api.get_search_uri(query)
    expected = "https://openlibrary.org/search.json?q=first_publish_year%3A2023&page=2"
    assert expected == actual


def test_no_query_value_raises_error():
    ol_api = olapi.OpenLibraryAPI()
    query = {
        "key": "a key",
        "value": ""
    }
    with pytest.raises(olapi.EmptySearchQueryException):
        ol_api.get_search_uri(query)


def test_no_query_key_raises_error():
    ol_api = olapi.OpenLibraryAPI()
    query = {
        "key": "",
        "value": "a value"
    }
    with pytest.raises(olapi.EmptySearchQueryException):
        ol_api.get_search_uri(query)


def test_malformed_query_key_raises_error():
    ol_api = olapi.OpenLibraryAPI()
    query = {
        "key": "bad key",
        "value": "ex"
    }
    with pytest.raises(olapi.MalformedQueryKeyException):
        ol_api.get_search_uri(query)


def test_malformed_query_special_chars_key_raises_error():
    ol_api = olapi.OpenLibraryAPI()
    query = {
        "key": "bad%key&",
        "value": "ex"
    }
    with pytest.raises(olapi.MalformedQueryKeyException):
        ol_api.get_search_uri(query)
