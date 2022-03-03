from flask import Blueprint
from api_manager.api_endpoints import Nationalize, ReqMethod, RestCountry
from markupsafe import escape

account_api = Blueprint('api_routes', __name__)


@account_api.route('/<name>', methods=['GET'])
def step1(name: str):
    pretty_out = ""
    nazionalize = Nationalize()
    rest_country = RestCountry()
    resp = nazionalize.send_request(ReqMethod.get, escape(name))
    out = nazionalize.check_response(resp)
    if out.get("status") != 200:
        return out.get("content")
    else:
        cont = nazionalize.extract_results(out.get("content"))
    for count in cont.country:
        response_country = rest_country.send_request(ReqMethod.get, count.country_id)
        out_country = rest_country.check_response(response_country)
        if out_country.get("status") != 200:
            return out_country.get("content")
        else:
            final = rest_country.extract_results(out_country.get("content")[0])
            pretty_out += final.json()
    return pretty_out


@account_api.route('/', methods=['GET'])
def home(name):
    return f"<h1>Distant Reading Archive {name}</h1>" \
           "<p>This site is a prototype API for distant reading of science fiction novels.</p>"
