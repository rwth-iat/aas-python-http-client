# Upgrade instructions
This document describes the steps to upgrade the client to a new version of the AAS API from swagger.

## Steps
The following steps are necessary to upgrade the client to a new version of the AAS API from swagger. Steps include:
- Generating client with swagger-codegen or swaggerhub
- Replacing the old client with the new one
- Adjusting the new generated client with 
  - BaSyx De-/Serialization
  - Some Naming
  - README modifications


### 1. Generate the client
- Go to [AAS Swagger API](https://app.swaggerhub.com/apis/Plattform_i40/Entire-API-Collection/)
- Click in the right top corner on Export/Client SDK/python
- Archived generated client will be downloaded

### 2. Replace the old client
- Replace the old client files with the new one from the downloaded archive

### 3. Adjust the new generated client
- Rename the package `sawgger_client` to `aas_python_http_client` 
  - PyCharm: click on package older and press `Shift+F6` to rename the package
- Adjust `README.md` if necessary
- Add `basyx-python-sdk` to the requirements.txt
- Adjust `api_client.py`
  - Look up for changes made in the generated `api_client.py` in last upgrade
  - Apply the same changes to the new generated `api_client.py`
