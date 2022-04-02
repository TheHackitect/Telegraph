import requests
from telegraph import Telegraph
telegraph = Telegraph()
telegraph.create_account(short_name='1337')
image = open('img.jpg', 'rb')
video = open('vid.mp4', 'rb')
src = requests.post('https://telegra.ph/upload', files={'file1':('image', image, 'image/jpeg')}).json() # A list containnig dict(s)
img_src = src[0]["src"]
response = telegraph.create_page('FutariansBot',html_content=f"Welcome!<br><img src={img_src}>")
print((response))

# 
"""

response = telegraph.create_page('Thehackitect',html_content="".format(path))
url = 'https://telegra.ph/upload'
payload = files
headers = {}
response = requests.request("POST", url, headers=headers, data=payload)
# reponse
# {'path': 'Hey-03-23-28', 'url': 'https://telegra.ph/Hey-03-23-28', 'title': 'Hey', 'description': '', 'views': 0, 'can_edit': True}
print(response["url"])
print('http://telegra.ph/{}'.format(response['path']))
"""


memo = """line 1
line 2

line 3"""

out = '<br>'.join(memo.splitlines())
print(out)