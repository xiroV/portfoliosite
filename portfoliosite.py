import cherrypy
import os
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('portfoliosite', 'template'))
template = env.get_template('main.html')

class PortfolioSite(object):
	@cherrypy.expose
	def index(self):
		content = '''
			Din mor
		'''
		return template.render(content = content)
		
	@cherrypy.expose
	def search(self):
		content = '''
			<form method="post" action="/search" class="search">
				<label for="username">Find personer efter kategori</label>
				<select name="categories">
					<option value="" disabled selected>Vælg kategori..</option>
					<option value="">Kategori 1</option>
				</select>
				<input type="submit" value="Find person" />
				<div class="clear"></div>
			</form>
		'''
		
		return template.render(content = content)
        
	@cherrypy.expose
	def login(self):
		content = '''
			<form method="post" action="/login" class="login">
				<label for="username">Brugernavn</label>
				<input type="text" name="username" id="username" />
				<label for="password">Kodeord</label>
				<input type="password" name="password" id="password" />
				<input type="submit" value="Log ind" />
				<div class="clear"></div>
			</form>
		'''
		
		return template.render(content = content)

cherrypy.quickstart(PortfolioSite(), '/', '/home/xirov/sdu/interaktionsdesign/project/portfoliosite.conf')
