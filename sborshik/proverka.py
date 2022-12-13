import re

s = '<table></table>'

итог = re.findall(r'<table[^<(<table)>](.|\n)*<\/table>', s)

print(итог)