#Muestra paginas y se conecta con base de datos
import web
#Permite saber la direccion de la pagina
urls = (
    '/', 'Usuarios',
)
#Hace que todo funcione
app = web.application(urls, globals())
render = web.template.render('templates')

class Usuarios:
    def GET(self):
        return render.usuarios()
#Ejecuta el servidor
if __name__ == "__main__":
    app.run()