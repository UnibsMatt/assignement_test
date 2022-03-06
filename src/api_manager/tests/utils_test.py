from unittest import TestCase
from api_manager.utilities import prettify_content, DesiredOutput
from api_manager.api_endpoints import ReqMethod, Nationalize
from unittest.mock import MagicMock, patch
from api_manager.server.api_router import step1


class UtilitiesTest(TestCase):
    def test_pretty(self):
        out = [
            DesiredOutput(**{"name": "mattia", "probability": .99, "country_name": "italy"})
        ]
        content = prettify_content(out)
        self.assertEqual(content, "mattia is mostly certain to be from italy<br>")
        out = [
            DesiredOutput(**{"name": "mattia", "probability": .49, "country_name": "italy"})
        ]
        content = prettify_content(out)
        self.assertEqual(content, "mattia may be from italy<br>")
        out = [
            DesiredOutput(**{"name": "marco", "probability": .19, "country_name": "italy"})
        ]
        content = prettify_content(out)
        self.assertEqual(content, "It seems that marco is from italy. But I'm just guessing!<br>")

    def test_endpoint_nat_ok(self):
        nazionalize = Nationalize()
        resp = nazionalize.send_request(ReqMethod.get, "giacomo")
        self.assertEqual(resp.response.status_code, 200)
        self.assertEqual(resp.response.url, 'https://api.nationalize.io/?name=giacomo')
        resp = nazionalize.check_response(resp)
        results = nazionalize.extract_results(resp.get("content"))

        self.assertEqual(results.country[0].country_id, "SM")
        self.assertEqual(results.country[1].country_id, "IT")
        self.assertEqual(results.country[2].country_id, "")

    def test_endpoint_nat_ko(self):
        nazionalize = Nationalize()

        resp = nazionalize.send_request(ReqMethod.get, "testoneneoe")
        self.assertEqual(resp.response.status_code, 200)
        self.assertEqual(resp.response.url, 'https://api.nationalize.io/?name=testoneneoe')
        resp = nazionalize.check_response(resp)

        self.assertEqual(resp.get("status"), 200)
        results = nazionalize.extract_results(resp.get("content"))
        self.assertEqual(results.country, [])

    @patch("api_manager.api_endpoints.ApiEndpoint.check_response")
    def test_failed_connection(self, mock):
        mock.return_value = {"status": 999, "content": "Generic error"}
        out = step1("marco")
        self.assertEqual(out, "Generic error")

    @patch("api_manager.api_endpoints.ApiEndpoint.check_response")
    def test_empty_country(self, mock):
        mock.return_value = {"status": 200, "content": {"name": "marco", "country": []}}
        out = step1("marco")
        self.assertEqual(out, "Sorry no matching found for marco")

    @patch("api_manager.api_endpoints.Nationalize.check_response")
    def test_null_country(self, mock):
        mock.return_value = {
            "status": 200,
            "content": {
                "name": "marco",
                "country": [

                    {

                        "country_id": "",
                        "probability": 0.2
                    },
                    {
                        "country_id": "IT",
                        "probability": 0.2

                    }
                ]
            }
        }
        out = step1("marco")
        self.assertEqual(out, "It seems that marco is from Italy. But I\'m just guessing!<br>")
