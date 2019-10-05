import requests
import base64
auth = base64.b64encode(bytes("pedro--vhost-959@terrortime.app:",'utf-8')+bytes('838993', 'utf-8'))
response = requests.get(
        'https://54.91.5.130:443/oauth2/token',
        params={
            'Content-Type':'application/x-www-form-urlencoded',
            'Authorization':auth,
            'X-Server-Select':'oauth',
            })
print(response)
