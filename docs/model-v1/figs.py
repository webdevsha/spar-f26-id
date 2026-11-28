import json,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch,Rectangle
import numpy as np
for w in('Regular','Bold'): fm.fontManager.addfont(f'../report/fonts/Inter-{w}.otf')
INK='#1F2A2E';MUT='#5C6B70';GRID='#D9DEDF';TEAL='#01696F';TEAL2='#9CC7C9';TEAL3='#DCEBEC';AMB='#B4540A';AMB2='#F2D3B8';PALE='#F3F5F5'
plt.rcParams.update({'font.family':'Inter','svg.fonttype':'path','text.color':INK})
N=json.load(open('../../m/model_nums.json'))
def save(fig,name):
    fig.savefig(name+'.png',dpi=200,bbox_inches='tight',facecolor='white');fig.savefig(name+'.svg',bbox_inches='tight',facecolor='white');plt.close(fig)
def box(ax,x,y,w,h,fc,ec=None,lw=0.8,r=0.012):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',fc=fc,ec=ec or fc,lw=lw))
def T(ax,x,y,s,size=6.5,c=INK,w='normal',ha='left',va='center',ls=1.25):
    ax.text(x,y,s,fontsize=size,color=c,fontweight=w,ha=ha,va=va,linespacing=ls)
def arrow(ax,a,b,c=MUT,lw=1.0,style='-|>',cs='arc3'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=7,lw=lw,color=c,connectionstyle=cs,shrinkA=0,shrinkB=0))

# ---------- FIG A architecture
fig=plt.figure(figsize=(9.6,6.8));ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,100);ax.set_ylim(-4.5,66.5);ax.axis('off')
T(ax,1,64.2,'The model in one picture: from exposed work to who is protected, and whether we would see it',9.6,INK,'bold')
T(ax,1,61.6,'Four questions, six modules (M1 to M6, after the Akbar measures), three layers of scale. Figures are what the sheets hold today.',6.6,MUT)
for x,t in((1,'1  WHAT WE OBSERVE'),(37,'2  HOW THE SHOCK MOVES  (Slow 40 / Medium 50 / Extreme 10)'),(77,'3  WHAT IT TELLS US')):
    T(ax,x,57.8,t,6.3,AMB,'bold')
L=[('Economy','147.99m employed; 85.73m informal\nUnemployment 4.75%, youth 17.5%'),
   ('Sector','Finance and insurance 1.62m jobs, 4.11% of GDP\nWage Rp5.08m against Rp3.42m average'),
   ('Bank panel','8 banks, 218,129 staff (13% of sector)\n2025: 21,812 hired, 12,392 left'),
   ('Exposure','Postings index 0.582 (20,088 bank ads)\nILO: 21.7% of jobs, 93.9% of clerks'),
   ('Adoption','18% operational, 34% pilot, 4% governed\n14.8% public use, rank 76 of 147'),
   ('Protection','JKP paid 90,513 in 2025, 17% rejected\nPP 6/2025 and UU 27/2026'),
   ('Policy','24 policies, 15 actors, 73 links\nReadiness q1 to q6 drafted for 3 documents')]
y=55.6;pitch=7.35
for n,d in L:
    box(ax,1,y-6.3,33,6.6,PALE,GRID);T(ax,2,y-1.4,n,6.4,TEAL,'bold');T(ax,2,y-4.1,d,5.2,INK,ls=1.25);y-=pitch
M=[('M1','Stock','Who sits in the chairs, by layer'),
   ('M2','Driver','Adoption x task exposure, with probabilities'),
   ('M3','Hiring channel','Attrition absorbs first: hires not made'),
   ('M4','Exits and destinations','Dismissals, JKP, informal work'),
   ('M5','Protection capacity','Who is covered, who is missed'),
   ('M6','Spillover','Wage bill, JKP cost, spending, tax base')]
y=55.6;mx=38;mp=8.6
for i,(c,n,d) in enumerate(M):
    fc=TEAL if i<4 else '#7A8E92'
    box(ax,mx,y-6.3,30,6.6,'white',TEAL,1.1);box(ax,mx,y-6.3,4.2,6.6,fc,fc)
    T(ax,mx+2.1,y-3.0,c,6.6,'white','bold','center');T(ax,mx+5.4,y-2.0,n,6.6,INK,'bold');T(ax,mx+5.4,y-4.5,d,5.0,MUT)
    if i<5: arrow(ax,(mx+15,y-6.35),(mx+15,y-8.25),TEAL)
    y-=mp
arrow(ax,(34.2,32),(37.8,32),TEAL,1.4);arrow(ax,(68.2,32),(76.8,32),TEAL,1.4)
O=[('Where it lands','Hires not made, exits and\ndismissals by year and scale'),
   ('Fingerprint','What each scenario shows on\nS1 to S10, and what we can see'),
   ('Trigger test','Watch, Alert and Act thresholds\nchecked against fingerprints'),
   ('Policy fit','Each instrument tested against\nthe loud and the quiet shock')]
y=55.6
for n,d in O:
    box(ax,77,y-8.6,22,9.0,PALE,GRID);T(ax,78,y-2.2,n,6.4,AMB,'bold');T(ax,78,y-5.8,d,5.2,INK,ls=1.3);y-=11.6
box(ax,38,0.2,61,4.0,'#FBEFE3',AMB,0.8)
T(ax,39,2.2,'Feedback: observed signals re-weight the scenarios each quarter; thresholds are revised when they miss.',5.7,AMB,'bold')
T(ax,1,-1.5,'Scale layers: panel (observed)  >  sector (upper bound)  >  economy',5.4,MUT)
T(ax,1,-3.5,'M1 to M4 run today on the panel. M5 and M6 are specified; most inputs still need a feed.',5.4,MUT)
save(fig,'fig_model_architecture')

# ---------- FIG B where it lands
k=1.62e6/218129
fig,axs=plt.subplots(1,3,figsize=(9.6,3.9),sharey=True)
yrs=['2027','2028','2029','2030']
JKP=90513
for a,sc,lab in zip(axs,('Slow','Medium','Extreme'),('Slow (40%)','Medium (50%)','Extreme (10%)')):
    q=np.array(N[sc]['notmade'])*k/1000;l=np.array(N[sc]['layoffs'])*k/1000
    x=np.arange(4)
    a.bar(x,q,color=TEAL2,width=.62,label='Hires not made (quiet)');a.bar(x,l,bottom=q,color=AMB,width=.62,label='Dismissals (loud)')
    for i in range(4):
        if q[i]>12: a.text(i,q[i]/2,f'{q[i]:.0f}k',ha='center',va='center',fontsize=6.6,color=INK)
        if l[i]>6: a.text(i,q[i]+l[i]/2,f'{l[i]:.0f}k',ha='center',va='center',fontsize=6.6,color='white',fontweight='bold')
    a.axhline(JKP/1000,color=INK,lw=.9,ls=(0,(3,2)))
    a.set_xticks(x,yrs,fontsize=7);a.set_title(lab,loc='left',fontsize=8.2,fontweight='bold',color=INK)
    for s in('top','right'): a.spines[s].set_visible(False)
    a.spines['left'].set_color(GRID);a.spines['bottom'].set_color(GRID);a.tick_params(colors=MUT,labelsize=6.8)
    pk=N[sc]
    a.text(0.0,-0.2,f"Panel total 2027 to 2030: {pk['hn']:,.0f} hires not made, {pk['L']:,.0f} dismissals",transform=a.transAxes,fontsize=6.0,color=MUT)
axs[0].set_ylabel('People per year, thousand (sector scale)',fontsize=7,color=MUT)
axs[0].text(3.45,JKP/1000+4,'All JKP recipients in 2025: 90,513',ha='right',fontsize=6.4,color=INK)
axs[0].legend(frameon=False,fontsize=6.6,loc='upper left',bbox_to_anchor=(0,0.93))
fig.text(0.01,1.04,'Where the shock lands: the Medium case never touches a dismissal or a JKP claim',fontsize=9.6,fontweight='bold',ha='left')
fig.text(0.01,0.985,f'Panel results from the model, multiplied by {k:.1f} (1.62m finance and insurance jobs / 218,129 panel staff). An upper bound for banks, because the sector includes insurance and others. Stress test, not a forecast.',fontsize=6.4,color=MUT,ha='left')
fig.subplots_adjust(wspace=.08,top=.86,bottom=.2)
save(fig,'fig_where_it_lands')

# ---------- FIG C fingerprint
S=[('S1','Capability milestone',('none','none','none'),'Static: ILO 21.7%, postings 0.582','Yes'),
 ('S2','Employers\u2019 AI targets',('pilots stay pilots','workforce redesign disclosed','AI-linked cuts announced'),'5 banks name tools; no workforce target','Partly'),
 ('S3','AI adoption rate',('30% by 2030','52% by 2029','85% by 2028'),'One survey (Oct 2026), 91 respondents','Partly'),
 ('S4','Forecast or outlook',('silent','silent','silent'),'No outlook names AI','No'),
 ('S5','Hiring rate',('hires -4%','hires -31% to -35%, 2027 to 29','hires -100%, 2027 to 28'),'Annual Pasker extract; no fill status','Partly'),
 ('S6','Layoffs and closures',('0','0','7k to 8k a year (panel)'),'National PHK only; no finance cut','No'),
 ('S7','Office and branch footprint',('flat','slow decline','sharp decline'),'OJK counts; not linked to staff','Partly'),
 ('S8','Benefit claims (JKP)',('0','0','6k to 7k a year (panel)'),'National totals; 17% rejected','No'),
 ('S9','Worker destinations',('0','entrants squeezed','3k a year informal'),'Sakernas; no follow-up of leavers','No'),
 ('S10','Training demand',('flat','rising','surge'),'BCA 2,550 trained; no JKP outcomes','Partly')]
lev={'none':0,'silent':0,'0':0,'flat':0,'Slow':0}
def lv(s,col):
    t=s[2][col]
    if t in('none','silent','0','flat'):return 0
    if col==0:return 1
    if col==1:return 2 if t not in('slow decline','rising') else 2
    return 3
fig=plt.figure(figsize=(9.6,5.5));ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,100);ax.set_ylim(0,58);ax.axis('off')
T(ax,1,56,'Fingerprints: what each scenario would show, and what we can see today',9.6,INK,'bold')
T(ax,1,53.4,'Shading is movement in the model against a no-AI world. The last column is whether the indicator can be read for finance in Indonesia now.',6.5,MUT)
cx=[1,17,40,58,78];hd=['Signal','Slow','Medium','Extreme','Can we see it for finance today?']
for x,t in zip((1,31,48,65,82),('Signal','Slow','Medium','Extreme','Seen today?')):
    pass
xs=[1,22,40,58,78];wd=[20,17.5,17.5,19.5,21]
for x,t in zip(xs,['Signal','Slow  (40%)','Medium  (50%)','Extreme  (10%)','What we can read today']):
    T(ax,x+0.5,50.2,t,6.4,AMB,'bold')
y=48.2;rh=4.35
cols=['#FFFFFF',TEAL3,TEAL2,'#E7A66B']
dot={'Yes':TEAL,'Partly':'#C9A227','No':AMB}
for s in S:
    box(ax,1,y-rh+0.5,98,rh-0.4,'white',GRID,0.5,0.004)
    T(ax,1.8,y-rh/2+0.5,f'{s[0]}  {s[1]}',6.0,INK,'bold')
    for c in range(3):
        l=lv(s,c);x=xs[c+1]
        box(ax,x,y-rh+0.9,wd[c+1]-0.8,rh-1.2,cols[l],cols[l],0,0.004)
        T(ax,x+0.6,y-rh/2+0.5,s[2][c],5.5,INK if l<3 else '#2B1503',ls=1.05)
    ax.add_patch(plt.Circle((xs[4]+0.9,y-rh/2+0.5),0.75,color=dot[s[4]]))
    T(ax,xs[4]+2.4,y-rh/2+0.5,s[3],5.3,INK,ls=1.05)
    y-=rh
T(ax,1,y-1.0,'Reading: in the quiet cases (Slow, Medium) the model moves hiring (S5) but S6 and S8 stay at zero. The loud case moves S6, S8 and S9, the signals we can see least.',6.3,AMB,'bold')
T(ax,1,y-3.0,'Dots:  teal = readable for finance,  gold = partly,  rust = not readable for finance. Panel figures; sector is about 7.4 times larger (upper bound).',5.4,MUT)
save(fig,'fig_scenario_fingerprint')
