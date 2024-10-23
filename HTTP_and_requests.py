# Requests in Python

# Requests is a Python Library that allows you to send <code>HTTP/1.1</code> requests easily. 
# We can import the library as follows:

import requests

import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
r.status_code
print(r.request.headers)
print("request body: ", r.request.body)

header = r.headers
print(r.headers)

# We can obtain the date the request was sent using the key <code>Date</code>.
header['date']

# Content-type indicates the type of data
header['Content-Type']

# You can also check the encoding
r.encoding
# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. 
# We can review the first 100 characters:
r.text[0:100]

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

# We can make a get request
r = requests.get(url)

# We can llok at the response header
print(r.headers)

# We can see the Content-Type
r.headers['Content-Type']

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. 
# First, we specify the file path and name

path=os.path.join(os.getcwd(), 'image.png')

with open(path, "wb") as f:
    f.write(r.content)
    
# We can view the image
Image.open(path)
