from api_manager.api_endpoints.abstract_endpoint import ApiEndpoint
from pydantic import BaseModel
from typing import List


class Country(BaseModel):
    """
    Base model with id as string and probability as float [0,1]
    """
    country_id: str
    probability: float


class NationalizeContent(BaseModel):
    name: str
    country: List[Country]

    def get_country(self) -> List[Country]:
        """
        Getter of country
        Returns: country

        """
        return self.country


class Nationalize(ApiEndpoint):
    def __init__(self):
        super(Nationalize, self).__init__("https://api.nationalize.io/?name=")

    @staticmethod
    def extract_results(dictionary: dict) -> NationalizeContent:
        """
        Extract results from the dictionary retrived from the request
        Args:
            dictionary: {"name" : str -> country : List[id , prob]}

        Returns:
            NationalizeContent instance
        """
        return NationalizeContent(**dictionary)
