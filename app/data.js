// Evidence used in the narrative. Mirrors Context_ID, Moody_Scenarios and Fit_Log in the workbook.
const SRC = {
  msft:{t:"Microsoft AI Diffusion Report, Q2 2026",u:"https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/"},
  rai:{t:"report-ai.org, AI use by country 2026",u:"https://report-ai.org/indexes/geography-of-ai/ai-use-by-country-2026/"},
  aws:{t:"AWS/Strand 2025 via dhawalshah.net (secondary)",u:"https://www.dhawalshah.net/research/sea-ai-adoption-numbers/"},
  ilo:{t:"ILO, Generative AI and ASEAN labour markets",u:"https://www.ilo.org/resource/article/navigating-generative-ai%E2%80%99s-transformations-asean-labour-markets"},
  iloPdf:{t:"ILO ASEAN brief (PDF)",u:"https://www.ilo.org/sites/default/files/2026-07/ILO%20Brief%20ASEAN%20AI%20v11%20clean.pdf"},
  kompasInf:{t:"Kompas, informal work series",u:"https://www.kompas.id/artikel/en-pekerja-indonesia-bergantung-pada-pekerjaan-informal"},
  idn:{t:"IDN Research Institute, labour market 2026",u:"https://www.idnresearchinstitute.com/english/indonesia-labor-market-2026-formal-jobs-are-declining-00-vnqjp-0m6wc2"},
  bps:{t:"BPS press release, Aug 2026 labour force",u:"https://www.bps.go.id/id/pressrelease/2026/11/05/169961/tingkat-pengangguran-terbuka--tpt--sebesar-4-75-persen---rata-rata-upah-buruh-sebesar-3-42-juta-rupiah.html"},
  wiego:{t:"WIEGO, Indonesia informal workers statistics",u:"https://www.wiego.org/research-library-publications/indonesia-informal-workers-statistics-2019-2024/"},
  indef:{t:"Databoks on INDEF job-creation shares",u:"https://databoks.katadata.co.id/en/employment/statistics/6b08e8972a667/the-informal-sector-dominated-job-creation-in-indonesia-in-2026"},
  kompasYouth:{t:"Kompas, young workforce",u:"https://www.kompas.id/artikel/multi-layered-load-of-the-young-workforce"},
  kompasGrad:{t:"Kompas, unemployed graduates",u:"https://www.kompas.id/artikel/the-problem-of-unemployed-graduates-keeps-recurring"},
  fin:{t:"Databoks, workforce by sector Aug 2025",u:"https://databoks.katadata.co.id/en/employment/statistics/690c110930ed9/indonesias-business-sector-with-the-largest-workforce-august-2025"},
  gdp:{t:"Databoks, GDP by sector 2025",u:"https://databoks.katadata.co.id/en/economics-macro/statistics/69840d2a0c4dc/business-sectors-with-the-largest-gdp-in-indonesia-in-2025"},
  imf:{t:"IMF Article IV 2025",u:"https://www.imf.org/-/media/files/publications/cr/2025/english/1idnea2025003-print-pdf.pdf"},
  ksei:{t:"Databoks on KSEI investors, Sep 2026",u:"https://databoks.katadata.co.id/en/market/statistics/6ae1536a4b6e6/32-million-investors-in-the-indonesian-capital-market-as-of-september-2026-mostly-retail-investors"},
  moody:{t:"Moody's Analytics, The Macroeconomic Consequences of AI (Redux), Aug 2026",u:null},
  windfall:{t:"Windfall Trust, Scenarios 2030 (layout reference)",u:"https://scenarios-2030.windfalltrust.org/"}
};
const ADOPT = [ // Microsoft AI Diffusion: share of working-age population using AI
  {c:"Singapore",h1:58.6,q2:64.3,g:"asean"},{c:"United Kingdom",h1:36.4,q2:43.7,g:"base"},{c:"United States",h1:26.3,q2:33.0,g:"base"},
  {c:"Vietnam",h1:21.2,q2:27.9,g:"asean"},{c:"Malaysia",h1:18.3,q2:22.6,g:"asean"},{c:"Philippines",h1:17.1,q2:20.7,g:"asean"},
  {c:"Indonesia",h1:11.7,q2:14.8,g:"id"},{c:"Thailand",h1:9.1,q2:13.4,g:"asean"}
];
const BIZ = [{c:"Singapore",v:48},{c:"Thailand",v:32},{c:"Indonesia",v:28},{c:"Malaysia",v:27},{c:"Philippines",v:21},{c:"Vietnam",v:18}];
const EXPO = [{c:"Singapore",v:42.2},{c:"Philippines",v:28.1},{c:"Indonesia",v:21.7},{c:"Vietnam",v:20.8},{c:"Thailand",v:20.6}];
// BPS Sakernas, August rounds. formal and inf in million, sh = informal share in percent of employed.
const LABOUR = [
  {y:2021,formal:53.14,inf:77.91,sh:59.45},{y:2022,formal:55.06,inf:80.24,sh:59.31},{y:2023,formal:57.18,inf:82.67,sh:59.11},
  {y:2024,formal:60.81,inf:83.83,sh:57.95},{y:2025,formal:61.84,inf:84.70,sh:57.80},{y:2026,formal:62.25,inf:85.73,sh:57.93}
];
LABOUR.forEach(r=>{ r.total=r.formal+r.inf; r.derived=false; });
const MOODY = [
  {n:"AI-Empowered Economy",p:40,lo:35,hi:50,avg:41.3,map:"medium",fit:"Partly",ur:0,emp:"baseline",fin:"+2.0% (9.20m to 9.38m)",why:"Adoption path and gains plausible for banks. The baseline leans on a stock wealth effect (about two-thirds of AI's 0.52pp contribution to 2025 US growth) that is thin in Indonesia."},
  {n:"AI Falls Flat",p:25,lo:20,hi:35,avg:24.4,map:"slow",fit:"Does not fit as written",ur:2.4,emp:"-1.71m by 2030",fin:"not published",why:"US job losses come from an equity and capex bust (stocks -25%), not from adoption. In Indonesia the channel would be capital flows and the rupiah. We keep the slow-adoption part and test the bust with a separate overlay."},
  {n:"Productivity Boon",p:20,lo:10,hi:20,avg:17.5,map:"medium",fit:"Does not fit",ur:0.8,emp:"-0.26m by 2030, then positive",fin:"not published",why:"Needs tight labour markets, wage pass-through and domestic ownership of the gains. Indonesia has a labour surplus and imports frontier models."},
  {n:"Job Market Upheaval",p:10,lo:5,hi:18,avg:11.6,map:"extreme",fit:"Mechanism fits, timing does not",ur:2.2,emp:"-3.8m by 2030",fin:"-0.2% vs 2025 (-199k vs baseline)",why:"Fast substitution of cognitive tasks. With usage at 14.8% against 33.0% in the US, a 2030 arrival needs a very fast catch-up. Plausible first inside banks and BPO."},
  {n:"Job Market Dystopia",p:5,lo:3,hi:7,avg:5.3,map:"extreme",fit:"Tail only",ur:2.1,emp:"-7.1m by 2030",fin:"-6.4% vs 2025 (-769k vs baseline)",why:"Mass cognitive-labour substitution. Our Extreme case is the nearest run; not modelled separately."}
];
const PRIORS = { moody:{slow:25,medium:60,extreme:15}, indo:{slow:40,medium:50,extreme:10} };
const HYP = [
 {k:"C",t:"Unpreparedness: the economy cannot absorb displaced and new workers",score:4,
  ev:["Labour force grew 1.37m in a year; formal jobs grew 0.41m (61.84m to 62.25m), and 57% of the last two years' new jobs were informal.","Youth unemployment is 17.50%; 12.84m people are underemployed.","Unemployment insurance (JKP) covers formal workers only, and 57.9% of workers are informal."],
  test:"Falsified if bank and BPO entrants find formal jobs at rates similar to today even as hiring falls.",
  verdict:"Strongest evidence. The shock is more likely to show up as young entrants not getting formal jobs than as bank layoffs."},
 {k:"B",t:"Unplanned adoption: cost-cutting first, no job redesign or retraining",score:3,
  ev:["52% of surveyed institutions are piloting or running AI, but only 4% run it across functions with governance (ID-05, 91 respondents).","Bank headcount already falls by not replacing leavers (CIMB Niaga -3.1%, KB Bank -22.6% year on year)."],
  test:"Falsified if bank disclosures show retraining and redeployment budgets that match the headcount saved.",
  verdict:"Likely in banks, and it shapes who bears the cost (entry-level hiring), but it is not enough on its own to cause a macro shock."},
 {k:"E",t:"Distribution: gains go to foreign model owners, costs stay at home",score:2,
  ev:["Indonesia ranks 76 of 147 in AI use and imports frontier models.","Moody's US scenarios assume domestic ownership of the gains; the Windfall Trust scenarios use market structure as a second axis."],
  test:"Needs data on imported AI service spend and local data-centre investment.",
  verdict:"Plausible, not yet measured. A feed, not a finding."},
 {k:"A",t:"Speed: adoption outruns the economy's ability to adjust",score:2,
  ev:["Indonesia's usage is 14.8% (US 33.0%, UK 43.7%) and rose 3.1 points since H1 2025 against 6.7 in the US.","Extreme requires operational adoption to go from 18% to 85% in two years."],
  test:"Falsified if quarterly usage stays below about 25% by 2028 and bank pilots stay pilots.",
  verdict:"Weak through 2030 on current evidence. Speed matters for banks first, and it only needs to be fast inside a few firms."},
 {k:"D",t:"External shock: an AI-linked financial bust spills into Indonesia",score:1,
  ev:["Moody's gives Falls Flat 25%; the US downturn comes from stocks falling 25% and a capex bust.","Indonesia's domestic equity base is small (about 9m equity investor accounts), so the route is capital flows and the rupiah."],
  test:"Needs foreign portfolio flows, rupiah and bank funding data under a US equity fall.",
  verdict:"Real but unquantified for Indonesia. It is the one that could arrive without any adoption at all."}
];
const ADJ = [
 ["Scenario probabilities","US economists' subjective average: 40 / 25 / 10 / 5 / 20.","Usage 14.8% vs 33.0%; banks ahead of the economy (52% piloting or operational).","Slow 40, Medium 50, Extreme 10 as a starting prior (from 25 / 60 / 15). Editable. Replace with expert elicitation.","Low"],
 ["Wealth effect","About two-thirds of AI's 0.52pp 2025 US growth came through stock wealth.","About 9m equity investor accounts; 32m capital-market accounts, 99.8% retail.","Not carried over. Macro overlay set to 0; external channel left as a flagged gap.","Medium"],
 ["Shock measure","Unemployment rate and payrolls.","Open unemployment 4.68% (Feb 2026), 4.75% (Aug 2026); informal 57.9%; JKP formal only.","Track where displaced staff go: formal, informal, open unemployed.","Medium"],
 ["Labour supply","US labour force growth slows with immigration.","Labour force +1.37m a year vs formal jobs +0.41m (Aug 2025 to Aug 2026).","Adjustment lands on hiring of entrants; hiring cut is a headline output.","Medium"],
 ["Exposure to loss","Loss = exposure x adoption x friction, an upper bound (Box 4).","ILO: 21.7% of Indonesian jobs exposed; 24% of clerical tasks highly exposed, 58% medium.","r = e x phi. e from ILO task shares; phi is our friction residual, to be calibrated.","Low to medium"],
 ["Baseline growth","US financial activities payrolls +2.0% over 2025 to 2030.","Finance and insurance employment 1.71m (Aug 2024) to 1.65m (Aug 2025).","No baseline growth (g = 0).","Medium"],
 ["Policy response","Reaction function and stabilisers only.","JKP pays 60% of wages for up to 6 months, formal workers only.","JKP cost tracked; no new programme assumed.","Medium"],
 ["Horizon","2025 to 2035.","Evidence base anchors on 2026.","2026 to 2030 only.","Medium"]
];
// Mirrors Data_Feed in the workbook as of v0.3b: what is still missing, after the 28 Nov feed.
const FEEDS = [
 ["Headcount by function (tellers, customer service, back office)","GRI 2-7; OJK; Sakernas KBJI by KBLI K","Exposed share x — currently a flat 30% assumption"],
 ["One BRI headcount definition","BRI annual report","Panel size: BRI is 56% of the panel at bank-only 84,949"],
 ["Full ID-05 white paper (PERBANAS/IBM/K&A)","PERBANAS","Adoption anchors and the 34 / 18 / 4% split"],
 ["AI system start dates per bank","Annual reports, press","Bank-level adoption timing"],
 ["Labour-saving estimate r, calibrated","ILO index mapped to KBJI","Size of the shock in each scenario"],
 ["Sakernas transitions out of formal finance jobs","BPS SILASTIK request","Destination split; mu and theta"],
 ["Vacancies for teller, customer service, back office","Pasker ID / Karirhub; Core file","Job-finding rate f(theta)"],
 ["FED as of v0.3b: hires and leavers for all 8 banks; Mandiri, BTN, BSI headcount","GRI 401-1 in bank sustainability reports","Done — attrition is now per bank, 6.11% weighted, not the flat 3.4%"]
];
