// Mirror of the workbook logic (Model_* sheets, v0.2). Keep in sync with the Google Sheet.
const YEARS = 5;
function rOf(S){ return S.e*S.phi; }
function runScenario(P, S, banks) {
  const live = banks.filter(b => b.hc > 0);
  const hc0 = live.reduce((a,b)=>a+b.hc,0);
  const q = hc0 ? live.reduce((a,b)=>a+b.hc*((b.leavers>0)? b.leavers/b.hc : P.q),0)/hc0 : P.q;
  const x = hc0 ? live.reduce((a,b)=>a+b.hc*((b.exp>0)? b.exp : P.x),0)/hc0 : P.x;
  const f = P.chi*P.theta/Math.pow(1+Math.pow(P.theta,P.iota),1/P.iota);
  const r_ = rOf(S);
  const rows=[];
  for (let t=0;t<YEARS;t++){
    const yr=P.baseYear+t;
    const A = yr>=S.year ? S.A : P.A0+(S.A-P.A0)*t/(S.year-P.baseYear);
    const noai = hc0*Math.pow(1+P.g,t);
    const fac = 1 - x*r_*(A-P.A0) - S.m*Math.min(1,t/2);
    const tgt = noai*fac;
    const r={yr,t,A,noai,fac,E: t===0?hc0:tgt};
    if(t>0){
      const p=rows[t-1];
      r.dE=r.E-p.E; r.dEp=r.dE/p.E;
      r.S=q*p.E; r.D=p.E-r.E;
      r.H=Math.max(0,r.S-r.D); r.L=Math.max(0,r.D-r.S);
      r.H0=Math.max(0,q*p.noai+(r.noai-p.noai));
      r.hcut=r.H0>0?1-r.H/r.H0:0;
      r.absorbed=r.D<=0?null:Math.min(r.D,r.S)/r.D;
      r.cum=(t>1?p.cum:0)+r.L;
      r.jkp=r.L*P.acc;
      r.cost=r.jkp*Math.min(P.wage,P.cap)*P.rate*P.months/1000;
      r.ref=r.L*f; r.inf=r.L*(1-f)*P.psi; r.unemp=r.L*(1-f)*(1-P.psi);
      r.sector=r.L*(P.fi*1e6)/hc0;
    } else { r.cum=0; }
    rows.push(r);
  }
  const rest=rows.slice(1);
  return {rows,q,x,f,hc0,r:r_,
    sum:{A:rows[YEARS-1].A,E:rows[YEARS-1].E,chg:rows[YEARS-1].E/hc0-1,
      maxFall:Math.min(...rest.map(r=>r.dEp)),avgCut:rest.reduce((a,r)=>a+r.hcut,0)/rest.length,
      cum:rows[YEARS-1].cum,cost:rest.reduce((a,r)=>a+r.cost,0),inf:rest.reduce((a,r)=>a+r.inf,0),
      unemp:rest.reduce((a,r)=>a+r.unemp,0),ref:rest.reduce((a,r)=>a+r.ref,0),sector:rest.reduce((a,r)=>a+r.sector,0)}};
}
function expected(results, w){ // results: {slow,medium,extreme}; w: {slow,medium,extreme} summing to 1
  const keys=['A','E','chg','maxFall','avgCut','cum','cost','inf','unemp','ref','sector'];
  const o={}; keys.forEach(k=>o[k]=['slow','medium','extreme'].reduce((a,s)=>a+w[s]*results[s].sum[k],0)); return o;
}
if (typeof module!=='undefined') module.exports={runScenario,expected,rOf};
