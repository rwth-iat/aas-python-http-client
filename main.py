from aas_api_python_client import ApiClient, Configuration, AssetAdministrationShellRepositoryAPIApi

from aas_api_python_client.util import string_to_base64url

configuration = Configuration()
configuration.host = "http://localhost:8080/api/v3.0"

api_client = ApiClient(configuration=configuration)
aasRepoClient = AssetAdministrationShellRepositoryAPIApi(api_client=api_client)

all_aas = aasRepoClient.get_all_asset_administration_shells()
print(all_aas)
aas = aasRepoClient.get_asset_administration_shell_by_id(string_to_base64url('https://acplt.org/Test_AssetAdministrationShell'))
print(aas)
aas_info = aasRepoClient.get_asset_information_aas_repository(string_to_base64url('https://acplt.org/Test_AssetAdministrationShell'))
print(aas_info)
