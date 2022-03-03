from api_manager.api_endpoints.nazionalize import NationalizeContent
from flask import Blueprint
from api_manager.api_endpoints import Nationalize, ReqMethod, RestCountry
from markupsafe import escape
import logging
from api_manager.utilities import prettify_content, DesiredOutput

account_api = Blueprint('api_routes', __name__)


@account_api.route('/<name>', methods=['GET'])
def step1(name: str):
    pretty_out = []
    nazionalize = Nationalize()
    rest_country = RestCountry()
    resp = nazionalize.send_request(ReqMethod.get, escape(name))
    out = nazionalize.check_response(resp)

    if out.get("status") != 200:
        logging.error(out.get("content"))
        return out.get("content")
    else:
        logging.info(out.get("status"))
        logging.info(out.get("content"))

        cont: NationalizeContent = nazionalize.extract_results(out.get("content"))
    if len(cont.country) == 0:
        return f"Sorry no matching found for {name}"
    for count in cont.country:
        # country id can be empty if not corrispondence is found
        if count.country_id == "" or count.country_id is None:
            continue
        response_country = rest_country.send_request(ReqMethod.get, count.country_id)
        out_country = rest_country.check_response(response_country)
        logging.info(out_country)
        # check if the response it's still different than 200 for more security
        if out_country.get("status") != 200:
            logging.warning(f"Country: {count} had -> {out_country.get('content')}")
        else:
            final = rest_country.extract_results(out_country.get("content")[0])
            # merge all the info in a known structure
            pretty_out.append(DesiredOutput(**{"name": cont.name, "probability": count.probability,"country_name": final.name.common}))
    # if no match found return a no matching string
    return prettify_content(pretty_out)


@account_api.route('/', methods=['GET'])
def home():
    return f"<h1>Welcome to the main api page" \
           "<p>This site is a prototype API for country / name probability</p>" \
           "<p>Made by Mattia Federici -> mattia.federici006@gmail.com</p>"
