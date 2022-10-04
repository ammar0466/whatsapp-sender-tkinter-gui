import requests
import json
import configparser

#get apiserver value from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
apiserver = config['server']['apiserver']


def sendWhapi2 (sender, number, message):
    # 601154285983
    url = f"http://{apiserver}/chats/send?id={sender}"

    # payload=f"receiver={number}&message={message}"
    payload = json.dumps({
        "receiver": number,
        "message": {
            "text": message
            
        }
    })
    
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return(response['message'])

def sendImg (sender, number, image):
    # 601154285983
    url = f"http://{apiserver}/chats/send?id={sender}"

    # payload=f"receiver={number}&message={message}"
    payload = json.dumps({
        "receiver": number,
        "message": {
            "image": {
                "url": image
            }
          }
    })
    
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return(response['message'])

