from api_manager.api_endpoints.abstract_endpoint import ApiEndpoint


class Nationalize(ApiEndpoint):
    def __init__(self):
        super(Nationalize, self).__init__("http://localhost:5000/")
