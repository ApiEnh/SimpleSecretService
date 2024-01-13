
#pip install openai # need to install open openai module

import openai
from secrets import getSecret

#openai.api_key = 'sk-kS_NOT_A_WORKING_KEY_DONT_STORE_THEM_IN_CODE_tWumnk'
open.api_key = getSecret('OpenApiKey')

# 16k tokens
openaiModel = 'gpt-3.5-turbo-16k-0613'
apiTimeout = 60 

# messages is conversation thread 
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

# get OpenAPI reply for request
def getReply(messages, request):
    
    messages.append(
            {"role": "user", "content": request},
        )

    chat = openai.ChatCompletion.create(
        model=openaiModel, 
        messages=messages,
        request_timeout=apiTimeout
    )
    reply = chat.choices[0].message.content

    # keep conversation history
    messages.append({"role": "assistant", "content": reply})

    return messages, reply

# main
# interactive usage code example

while True:
    message = input("User : ")
    if message:
        messages, reply = getReply(messages, message)
    print(f"ChatGPT: {reply}")
