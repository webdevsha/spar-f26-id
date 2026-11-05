"""Decide the AI-skill flag from the posting's own words.

Rule (per the team's request): a posting counts as AI-skill = Yes when its
'Persyaratan Khusus' (special requirements) names an AI skill or tool. When the
posting has no requirements text at all we fall back to the title/description and
say so in the evidence, rather than silently leaving it at No.

Only genuine AI terms count. Generic office/digital skills (Excel, typing) and
automation-adjacent ones (RPA, "otomasi", "big data", "predictive") are NOT AI
and are deliberately excluded -- they inflated the old flag.
"""
import re

# AI skills and tools, Indonesian and English. Word boundaries everywhere, so
# "email" or "DKI" cannot match "AI".
AI_TERMS = [
    # Indonesian
    r"kecerdasan buatan", r"kecerdasan artifisial", r"kecerdasan artifisial \(ai\)",
    r"pembelajaran mesin", r"pembelajaran mendalam", r"ilmu data", r"ilmuwan data",
    r"pengolahan bahasa alami", r"visi komputer",
    r"ai generatif", r"kecerdasan buatan generatif",
    # English / general
    r"artificial intelligence", r"a\.i\.", r"\bgen\s?ai\b", r"generative ai", r"ai generat",
    r"machine learning", r"deep learning", r"neural network", r"reinforcement learning",
    r"large language model", r"\bllms?\b", r"foundation model", r"model bahasa besar",
    r"natural language processing", r"\bnlp\b", r"computer vision", r"speech recognition",
    r"pengenalan wajah", r"face recognition", r"image recognition", r"object detection",
    r"data science", r"data scientist", r"data mining", r"text mining",
    r"chatbot", r"chat bot",
    # named tools / products
    r"chatgpt", r"openai", r"gpt-?[34o]", r"\bgemini\b", r"\bcopilot\b", r"claude",
    r"midjourney", r"stable diffusion", r"dall-?e", r"hugging ?face", r"tensorflow",
    r"pytorch", r"tensorflow\s*/\s*keras", r"scikit-?learn", r"langchain", r"ollama",
    # prompt work
    r"prompt engineering", r"prompt engineer", r"rekayasa prompt", r"penulisan prompt",
    r"prompt ai", r"prompt negatif",
    # bare AI, last: shortest and broadest
    r"\bai\b", r"\bai-?based\b", r"\bai-?powered\b", r"\bai-?driven\b",
    r"\bai tools?\b", r"\btools? ai\b",
]
AI_RE = [re.compile(p, re.I) for p in AI_TERMS]
# "AI" in a design/print ad almost always means Adobe Illustrator, not artificial
# intelligence -- unless the same text also says something unmistakably AI.
ILLUSTRATOR = re.compile(r"adobe|illustrator|photoshop|premiere|after ?effect|corel|indesign", re.I)
REAL_AI = re.compile(r"kecerdasan buatan|artificial intelligence|machine learning|chatgpt|"
                     r"generative ai|\bgen\s?ai\b|large language|pembelajaran mesin", re.I)


def _illustrator_only(text, m):
    """True when this 'AI' is Adobe Illustrator and nothing else in the text is AI."""
    if m.group(0).strip().lower() != "ai":
        return False
    if REAL_AI.search(text):
        return False
    return bool(ILLUSTRATOR.search(text))


BARE_AI = re.compile(r"\bai\b", re.I)


def find(text, strict=False):
    """Return (matched terms, snippet around the first match).

    strict=True drops the bare word "AI": in a free-text description it is as often a
    brand or a partner's name as a skill, so outside the requirements section only an
    explicit phrase (AI-driven, machine learning, ChatGPT, ...) counts.
    """
    if not text:
        return [], ""
    hits, snip = [], ""
    for rx in AI_RE:
        if strict and rx.pattern == r"\bai\b":
            continue
        m = rx.search(text)
        if m and _illustrator_only(text, m):
            m = None
        if m:
            term = m.group(0).strip().lower()
            if term not in hits:
                hits.append(term)
            if not snip:
                a, b = max(0, m.start() - 60), min(len(text), m.end() + 60)
                snip = text[a:b].replace("\n", " ").strip()
    return hits, snip


def classify(requirements, title="", desc=""):
    """-> dict(flag, tier, evidence, source)."""
    for source, text in (("requirements", requirements), ("title", title), ("content", desc)):
        hits, snip = find(text, strict=(source == "content"))
        if hits:
            ev = "%s: %s — “…%s…”" % (source, ", ".join(hits[:4]), snip[:160])
            return {"flag": "Yes", "tier": "ai_explicit", "evidence": ev, "source": source,
                    "hits": hits[:8]}
    return {"flag": "No", "tier": "none", "evidence": "", "source": "", "hits": []}
