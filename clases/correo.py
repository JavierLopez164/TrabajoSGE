import smtplib
from email.message import EmailMessage

class Correo():

    def __init__(self, usuario, password, destino, asunto, cuerpo):
        self.usuario = usuario
        self.password = password
        self.destino = destino
        self.asunto = asunto
        self.cuerpo = cuerpo

    def enviarEmail(self):
        email = EmailMessage()
        origen = f"{self.usuario}@educa.madrid.org"
        email["From"] = origen
        email["To"] = f"{self.destino}@educa.madrid.org"
        email["Subject"] = self.asunto
        email.set_content(self.cuerpo)

        with smtplib.SMTP("smtp01.educa.madrid.org", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(self.usuario, self.password)
            server.send_message(email)