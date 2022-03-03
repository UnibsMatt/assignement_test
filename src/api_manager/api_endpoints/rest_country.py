from api_manager.api_endpoints.abstract_endpoint import ApiEndpoint

from pydantic import BaseModel


class CountryCommon(BaseModel):
    """
    Base model with common name as string and official name as string
    """
    common: str
    official: str


class RestContent(BaseModel):
    name: CountryCommon


class RestCountry(ApiEndpoint):
    """
    Rest country class used to implements requests to restcountry
    """
    def __init__(self):
        super(RestCountry, self).__init__("https://restcountries.com/v3.1/alpha/")

    @staticmethod
    def extract_results(dictionary: dict) -> RestContent:
        """
        Extraction of Rest content from dictionary
        Args:
            dictionary: {"common": str, "official": str}

        Returns:

        """

        return RestContent(**dictionary)