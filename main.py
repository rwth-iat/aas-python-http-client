from swagger_client import ApiClient, Configuration, SubmodelAPIApi, SubmodelRepositoryAPIApi, AASXFileServerAPIApi
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

configuration = Configuration()
configuration.host = "SOME_HOST"


api_client = ApiClient(configuration=configuration)
submodelClient = SubmodelRepositoryAPIApi(api_client=api_client)

encoded_id = string_to_base64url("https://example.com/ids/sm/0154_9092_1122_2220")
submodel = submodelClient.get_submodel_by_id(encoded_id)
print(submodel)


aasx_ids = AASXFileServerAPIApi(api_client=api_client).get_all_aasx_package_ids()
print(aasx_ids)