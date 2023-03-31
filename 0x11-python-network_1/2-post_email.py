#!/usr/bin/python3
'''A python script that sends post request to the passed URL
and displays the body of the response'''

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        html = response.read().decode('utf-8')
        print(html)
