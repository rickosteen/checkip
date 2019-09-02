#checkIP.py is using Python3.7 with packages bs4 & urllib3
import urllib3
from bs4 import BeautifulSoup
url = 'http://checkip.dyndns.org/'
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'), features="lxml")

print(soup.get_text())
#script by Rick Osteen rick.osteen@gmail.com
