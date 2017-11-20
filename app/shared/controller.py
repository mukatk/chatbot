from flask import Blueprint, render_template

root_page = Blueprint(
	'root_page', 
	__name__, 
	template_folder='templates', 
	static_folder='static',
	static_url_path='/%s/shared' % __name__
)

@root_page.route('/')
def index():
	return render_template('index.html')