from flask import Flask
from api_manager.server.api_router import account_api
import logging
import os


app = Flask(__name__)
app.register_blueprint(account_api)
app.logger.setLevel(logging.INFO)
if __name__ == '__main__':
    # if run on docker the DOCKER_ON is setted so it redirect the traffic to docker localhost
    if os.environ.get("DOCKER_ON") is None:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')

