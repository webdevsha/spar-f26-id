// Does the app still reproduce the sheet's Summary? Reads the app's own BANK0/P0/SC0.
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const { runScenario } = require(path.join(root, 'app/model.js'));
const html = fs.readFileSync(path.join(root, 'app/index.html'), 'utf8');
const grab = n => eval('(' + html.match(new RegExp('const ' + n + '=(\\{[^\\n]*?\\}|\\[[^\\n]*?\\]);'))[1] + ')');
const P0 = grab('P0'), SC0 = grab('SC0'), BANK0 = grab('BANK0');
const sheet = { slow: 215844, medium: 203030, extreme: 167214 };
let bad = 0;
console.log('  panel', BANK0.reduce((a, b) => a + (+b.hc || 0), 0).toLocaleString(), '| per-bank exp', BANK0[0].exp);
for (const k of ['slow', 'medium', 'extreme']) {
  const e = Math.round(runScenario(P0, SC0[k], BANK0).sum.E);
  const d = e - sheet[k];
  if (d) bad++;
  console.log('  ' + k.padEnd(9), e.toLocaleString().padEnd(10), 'sheet', sheet[k].toLocaleString().padEnd(10), d ? 'DELTA ' + d : 'ok');
}
const ex = runScenario(P0, SC0.extreme, BANK0);
console.log('  dismissals', Math.round(ex.sum.cum), '| JKP Rp bn', ex.sum.cost.toFixed(1));
process.exit(bad ? 1 : 0);
