from abc import ABC
from typing import Dict


class RestAPIException(Exception):
    pass


class EmptySearchQueryException(RestAPIException):
    def __init__(self: RestAPIException, message: str) -> RestAPIException:
        self.message = message


class MalformedQueryKeyException(RestAPIException):
    def __init__(self: RestAPIException, message: str) -> RestAPIException:
        self.message = message


class IRestAPI(ABC):
    def get_uri(self, endpoint: str) -> str:
        """
        Get the endpoint to query.

        :param endpoint: The endpoint of the query.
        :return: The complete URI to send to requests.
        """
        return self._base + endpoint


class OpenLibraryAPI(IRestAPI):

    def __init__(self: IRestAPI):
        self._base = "https://openlibrary.org/"
        self._limit = None
        self._page = None

    @property
    def limit(self: IRestAPI) -> int:
        """
        Get the limit value.
        """
        return self._limit

    @property
    def page(self: IRestAPI) -> int:
        """
        Get the page value.
        """
        return self._page

    @limit.setter
    def limit(self: IRestAPI, limit: int) -> None:
        """
        Set the limit value.

        :param limit: The limit to set on the query.
        :return: None.
        """
        self._limit = limit

    @page.setter
    def page(self: IRestAPI, page: int) -> None:
        """
        Set the page value.

        :param page: The page to return in the query.
        :return: None.
        """
        self._page = page

    def get_uri(self: IRestAPI, endpoint: str) -> str:
        if self.limit is not None:
            endpoint += f"&limit={self.limit}"
        if self.page is not None:
            endpoint += f"&page={self.page}"
        return super().get_uri(endpoint)

    def get_search_uri(self: IRestAPI, query: Dict[str, str]) -> str:
        """
        Get the URI query against the search endpoint.

        :param query: A map of search keys to search values. E.g. {"key": "first_publish_year": "2023"}
        :return: A URI with parameters formatted correctly.
        :raises EmptySearchQueryException: If either 'key' or 'value' of query is empty or missing.
        :raises MalformedQueryKeyException: If the 'key' of query is not purely alphabetic.
        """
        if OpenLibraryAPI._query_is_malformed(query, "key"):
            raise EmptySearchQueryException(
                "The query is malformed. Requires non-empty strings for 'key'.")
        if OpenLibraryAPI._query_is_malformed(query, "value"):
            raise EmptySearchQueryException(
                "The query is malformed. Requires non-empty strings for 'value'."
            )
        if OpenLibraryAPI._key_is_malformed(query["key"]):
            raise MalformedQueryKeyException(
                "The query key is malformed. Requires alphabetic characters only [a-z]."
            )
        search_endpoint = "search.json?q=" + \
            query["key"] + "%3A" + query["value"]
        return self.get_uri(search_endpoint)

    @staticmethod
    def _query_is_malformed(query: Dict[str, str], element: str) -> bool:
        """
        Checks if a given element is missing or empty in the query.

        :param query: A key:value query mapping.
        :param element: The element to check.
        :return: True if query is well-formed.
        """
        return (element not in query or query.get(element).strip() == "")

    @staticmethod
    def _key_is_malformed(key: str) -> bool:
        """
        Checks if the query key is not alphabetic.

        :param key: The key to check.
        :return: True if key is well-formed.
        """
        return (key.count(" ") > 0 or key.count("&") > 0 or key.count("*") > 0)
