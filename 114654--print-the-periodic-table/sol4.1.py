q=range
p=print
u,*x='_\\/'
W=6
H=3
I={}
def d(n,s,R,C):
 R=R*H;C=C*W
 for c in q(C+1,C+W):I[R,c]=I[R+H,c]=u
 for r in q(R+1,R+H+1):I[r,C]=I[r,C+W]='|'
 w(R+1,C+1,str(n));w(R+2,C+1,s)
def w(r,c,X):
 for x in X.center(5):I[r,c]=x;c+=1
for c in q(13,102):I[(c<73)*6+3,c]=u
D=[None]
r=c=0
for Z in'1 c=17 1 - 2 c=12 6 - 2 c=12 6 - 18 - 18 - 3 r=8 14 r=5 c=3 15 - 3 r=9 14 r=6 c=3 15'.split():
 if'-'==Z:r=r+1;c=0
 elif Z.isdigit():
  for _ in range(int(Z)):D.append((r,c));c+=1
 else:exec(Z)
E='  H HeLiBeB C N O F NeNaMgAlSiP S ClArK CaScTiV CrMnFeCoNiCuZnGaGeAsSeBrKrRbSrY ZrNbMoTcRuRhPdAgCdInSnSbTeI XeCsBaLaCePrNdPmSmEuGdTbDyHoErTmYbLuHfTaW ReOsIrPtAuHgTlPbBiPoAtRnFrRaAcThPaU NpPuAmCmBkCfEsFmMdNoLrRfDbSgBhHsMtDsRgCnNhFlMcLvTsOg'
F=[E[x*2:x*2+2] for x in range(119)]
for s,(r,c),n in[*zip(F,D,range(999))][1:]:d(n,s,r,c)
I[24,18]=u
for r,c in[(16,18),(25,18),(25,102)]:
 for i in q(6):I[r+i,c]=x[i%2]
for r in q(31):
 for c in q(109):p(I.get((r,c),' '),end='')
 p()
