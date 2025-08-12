import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificates 
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
