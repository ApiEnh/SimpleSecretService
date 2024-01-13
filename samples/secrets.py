#pip requests # requests may need to be installed

# secrets module, main function is getSecret()
#
#   Usage:
#
#       openai.api_key = getSecret('myOpenApiKey')   # myOpenApiKey previously stored in service
#
#   Parameters:
#     name = name of secret to fetch
#     username = secret service username, if not specified this function will prompt
#     password = secret service password, if not specified this function will prompt
#     cacheSession = store session ID in OS env variable for this process. 
#
#   Security Note: caching session is less secure as other programs could potentially access it, 
#        but avoids prompts and MFA across program execution
#


# 
#   get a session based on user password
#

def getSecretsSession(user, password):
    import requests

    # Define the API URL and query parameters
    api_url = "https://TLD/api/"
    query_params = {
        "username": username,
        "password": password,
    }

    # Make the GET request
    response = requests.get(api_url, params=query_params)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print("Response Text:", response.text)
        return None

 
    session = response.text()
    print("Response Data:", session)

    return session

#
# get secret using session
#

def getSecret(session, name):
    import requests

    # Define the API URL and query parameters
    api_url = "https://example.com/api/endpoint"
    query_params = {
        "param1": "value1",
        "param2": "value2",
    }

    # Make the GET request
    response = requests.get(api_url, params=query_params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data (assuming it's JSON)
        data = response.json()
        print("Response Data:", data)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print("Response Text:", response.text)

    return

# getSecret function
#
#   Parameters:
#     name = name of secret to fetch
#     username = secret service username, if not specified this function will prompt
#     password = secret service password, if not specified this function will prompt
#     cacheSession = store session ID in OS env variable for this process. 
#
#   Security Note: caching session is less secure as other programs could potentially access it, 
#        but avoids prompts and MFA across program execution
#
#   Usage:
#
#       openai.api_key = getSecret('myOpenApiKey')   # myOpenApiKey previously stored in service

def getSecret(name, user=None, password=None, cacheSession=True):
    import os

    session=None
    secret =None

    # if session cache enabled, check if stored
    if cacheSession:
        session = os.environ.get("secretsStoreSession")
    
    # get session
    if session is None:

        # prompt for data if needed
        if user is None:
            message = input("Secrets username : ")

        if password is None:
            message = input("Secrets password : ")

        session = getSecretsSession(user, password)

    # get secret
    secret = getSecret(session, name)

    # cache session if enabled
    if cacheSession:
        os.environ["secretsStoreSession"] = cacheSession

    return secret

