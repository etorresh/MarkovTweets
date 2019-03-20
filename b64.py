import base64


def encode(string_to_encode):
    return base64.urlsafe_b64encode(string_to_encode.encode('UTF-8')).decode('ascii')


def decode(string_to_decode):
    return base64.urlsafe_b64decode(string_to_decode).decode('ascii')