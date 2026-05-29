#Muestra paginas y se conecta con base de datos
import web
#Permite saber la direccion de la pagina
urls = (
    '/', 'Index',
)
#Hace que todo funcione
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
#Ejecuta el servidor
if __name__ == "__main__":
    app.run()