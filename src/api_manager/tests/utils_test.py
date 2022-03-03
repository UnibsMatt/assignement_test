from unittest import TestCase
from api_manager.utilities import prettify_content, DesiredOutput
from api_manager.api_endpoints import ReqMethod, RestCountry, RestContent, CountryCommon, Country, NationalizeContent, Nationalize
from unittest.mock import MagicMock


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
        print("asd")

