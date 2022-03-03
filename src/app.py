from flask import Flask
from api_manager.server.api_router import account_api

app = Flask(__name__)
app.register_blueprint(account_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
