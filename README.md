# Cloud Resume Challenge

## Overview
This is the code for http://reganhw.site which I created for the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/).<br/>
Microsoft Azure was used as the cloud provider. The DB uses NoSQL and the function app is written in Python.

## Structure
- **.github/workflows**: Files for creating a CI/CD pipeline with Github Actions.
- **frontend**: HTML, CSS, Javascript files for the frontend.
- **backend**:
  - **get_visitor_count.py**: Python file to read the visitor count of the website from the command line.
  - **set_visitor_count.py**: Python file to set the visitor count of the website from the command line.
  - **api**:
    - **cosmos_db_funcs.py**: Functions for interacting with the database.
    - **function_app.py**: App that interacts with the database. 
    - **requirements.txt**: External Python libraries that need to be imported when deploying to Azure.
  - **tests**:
    - **items.py**: Functions for creating and deleting DB items for testing. 
    - **set_db_value_test.py**: Tests the set_db_value function from cosmos_db_funcs.py.
    - **increment_db_value_test.py**: Tests the get_db_value function from cosmos_db_funcs.py.

## References
- [Cloud resume challenge intro.](https://cloudresumechallenge.dev/docs/the-challenge/azure/)
- [Youtube tutorial.](https://www.youtube.com/watch?v=ieYrBWmkfno)
  - [Code from the tutorial.](https://github.com/madebygps/azure-resume)
- [HTTP triggers for Azure Functions with Python.](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook?tabs=isolated-process%2Cfunctionsv2&pivots=programming-language-python)
- [Cosmos DB input binding with Python.](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cextensionv4&pivots=programming-language-python)
- [Azure-cosmos Python library documentation.](https://pypi.org/project/azure-cosmos/4.7.0/)