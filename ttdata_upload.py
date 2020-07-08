import sys
import requests

def upload_data(lastUpdatedDatetime, deployer, imageName, digest, tag, appkey):
    url = "http://52.170.154.169:7061/uploaddata"

    device_data = [{
    'last_updated_datetime': lastUpdatedDatetime,
    'name': imageName,
    'tag': tag,
    'deployer': deployer,
    'digest': digest,
    'key': "last_updated_datetime|name|deployer|digest"
    }]

    payload = {
    "data_type": 2,
    "device_id": imageName,
    "key": "last_updated_datetime|name|deployer|digest",
    "device_data": device_data
    }

    headers = {
        'appkey': appkey    
    }

    r = requests.post(url = url, json = payload, headers = headers)
    print(r.text.encode('utf8'))


if __name__ == "__main__":
    deployer = sys.argv[1]
    imageName = sys.argv[2]
    digest = sys.argv[3]
    lastUpdatedTime = sys.argv[5]
    tag = sys.argv[6]
    appkey = sys.argv[7]
    
    print(lastUpdatedTime)
    print(digest)
    print(tag)

    upload_data(lastUpdatedTime, deployer, imageName, digest, tag, appkey)



