# Reconciling our own postings with the corpus — and what it proves

**28 Nov 2026 · CRO for Shafira · Indonesia lane**
Tab: Core file **`postings-recon`** (62 rows, platform × month) · data: `id-postings` (17,196 individual
ads) against `data/postings-corpus/clean/monthly-platform.csv` (256 Indonesia platform-months).

---

## 1 · What we actually hold in `id-postings`

| | |
|---|---|
Rows | **17,196 individual advertisements**
Channels | **Dealls 13,115 · Karirhub 2,757** (web archive 2,337 + live 281 + archived 139) **· Kalibrr 687 · Glints 637**
Arms | boxcompute_census 14,578 · archive 2,337 · live 281
In finance/BPO scope | **1,951**
Months | **2022-03 → 2026-10** (46 months — longer than the corpus)
AI skill flagged | 198 (1.15%)
Verification | verified 281 · partly 177 · **not checked 16,738**

So we hold something the corpus does not: an individual-posting file with a longer history and a
Kemnaker-portal channel. The corpus holds something we do not: six extra channels.

## 2 · The three platforms both sides cover

| Platform | Months | Ours | Corpus | Ratio | Median | Min | Max | Comparable? |
|---|---|---|---|---|---|---|---|---|
**Dealls** | 31 | 13,112 | 15,538 | **0.84** | **0.97** | 0.30 | 1.67 | **Yes** |
Glints | 2 | 580 | 5,619 | 0.10 | 0.11 | 0.04 | 0.18 | **No** — ours is flat and thin |
Kalibrr | 29 | 677 | 3,335 | 0.20 | 0.21 | 0.08 | 0.52 | **No** — ours looks capped at ~25/month |

## 3 · Three findings

**1 · Dealls validates the method.** Two independent harvests of the same platform land within **16%** on
the 31-month total (0.84) with a **median monthly ratio of 0.97**. That is the strongest internal check in
the study after the census validation — same platform, different harvest, same shape.

**2 · And it measures the noise floor.** The same two harvests differ by **0.30 to 1.67** in individual
months. Two harvests of *the same evidence* disagree by ±50% month to month. **Any monthly claim smaller
than that is not a finding; it is harvest noise.** This is the ceiling on what S5 can ever say from
advertised demand, and it belongs next to every chart drawn from these panels.

**3 · Two of our three overlapping series are truncated, and must not be trended.** Glints: ours covers 2
months against the corpus's 31, and ours is flat — a sample, not a census. Kalibrr: ours sits at ~25 ads
every month for 29 months, which is a **page cap**, not demand. Our Karirhub channel (2,757 ads) has no
counterpart in the corpus at all, so it cannot be validated by this comparison either way.

## 4 · How the two sources fit together

| | Channels | What it gives |
|---|---|---|
Ours (`id-postings`) | Dealls, **Karirhub**, Kalibrr, Glints | Individual ads with content, skills, education, AI flags; longer history; the Kemnaker portal nobody else has |
Corpus | Dealls, Glints, **JobStreet, Indeed, Karir.com, KitaLulus, LinkedIn, Pintarnya** | Scale (1.03m ads) and exposure scores per occupation |
Both | Dealls, Glints, Kalibrr | The only place a cross-check is possible |

**They are complementary, not duplicates.** The honest statement is: combined, we cover ten Indonesian
channels; separately, neither is a census of anything.

## 5 · What this changes

- **Use Dealls for validation, never for a monthly trend on its own.** Ratio 0.84 with a ±50% monthly
  spread means the level is trustworthy and the month-to-month move is not.
- **Drop Glints and Kalibrr from any series we publish.** Keep the ads (they carry content and AI flags),
  but never a monthly count from them.
- **Karirhub stays our unique asset** — and it is the one channel where posting content, education
  requirement and AI-skill flag all exist. That is where the school-leaver finding comes from.
- **The recon tab is now the audit trail.** Anyone quoting an Indonesian postings number can see, for the
  same platform and month, what each harvest said — which is the difference between a measurement and an
  assertion.

## 6 · What would close the remaining gap

A **fill-status signal**: whether an ad was filled, and when it disappeared. Neither harvest has it, and
no Indonesian channel publishes it. Until one does, S5 can measure advertised demand to within ±50% a
month and cannot measure hiring at all — which is why the trigger ladder's Watch rung sits where it does.
