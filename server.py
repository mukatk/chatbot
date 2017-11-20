from flask import Flask
from app.shared.controller import root_page
from app.chat.controller import chat_page
import os

app = Flask(__name__)

app.register_blueprint(root_page)
app.register_blueprint(chat_page)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)