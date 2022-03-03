from abc import ABC
from requests import Response, request, ConnectionError
from enum import Enum
import logging
from typing import NamedTuple


class ReqMethod(Enum):
    """
    Enum class for requests methods.
    """
    get = "get"
    post = "post"
    update = "update"
    delete = "delete"


class Outputs(NamedTuple):
    """
    Structure used to incapsulate the response of the request and also a description
    """
    response: Response
    description: str


class ApiEndpoint(ABC):
    """
    Abstract class used to implements basic methods that can be used to request an URL
    """

    def __init__(self, url_endpoint: str):
        """

        Args:
            url_endpoint: endpoint string used to request
        """
        self.url_endpoint = url_endpoint

    def send_request(self, request_method: ReqMethod, value: str) -> Outputs:
        """
        Methods used to send request
        Args:
            request_method: Get, post update, delete etc as enum class ReqMethod
            value: additional string methods to pass at the api

        Returns:
            Instance of Outputs class

        """
        resp = Response()
        try:
            resp = request(request_method.value, self.url_endpoint + value)
            return Outputs(resp, "")
        # check if we have connection error
        except ConnectionError as e:
            logging.warning(f"Connection error: {e}")
            return Outputs(resp, "Opsss. Seems like you have no internet connection")

    @staticmethod
    def check_response(output: Outputs) -> dict:
        """
        Check responde based on outputs
        Args:
            output:

        Returns: dict {"status" -> "content"}

        """
        # if not defined something went wrong
        if output.response.status_code is None:
            return {"status": 999, "content": output.description}
        # if status code not 200
        if output.response.status_code != 200:
            return {"status": output.response.status_code, "content": output.response}
        else:
            return {"status": output.response.status_code, "content": output.response.json()}
