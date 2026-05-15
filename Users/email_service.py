import resend
from django.conf import settings
resend.api_key = settings.RESEND_API_KEY

# Enviamos el correo con el código de verificación
# noinspection PyTypeChecker
def enviar_verificacion(email, codigo):
    response = resend.Emails.send({
        "from": "onboarding@resend.dev",
        # En la versión gratuita de Resend solo es posible enviar al correo verificado para la demostración
        "to": 'samantha.sofia.parra.riera@estudiante.epsum.school',
        "subject": "Verifica tu cuenta en Reelyx",
        "html": f"""
            <div style="font-family: Arial; background:#151315; color:white; padding:30px; border-radius:10px;">
                <h2 style="color:#a855f7">Bienvenido a Reelyx</h2>
                <p>Tu código de verificación es:</p>
                <h1 style="color:#a855f7; letter-spacing:8px">{codigo}</h1>
                <p>Introduce este código en la app para activar tu cuenta.</p>
            </div>
        """
    })
    print("RESEND RESPONSE:", response)