from flask import Blueprint, render_template, request, jsonify

chat_page = Blueprint(
	'chat_page', 
	__name__, 
	template_folder='templates', 
	static_folder='static',
	static_url_path='/%s/chat' % __name__
)

@chat_page.route('/chat', methods=['GET', 'POST'])
def busca_resposta():
    a = request.args.get('texto', default=None, type=None)
    return jsonify(a)