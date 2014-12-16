import cherrypy, re
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('portfoliosite', 'template'))
template = env.get_template('main.html')

class PortfolioSite(object):
	@cherrypy.expose
	def index(self):
		return self.search()

	@cherrypy.expose
	def search(self):
		content = '''
			<form method="post" action="/search" class="search">
				<label for="username">Find personer efter kategori</label>
				<select name="categories" class="sameline">
					<option value="" disabled selected>Vælg kategori..</option>
					<option value="">Kategori 1</option>
				</select>
				<input type="submit" class="sameline" value="Find person" />
				<div class="clear"></div>
			</form>
		'''

		return template.render(content = content)

	@cherrypy.expose
	def login(self):
		content = '''
			<form method="post" action="/login" class="login">
				<h1>Log ind</h1>
				<label for="username">Brugernavn</label>
				<input type="text" name="username" id="username" autofocus>
				<label for="password">Kodeord</label>
				<input type="password" name="password" id="password" />
				<input type="submit" value="Log ind" />
				<div class="clear"></div>
			</form>
		'''

		return template.render(content = content)

	@cherrypy.expose
	def register(self, name=None,):
		content = '''
			<h1>Ny bruger</h1>
			Her kan du registrere en ny bruger. Hvis du allerede har en bruger kan du logge ind <a href="/login">ved at trykke her</a>.
			<form method="post" action="/register" class="register">
				<label for="name">Navn</label>
				<input type="text" id="name" name="name" autofocus required>
				<label for="mail">Email</label>
				<input type="email" id="mail" name="mail" required>
				<label for="area">By/område</label>
				<input type="text" id="area" name="area" required>
				<label for="profession">Erhverv/branche</label>
				<input type="text" id="name" name="profession" required>
				<label for="name">Stilling/uddannelse</label>
				<input type="text" id="name" name="name" required>
				<label for="name">Kodeord</label>
				<input type="text" id="name" name="name" required>
				<label for="name">Gentag kodeord</label>
				<input type="text" id="name" name="name" required>
				<input type="submit" value="Opret bruger">
				<div class="clear"></div>
			</form>
		'''

		return template.render(content = content)

	@cherrypy.expose
	def about(self):
		content = '''
			<h1>Om Portfoliosiden</h1>
			Her kan du læse om siden..
		'''

		return template.render(content = content)

	@cherrypy.expose
	def help(self):
		content = '''
			<h1>Hjælp</h1>
			Her kan du få hjælp..
		'''

		return template.render(content = content)
		
	@cherrypy.expose
	def portfolio(self, name):
		fixed_name = re.sub(r'_', ' ', name)
		content = '<h1>'
		content += fixed_name
		content += '</h1>'
		
		projects = [['Medieval warrior character design', 'Some description'],['Female character design', 'another description']]
		
		for project in projects:
			content += '''
				<a class="project" href="">
					<div class="image"></div>
					<div class="information">
						<div class="name">%s</div>
						<div class="description">%s</div>
					</div>
					<div class="clear"></div>
				</a>
			''' % (project[0], project[1])
		
		return template.render(content = content)
		

cherrypy.quickstart(PortfolioSite(), '/', '/home/xirov/sdu/interaktionsdesign/project/portfoliosite.conf')
