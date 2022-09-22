import re
def f(s):
 P=re.split(r'([.?!])',s)
 r=''
 for p in P:
  r+=g(p)
 return r
def g(s):
 s=s.lower()
 r=''
 while s:
  c,*s=s
  C=c.upper()
  if C!=c:
   r+=C
   break
  r+=c
 r+=''.join(s)
 return r
