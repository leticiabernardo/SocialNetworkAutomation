import base64


def clean_password(password):
    password = base64.b64decode(password)
    return str(password, 'utf-8')