from abc import ABC
from requests import Response, request, ConnectionError
from enum import Enum
import logging
from typing import NamedTuple


class ReqMethod(Enum):
    get = "get"
    post = "post"
    update = "update"
    delete = "delete"


class Outputs(NamedTuple):
    response: Response
    description: str


class ApiEndpoint(ABC):
    def __init__(self, url_endpoint: str):
        self.url_endpoint = url_endpoint

    def send_request(self, request_method: ReqMethod, value: str) -> Outputs:
        resp = Response()
        try:
            resp = request(request_method.value, self.url_endpoint + value)
            return Outputs(resp, "")

        except ConnectionError as e:
            logging.warning(f"Connection error: {e}")
            return Outputs(resp, str(e))

    @staticmethod
    def check_response(output: Outputs) -> dict:
        if output.response.status_code is None:
            return {"status": 999, "content": output.description}
        if output.response.status_code != 200:
            return {"status": output.response.status_code, "content": output.response.reason}
        else:
            return {"status": output.response.status_code, "content": output.response.json()}
