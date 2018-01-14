import re

result = re.search('(?<=abc)def', 'abcdef')

print result.group(0)