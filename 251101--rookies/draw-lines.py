R=range
i=[['.']*71for _ in R(71)]
s=R(0,71,10)
g=R(8,71,9)
for r in R(71):
 for c in R(71):
  if r in s and c in s:i[r][c]='R'
  elif r in s or c in s:i[r][c]='*'
  if r in g or c in g:i[r][c]=' '
for x in i:print(*x,sep='')
