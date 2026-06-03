#Muestra paginas y se conecta con base de datos
import web
#Permite saber la direccion de la pagina
urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
#Hace que todo funcione
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        titulo = "Titulo desde Python"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit fusce nibh, nascetur proin eros rutrum torquent sapien blandit mattis, augue quis neque dui nunc ullamcorper fringilla primis. Congue id fermentum felis nibh ullamcorper montes conubia nascetur facilisis quis, vel metus parturient tempus quisque hendrerit iaculis mauris vehicula odio, habitasse justo ornare auctor non risus eros ultricies aenean. Mus fusce viverra inceptos consequat hac rhoncus, nibh lacus sociosqu aliquam ultricies nulla nec, fames quam quisque euismod volutpat.Vel ultrices integer metus risus urna quis non penatibus suspendisse, pretium leo sapien ante justo in cum gravida, class a magnis euismod sodales habitant eu consequat. Euismod fringilla proin dapibus feugiat tristique vehicula aenean hendrerit montes pulvinar, dui porta inceptos faucibus cras aliquet pellentesque magna non nulla, dictumst diam ultrices neque volutpat cum iaculis per morbi. Velit mauris turpis tortor nullam sagittis semper phasellus fusce sodales, leo eleifend bibendum suscipit hac diam pellentesque dictum ullamcorper auctor, sem primis cras lobortis vulputate felis in lacus."""
        return render.parametros(titulo,descripcion)
#Ejecuta el servidor
if __name__ == "__main__":
    app.run()