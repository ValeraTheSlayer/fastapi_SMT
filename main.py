from fastapi import FastAPI, HTTPException
from models import EmailSchema
from mailer import send_email
import os

app = FastAPI()

@app.post("/send_email/")
async def send_email_route(email: EmailSchema):
    if not os.environ.get('SMTP_EMAIL') or not os.environ.get('SMTP_PASSWORD'):
        raise HTTPException(status_code=500, detail="SMTP credentials are not set")

    success = send_email(email.to, email.subject, email.message)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"status": "email sent"}
