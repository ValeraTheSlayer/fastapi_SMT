from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    """
    Схема электронного письма.

    :param to: Адрес электронной почты получателя
    :param subject: Тема письма
    :param message: Сообщение письма
    """
    to: EmailStr
    subject: str
    message: str
