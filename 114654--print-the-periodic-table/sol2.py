q=range
p=print
u='_'
W=6
H=3
I={}
def z(r,c):
 x='\\/'
 for i in q(6):I[r+i,c]=x[i%2]
def d(n,s,R,C):
 R=R*H;C=C*W
 for c in q(C+1,C+W):I[R,c]=u;I[R+H,c]=u
 for r in q(R+1,R+H+1):I[r,C]='|';I[r,C+W]='|'
 w(R+1,C+1,str(n));w(R+2,C+1,s)
def w(r,c,X):
 for x in X.center(5):I[r,c]=x;c+=1
import lzma,base64
exec(lzma.decompress(base64.b85decode(b'{Wp48S^xk9=GL@E0stWa761SMbT8$j;0GT930(j(3IZbB=zbSC1FF)$GW|_p?2sH*ve8Ik3sIMUTof`Z&S=kAy|yUUn+Agq`&k(z`=s9<;3}{bPf^zPF`GT*dE&{=Ug`(iq$Cjd{f+5))$D!}*Sj7qJ_?X|&L|sD`m^Gyv*}qOHBnOK#GV?7aC%~twGs6dgN5SgP_`eI<!JG1d6ka60_%phb&mwe5tca9J5T39hqZ|Y*rXp34AyRtx*S0!fb_A~VQIXlSXwANxq_ql5u}6s-6);}ycnbyc**)qfO3$&63|X{nhZR!+wmWtF(4umAMHHoPFhUQGM7@mOwTu4N^{H$#_1I`;7p3y8+D?G$3PLL!(f{^xjw+W`^48MCXqK~8`@>LR!2F`Ki>7^$w<tGZ`N18!AMSkJ#_j3GdP+=QZGvF6SGE1S4*O7F^mech`ZymlUTDrLPIRS!9>B=j<CSNR3hZ7nPxQ?@2?<Z(!jxpj!QxD!*rGGpBhyus`LXoif7}>qQK7DRTV!P9fq|IKYPzzHPD;y9rhf4Khf}PAKrGb$NN5dB1od7$Xs!Jv!fM5Z;}VgwkhW!*0?73XOl>*LUjG70E8s)YcGf`5^j=ekKcqT(+>!zWJmw|Nz|lu=W|J3i0*%9P6-P(d%))%`f|GotGP5E{No{lm)Mbm=mM$czrk>3h92vrI?CMu00000ruLHlE`+I800E^0pbh{4PsZ^$vBYQl0ssI200dcD')).decode())
for c in q(73,102):I[3,c]=u
for c in q(13,72):I[9,c]=u
I[24,18]=u
z(16,18)
z(25,18)
z(25,102)
for r in q(31):
 for c in q(109):p(I.get((r,c),' '),end='')
 p()
