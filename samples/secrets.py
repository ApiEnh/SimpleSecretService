#pip requests # requests may need to be installed
#import pdb

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
#     cacheSession = store session ID in OS env variable for this process. default=true
#
#   Security Note: caching session is less secure as other programs could potentially access it, 
#        but avoids repeated credentials prompts
#


# 
#   get a session based on user password
#

def getSecretSession(user, password):
    import requests

    # Define the API URL and query parameters
    api_url = "https://api.simplesecretservice.com/session"
    query_params = {
        "user": user,
        "password": password,
    }

    # Make the GET request
    response = requests.get(api_url, params=query_params)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Session request failed status code: {response.status_code}")
        print("Bad user or password likely")
        return None
 
    sessionBytes = response.content
    session = sessionBytes.decode("utf-8")

    #print("Session:", session)
    return session

#
# get secret using session
#

def getSecretWithSession(session, name):
    import requests
    secret = ""

    # Define the API URL and query parameters
    api_url = "https://api.simplesecretservice.com/value"
    query_params = {
        "session": session,
        "key": name,
    }

    # Make the GET request
    response = requests.get(api_url, params=query_params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        secretBytes = response.content
        secret = secretBytes.decode("utf-8")
        #print(secret)
    else:
        print(f"Value lookup failed with status code: {response.status_code}")
        print("Probably invalid key name")

    return secret

#
# main export getSecret function
#

import json
def getSecret(name, user=None, password=None, cacheSession=True):
    import os

    sessionEnv = "secretServiceSession"
    sessionSettingsFile = "secretServiceSettings.json"
    session=None
    secret=None

    # if session cache enabled, check if stored
    if cacheSession:
        
        try:
            with open(sessionSettingsFile, 'r') as f:
                settings = json.load(f)
            session=settings.get('session')
        except FileNotFoundError:
            print("Settings file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from settings file.")
        #session = os.environ.get(sessionEnv) # these don't persist
    
    # get session
    if session is None:

        # prompt for data if needed
        if user is None:
            user = input("Secrets username : ")

        if password is None:
            password = input("Secrets password : ")

        # get secret
        session = getSecretSession(user, password)
    
    if cacheSession:
        if session:

            settings = {}
            settings["session"] = session
            try:
                with open(sessionSettingsFile, 'w') as f:
                    json.dump(settings, f)
            except IOError:
                print("An error occurred while writing to the settings file.")
            # cache session if enabled
            # os.environ[sessionEnv] = session # these don't persist

    if session:
        secret = getSecretWithSession(session, name)

    return secret

