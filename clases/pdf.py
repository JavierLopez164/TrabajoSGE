import jinja2
import pdfkit

class PDF():
    def __init__(self, inf):
        self.inf = inf

    def crearPDF(self, ruta_template, ruta_css, ruta_salida):
        nombre_template = ruta_template.split('/')[-1]
        ruta_template = ruta_template.replace(nombre_template, '')

        env = jinja2.Environment(loader = jinja2.FileSystemLoader(ruta_template))
        template = env.get_template(nombre_template)
        html = template.render(self.inf)

        options = {
            'page-size': 'letter',
            'margin-top': '0.05in',
            'margin-bottom': '0.05in',
            'margin-right': '0.05in',
            'margin-left': '0.05in',
            'encoding': 'UTF-8'
        }

        config = pdfkit.configuration(wkhtmltopdf = '/usr/bin/wkhtmltopdf')

        pdfkit.from_string(html, ruta_salida, css=ruta_css, options=options, configuration=config)