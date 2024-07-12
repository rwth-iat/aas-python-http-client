import base64

BASE64URL_ENCODING = "utf-8"


def string_to_base64url(input_string):
    encoded = base64.urlsafe_b64encode(input_string.encode(BASE64URL_ENCODING)).decode("ascii")
    return encoded
