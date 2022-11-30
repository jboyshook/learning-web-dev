import argparse
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--site", type=str, required=False, nargs=1)
args = parser.parse_args()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ssl.verify_mode = ssl.CERT_NONE

url = args.site[0]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
