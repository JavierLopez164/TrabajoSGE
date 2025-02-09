import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
import os

class Correo():

    def __init__(self, usuario, password, destino, asunto, cuerpo, adjunto):
        self.usuario = usuario
        self.password = password
        self.destino = destino
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.adjunto = adjunto

    def enviarEmail(self):
        email = EmailMessage()
        email["From"] = f"{self.usuario}@educa.madrid.org"
        email["To"] = f"{self.destino}@educa.madrid.org"
        email["Subject"] = self.asunto
        email.set_content(self.cuerpo)

        with open(self.adjunto, 'rb') as archivo:
            data = archivo.read()
            name = os.path.basename(self.adjunto)
            email.add_attachment(data, maintype = "file", subtype = "pdf", filename = name)

        with smtplib.SMTP("smtp01.educa.madrid.org", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(self.usuario, self.password)
            server.send_message(email)