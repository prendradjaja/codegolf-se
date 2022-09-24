q=range
u='_'
I={(24,18):u}
for c in q(13,102):I[(c<73)*6+3,c]=u
r,c,*D=0,0
for Z in'1,c=17,1,,2,c=12,6,,2,c=12,6,,18,,18,,3,r=8,14,r=5,c=3,15,,3,r=9,14,r=6,c=3,15'.split(','):
 if'1'>Z:r+=1;c=0
 elif'a'>Z:
  for _ in q(int(Z)):D.append((r,c));c+=1
 else:exec(Z)
for i in q(118):
 R,C=D[i];R*=3;C*=6
 for r in q(R+1,R+4):I[r,C]=I[r,C+6]='|'
 for r,X in(R+1,str(i+1)),(R+2,'H HeLiBeB C N O F NeNaMgAlSiP S ClArK CaScTiV CrMnFeCoNiCuZnGaGeAsSeBrKrRbSrY ZrNbMoTcRuRhPdAgCdInSnSbTeI XeCsBaLaCePrNdPmSmEuGdTbDyHoErTmYbLuHfTaW ReOsIrPtAuHgTlPbBiPoAtRnFrRaAcThPaU NpPuAmCmBkCfEsFmMdNoLrRfDbSgBhHsMtDsRgCnNhFlMcLvTsOg'[2*i:][:2]),(R,u*5),(R+3,u*5):
  c=C+1
  for z in X.center(5):I[r,c]=z;c+=1
for r,c in(16,18),(25,18),(25,102):
 for i in q(6):I[r+i,c]='\\/'[i%2]
for r in q(31):print(*(I.get((r,c),' ')for c in q(109)),sep='')
