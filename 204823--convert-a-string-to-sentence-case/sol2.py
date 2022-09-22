import re
f=lambda s:''.join(map(g,re.split(r'([.?!])',s)))
def g(s):
 s=s.lower();r=''
 while s:
  c,*s=s;C=c.upper()
  if C<c:
   r+=C
   break
  r+=c
 r+=''.join(s);return r
