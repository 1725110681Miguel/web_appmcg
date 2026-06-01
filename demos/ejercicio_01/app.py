import web
urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/usuario','Usuario',
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return (render.index())
    
class Clientes:
    def GET(self):
        return (render.clientes())
    
class Usuario:
    def GET(self):
        return (render.usuario())   
    
if __name__ == "__main__":
    app.run()