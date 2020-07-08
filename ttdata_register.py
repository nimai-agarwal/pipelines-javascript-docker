import sys
import requests

def register(did):
    url = "http://52.170.154.169:7061/register"
    payload = {"device_id": did,
                "category": "saic"
              }
    response = requests.post(url=url, data = payload)
    print('Appkey:', end = " ")
    print(response.json()['data'])

if __name__ == "__main__":
    imageName = sys.argv[1]
    register(imageName)