from api_manager.api_endpoints.abstract_endpoint import ApiEndpoint
from pydantic import BaseModel
from typing import List


class Country(BaseModel):
    country_id: str
    probability: float


class NationalizeContent(BaseModel):
    name: str
    country: List[Country]

    def get_country(self):
        return self.country


class Nationalize(ApiEndpoint):
    def __init__(self):
        super(Nationalize, self).__init__("https://api.nationalize.io/?name=")

    @staticmethod
    def extract_results(dictionary: dict) -> NationalizeContent:
        return NationalizeContent(**dictionary)
