from flask import Flask

from app.shared.controller import root_page

app = Flask(__name__)

app.register_blueprint(root_page)