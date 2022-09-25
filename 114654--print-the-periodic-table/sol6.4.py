q=range
u='_'
I={(24,18):u}
for c in q(102):I[(c<73)*6+3,c]=u
r,c,*D=0,0
for Z in('1,c=17,1,,'+'2,c=12,6,,'*2+'18,,'*2+'3,r=%d,14,r=%d,c=3,15,,'*2%(8,5,9,6)).split(','):
 if'1'>Z:r+=1;c=0
 elif'a'>Z:
  for _ in q(int(Z)):D+=[(r,c)];c+=1
 else:exec(Z)
for i in q(118):
 R,C=D[i];R*=3;C*=6
 for r in q(R+1,R+4):I[r,C]=I[r,C+6]='|'
 for r,X in(1,str(i+1)),(2,'H HeLiBeB C N O F NeNaMgAlSiP S ClArK CaScTiV CrMnFeCoNiCuZnGaGeAsSeBrKrRbSrY ZrNbMoTcRuRhPdAgCdInSnSbTeI XeCsBaLaCePrNdPmSmEuGdTbDyHoErTmYbLuHfTaW ReOsIrPtAuHgTlPbBiPoAtRnFrRaAcThPaU NpPuAmCmBkCfEsFmMdNoLrRfDbSgBhHsMtDsRgCnNhFlMcLvTsOg'[2*i:][:2]),(0,u*5),(3,u*5):
  c=C+1
  for z in X.center(5):I[R+r,c]=z;c+=1
for r,c in(16,18),(25,18),(25,102):
 for i in q(6):I[r+i,c]='\\/'[i%2]
for r in q(31):print(*(I.get((r,c),' ')for c in q(109)),sep='')
