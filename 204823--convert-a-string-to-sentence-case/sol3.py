import re
f=lambda s:''.join(map(lambda p:re.sub(r'[a-z]',lambda m:m[0].upper(),p.lower(),1),re.split(r'([.?!])',s)))
