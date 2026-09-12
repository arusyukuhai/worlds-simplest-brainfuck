# BrainF**k interpreter in 46 replace() rules
# ? = wildcard capture, $n = backreference

RULES=(
 ('SNp?cqr?el?m?n?ti?jo?h','SHp$1cqr$2el$3m$4n$5ti$6jo$7h'),
 ('SAp?cqr?el?m?n?ti?jo?h','SHp$1cqr$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c+r?el?mz?n?ti?jo?h','SPp$1c+r$2el$3mP$4n$5ti$6jo$7h'),
 ('SNp?c+r?el?m?n?ti?jo?h','SPp$1c+r$2el$3mP$4n$5ti$6jo$7h'),
 ('P0?n','x1$1n'),
 ('P1?n','0P$1n'),
 ('M10000000n','z00000000n'),
 ('M1?n','y0$1n'),
 ('M0?n','1M$1n'),
 ('M00000000n','11111111n'),
 ('SNp?c-r?el?mz?n?ti?jo?h','SMp$1c-r$2el$3mM$4n$5ti$6jo$7h'),
 ('SNp?c-r?el?m?n?ti?jo?h','SMp$1c-r$2el$3mM$4n$5ti$6jo$7h'),
 ('SMp?c-r?el?mz?n?ti?jo?h','SAp$1c-r$2el$3mz$4n$5ti$6jo$7h'),
 ('SNp?c>r?el?m?n?ti?jo?h','SRp$1c>r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c<r?el?m?n?ti?jo?h','SLp$1c<r$2el$3m$4n$5ti$6jo$7h'),
 ('SRp?c>r?el?m?nu?u?ti?jo?h','SAp$1c>r$2elu$4$3m$5nu$6ti$7jo$8h'),
 ('SRp?c>r?el?m?nuvti?jo?h','SAp$1c>r$2elu$4$3mz00000000nuvti$5jo$6h'),
 ('SLp?c<r?elu?u?m?n?ti?jo?h','SAp$1c<r$2elu$4m$3nu$5$6ti$7jo$8h'),
 ('SLp?c<r?eluwm?n?ti?jo?h','SAp$1c<r$2eluwmz00000000nu$3$4ti$5jo$6h'),
 ('SNp?c.r?el?m?n?ti?jo?h','SOp$1c.r$2el$3m$4n$5ti$6jo$7h'),
 ('SOp?c.r?el?m?n?ti?jo?h','SAp$1c.r$2el$3m$4n$5ti$6jou$4$7h'),
 ('SNp?c,r?el?m?n?ti?jo?h','SIp$1c,r$2el$3m$4n$5ti$6jo$7h'),
 ('SIp?c,r?el?m?n?tiu?u?jo?h','SAp$1c,r$2el$3m$6n$5tiu$7jo$8h'),
 ('SIp?c,r?el?m?n?tiujo?h','SAp$1c,r$2el$3mz00000000n$5tiujo$6h'),
 ('SNp?c[r?el?mz?n?ti?jo?h','SJp$1c[r$2el$3mz$4n$5ti$6jo$7h'),
 ('SNp?c[r?el?m?n?ti?jo?h','SAp$1c[r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c]r?el?mz?n?ti?jo?h','SAp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c]r?el?m?n?ti?jo?h','SKp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SFu?p?c[rd?d?el?m?n?ti?jo?h','SFuu$1p$2c[rd$3d$4el$5m$6n$7ti$8jo$9h'),
 ('SFup?c]r?el?m?n?ti?jo?h','SAp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SFuu?p?c]r?el?m?n?ti?jo?h','SFu$1p$2c]r$3el$4m$5n$6ti$7jo$8h'),
 ('SBu?pd?d?c]r?el?m?n?ti?jo?h','SBuu$1pd$2d$3c]r$4el$5m$6n$7ti$8jo$9h'),
 ('SBupd?d?c[r?el?m?n?ti?jo?h','SApd$1d$2c[r$3el$4m$5n$6ti$7jo$8h'),
 ('SBuu?pd?d?c[r?el?m?n?ti?jo?h','SBu$1pd$2d$3c[r$4el$5m$6n$7ti$8jo$9h'),
 ('SB?pd?d?c?r?el?m?n?ti?jo?h','SB$1pd$3c$2rd$4$5el$6m$7n$8ti$9jo$10h'),
 ('SAp?c?rd?d?el?m?n?ti?jo?h','SNpd$2$1c$3rd$4el$5m$6n$7ti$8jo$9h'),
 ('SF?p?c?rd?d?el?m?n?ti?jo?h','SF$1pd$3$2c$4rd$5el$6m$7n$8ti$9jo$10h'),
 ('SAp?c?r?el?m?n?ti?jo?h','SNp$1c$2r$3el$4m$5n$6ti$7jo$8h'),
 ('SPp?c+r?el?m?x?n?ti?jo?h','SAp$1c+r$2el$3m$4$5n$6ti$7jo$8h'),
 ('SMp?c-r?el?m?y?n?ti?jo?h','SAp$1c-r$2el$3m$4$5n$6ti$7jo$8h'),
 ('SJp?c[rd?d?el?m?n?ti?jo?h','SFupd[$1c$2rd$3el$4m$5n$6ti$7jo$8h'),
 ('SKpd?d?c]r?el?m?n?ti?jo?h','SBupd$2c$1rd]$3el$4m$5n$6ti$7jo$8h'),
 ('SPp?c+r?el?mz?n?ti?jo?h','SAp$1c+r$2el$3mz$4n$5ti$6jo$7h'),
 ('SMp?c-r?el?my?n?ti?jo?h','SAp$1c-r$2el$3m$4n$5ti$6jo$7h'),
 ('11111111Mn','y11111111n'),
 ('00000000Pn','z00000000n'),
 )


C={'0':0,'1':1,'+':43,',':44,'-':45,'.':46,'<':60,'>':62,'[':91,']':93,'S':1000,'N':1001,'A':1002,'P':1003,'M':1004,'R':1005,'L':1006,'O':1007,'I':1008,'F':1009,'B':1010,'H':1011,'J':1012,'K':1013,'x':1020,'y':1021,'p':1100,'c':1101,'r':1102,'e':1103,'d':1104,'q':1106,'l':1200,'m':1201,'n':1202,'t':1203,'u':1204,'z':1205,'v':1206,'w':1207,'i':1300,'j':1301,'o':1400,'h':1401}
OPS=set('+-<>.,[]')
def mt(s,p,i=0):
 q=p.split('?'); j=s.find(q[0],i);
 if j<0:return
 a=j; i=j+len(q[0]); c=[]
 for x in q[1:]:
  j=len(s) if not x else s.find(x,i)
  if j<0:return
  c.append(s[i:j]); i=j+len(x)
 return a,i,c
def rp(s,p,r):
 o=[];i=0
 while (m:=mt(s,p,i)):
  a,b,c=m;o.append(s[i:a]);k=0;j=0
  while j<len(r):
   if r[j]=='$':
    j+=1;k=0
    while j<len(r) and r[j].isdigit():k=k*10+int(r[j]);j+=1
    o.append(c[k-1])
   else:o.append(r[j]);j+=1
  i=max(b,a+1)
 o.append(s[i:]);t=''.join(o);return t,t!=s
def bv(b):return 'z00000000' if b==0 else ''.join(str(b>>i&1) for i in range(8))
def init(src,inp=b''):
 p=[x for x in src if x in OPS] or ['q'];s='SNpdqc'+p[0]+'r'+''.join('d'+x for x in p[1:]+['q'])+'deluwm'+bv(0)+'nuvti'
 return s+''.join('u'+bv(x) for x in inp)+'ujo'+'h'
def output_of(s):
    a,b=s.index("o")+1,s.index("h")
    z=[]; out=[]
    for x in s[a:b]+"u":
        if x=="u":
            if z and z[0]=="z": z=z[1:]
            if len(z)==8: out.append(sum(int(v)<<i for i,v in enumerate(z)))
            z=[]
        elif x in "01z": z.append(x)
    return bytes(out[::-1])

def run(src, inp=b"", limit=1_000_000, progress=100_000):
    s=init(src,inp)
    last_change=0
    for step in range(1, limit+1):
        if "H" in s:
            return output_of(s), step-1, True
        changed=False
        for pat, rep in RULES:
            s2,ch=rp(s,pat,rep)
            if ch:
                s=s2
                changed=True
        if not changed:
            return output_of(s), step, False
        if progress and step % progress == 0:
            print(f"  ... {step:,} BF steps")
    return output_of(s), limit, False

hello='++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'

print('BrainF**k interpreter — 46 replace rules')
print('Enter BF code repeatedly; type exit to quit. Empty BF = Hello World.')
print()
while True:
    try:
        src=input('BF> ')
    except (EOFError, KeyboardInterrupt):
        print()
        break
    if src.strip().lower() in {'exit','quit','q'}:
        break
    src=src.strip() or hello
    inp=input('IN> ').encode()
    try:
        out,steps,halt=run(src,inp)
        print('OUT:', out.decode('latin1'))
        print(f'[{"HALT" if halt else "TIMEOUT/STALL"}] {steps:,} BF steps')
    except Exception as e:
        print('ERR:', e)
    print()
