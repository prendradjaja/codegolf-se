R=range(8)
def m(r,c):
 z=[['.']*8for _ in R]
 for i in R:z[r][i]='*';z[i][c]='*';z[r][c]='R'
 return[''.join(row)for row in z]
for r in R:
 for rows in zip(*[m(r,c)for c in R]):print(*rows,sep=' ')
 print()
