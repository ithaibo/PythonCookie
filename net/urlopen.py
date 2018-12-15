from urllib.request import urlopen
# import re

with urlopen('https://docs.python.org/3/') as response:
    for line in response:
        line = line.decode('utf-8')
        print(line)