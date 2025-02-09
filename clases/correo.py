import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders

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

        if self.adjunto:
            with open(self.adjunto, "rb") as f:
                file_data = f.read()
                file_name = f.name
                email.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

        with smtplib.SMTP("smtp01.educa.madrid.org", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(self.usuario, self.password)
            server.send_message(email)