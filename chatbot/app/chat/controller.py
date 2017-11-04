from flask import Blueprint, render_template, request, jsonify
from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Robo Samuel")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train('chatterbot.corpus.english')

chat_page = Blueprint(
	'chat_page', 
	__name__, 
	template_folder='templates', 
	static_folder='static',
	static_url_path='/%s/chat' % __name__
)

@chat_page.route('/chat', methods=['GET', 'POST'])
def busca_resposta():
	a = chatterbot.get_response(request.get_json()["texto"])
	return jsonify(str(a))