from flask import Flask

from app.shared.controller import root_page
from app.chat.controller import chat_page

app = Flask(__name__)

app.register_blueprint(root_page)
app.register_blueprint(chat_page)