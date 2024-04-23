import base64


def string_to_base64url(input_string):
    # Ensure the input is in string format and encode to bytes
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    bytes_string = input_string.encode('utf-8')

    # Encode these bytes to Base64
    base64_bytes = base64.b64encode(bytes_string)

    # Convert the Base64 bytes back to string
    base64_string = base64_bytes.decode('utf-8')

    # Replace characters and remove padding for Base64URL
    base64url_string = base64_string.replace('+', '-').replace('/', '_').rstrip('=')

    return base64url_string
