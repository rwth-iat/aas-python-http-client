from aas_api_python_client import ApiClient, Configuration, SubmodelRepositoryAPIApi, AASXFileServerAPIApi

from aas_api_python_client.util import string_to_base64url

configuration = Configuration()
configuration.host = "SOME_HOST"


api_client = ApiClient(configuration=configuration)
submodelClient = SubmodelRepositoryAPIApi(api_client=api_client)

encoded_id = string_to_base64url("https://example.com/ids/sm/0154_9092_1122_2220")
submodel = submodelClient.get_submodel_by_id(encoded_id)
print(submodel)


aasx_ids = AASXFileServerAPIApi(api_client=api_client).get_all_aasx_package_ids()
print(aasx_ids)