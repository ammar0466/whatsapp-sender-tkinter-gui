import requests
import json

#using baileys api deploy on server
#https://github.com/ookamiiixd/baileys-api
IP_SERVER = "xx.xx.xx.xx"
PORT_SERVER ="7070"


def sendWhapi2 (sender, number, message):
    url = f"http://{IP_SERVER}:{PORT_SERVER}/chats/send?id={sender}"

    payload=f"receiver={number}&message={message}"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return(response['message'])

