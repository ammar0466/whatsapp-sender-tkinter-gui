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

    payload=f"receiver={number}&message={message}"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return(response['message'])

# def sendWhapi(x, y, z):
#     url = "https://whapi.io/api/send"
    
#     payload = json.dumps({
#       "app": {
#         "id": y,
#         "time": "1646716022",
#         "data": {
#           "recipient": {
#             "id": x
#           },
#           "message": [
#             {
#               "time": "1646716022",
#               "type": "text",
#               "value": z
#             }
#           ]
#         }
#       }
#     })

#     headers = {
#       'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response.text
    # print(x)
