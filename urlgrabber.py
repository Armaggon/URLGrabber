# This is a simple python script that extracts all href links/values from the source code of a specified web page

from urllib.request import urlopen
import re
import time

url = str(input('[+] Target URL: ')) # e.g. https://linkedin.com
try:
    html_bytes = urlopen(url)
    html = html_bytes.read().decode("utf-8")
except:
    print('[!] Error - please ensure the URL is valid.')

# Using regex to grab all href links from the source code
urls = re.findall('.*?href="(https://.*?)"', html)

for url in urls:
    time.sleep(0.02)
    print(url)

save = str(input('[+] Would you like to save the results? [Y / N]: '))
if save.lower() == 'y':
    results = open('results.txt', 'w')
    for result in urls:
        results.write(result + '\n')
    results.close()
    time.sleep(1)
    print('[+] Results have been saved.')
else:
    print('[!] Exiting!')
    exit()
