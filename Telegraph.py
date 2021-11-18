import requests
from telegraph import Telegraph
telegraph = Telegraph()
telegraph.create_account(short_name='1337')
with open('image.jpeg', 'rb') as f:
    path = requests.post(
                    'https://telegra.ph/upload', files={'file':('file', f, 'image/jpeg')}).json()[0]['src']
response = telegraph.create_page('Hey',html_content="<img src='{}'/><p>Hello, world!</p> ".format(path),)



print('http://telegra.ph/{}'.format(response['path']))