from api_manager.api_endpoints.abstract_endpoint import ApiEndpoint

from pydantic import BaseModel


class CountryCommon(BaseModel):
    common: str
    official: str


class RestContent(BaseModel):
    name: CountryCommon


class RestCountry(ApiEndpoint):
    def __init__(self):
        super(RestCountry, self).__init__("https://restcountries.com/v3.1/alpha/")

    @staticmethod
    def extract_results(dictionary: dict) -> RestContent:
        return RestContent(**dictionary)