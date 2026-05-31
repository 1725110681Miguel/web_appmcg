#Muestra paginas y se conecta con base de datos
import web
#Permite saber la direccion de la pagina
urls = (
    '/', 'Clientes',
)
#Hace que todo funcione
app = web.application(urls, globals())
render = web.template.render('templates')

class Clientes:
    def GET(self):
        return render.clientes()
#Ejecuta el servidor
if __name__ == "__main__":
    app.run()