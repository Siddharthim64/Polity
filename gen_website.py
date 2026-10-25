"""Build a multi-section UPPCS Polity test website from the master question bank.

Reads UPPCS_2026_Polity_Question_Bank.json and the single-file
uppcs_polity_test.html, then produces:

  index.html        - landing page listing every section
  all.html          - full-length test across all sections
  assets/style.css  - shared stylesheet (extracted from the single file)
  assets/quiz.js    - shared quiz logic (extracted, question bank removed)
  sections/<NN>-<slug>.html  - one page per section, holding only that
                                section's questions as an inline const Q

Each section page works standalone (opened as a file or served over HTTP)
because its questions are embedded inline and it links the shared assets.

Handles all question types: mcq_single, mcq_multi, assertion_reason, matching.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BANK_PATH = ROOT / "UPPCS_2026_Polity_Question_Bank.json"
SINGLE_HTML = ROOT / "uppcs_polity_test.html"

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

# Standard Assertion-Reason options (A-E), bilingual.
AR_OPTIONS = [
    {"en": "Both A and R are true and R is the correct explanation of A",
     "hi": "A और R दोनों सत्य हैं और R, A की सही व्याख्या है"},
    {"en": "Both A and R are true but R is NOT the correct explanation of A",
     "hi": "A और R दोनों सत्य हैं परंतु R, A की सही व्याख्या नहीं है"},
    {"en": "A is true but R is false",
     "hi": "A सत्य है परंतु R असत्य है"},
    {"en": "A is false but R is true",
     "hi": "A असत्य है परंतु R सत्य है"},
    {"en": "Both A and R are false",
     "hi": "A और R दोनों असत्य हैं"},
]


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def load_bank():
    with open(BANK_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data["questions"], data.get("total_questions", len(data["questions"]))


def extract_assets(html_text):
    css_match = re.search(r"<style>(.*?)</style>", html_text, re.S)
    js_match = re.search(r"<script>(.*?)</script>", html_text, re.S)
    css = css_match.group(1).strip() if css_match else ""
    js = js_match.group(1).strip() if js_match else ""

    # Remove the embedded question bank from the shared JS; each section page
    # defines its own const Q = [...] before loading quiz.js.
    start_marker = "/* ============ QUESTION BANK ============ */"
    end_marker = "/* ============ STATE ============ */"
    if start_marker in js and end_marker in js:
        start = js.index(start_marker)
        end = js.index(end_marker)
        js = (
            js[:start]
            + "/* Question bank (const Q) is defined per-section in each HTML page. */\n\n"
            + js[end:]
        ).strip()
    return css, js


def section_questions(questions):
    grouped = {}
    order = []
    for q in questions:
        sec = q["chapter"]
        if sec not in grouped:
            grouped[sec] = []
            order.append(sec)
        grouped[sec].append(q)
    return grouped, order


def option_to_html(opt):
    return {"en": opt["en"], "hi": opt["hi"]}


def question_to_html_obj(q):
    qtype = q.get("type", "mcq_single")
    obj = {
        "id": q["id"],
        "section": q["chapter"],
        "sub": q["subtopic"],
        "type": qtype,
        "qEn": q["question_en"],
        "qHi": q["question_hi"],
        "cEn": q.get("correct_en", ""),
        "cHi": q.get("correct_hi", ""),
        "eEn": q.get("explanation_en", ""),
        "eHi": q.get("explanation_hi", ""),
        "ref": q.get("reference", ""),
    }

    if qtype == "mcq_single":
        obj["opts"] = [option_to_html(q["options"][k]) for k in ("A", "B", "C", "D")]
        obj["correct"] = LETTER_TO_INDEX[q["correct"]]
    elif qtype == "mcq_multi":
        obj["opts"] = [option_to_html(q["options"][k]) for k in ("A", "B", "C", "D")]
        obj["correct"] = [LETTER_TO_INDEX[c] for c in q["correct"]]
    elif qtype == "assertion_reason":
        obj["assertionEn"] = q["assertion_en"]
        obj["assertionHi"] = q["assertion_hi"]
        obj["reasonEn"] = q["reason_en"]
        obj["reasonHi"] = q["reason_hi"]
        obj["opts"] = [{"en": o["en"], "hi": o["hi"]} for o in AR_OPTIONS]
        obj["correct"] = LETTER_TO_INDEX[q["correct"]]
    elif qtype == "matching":
        obj["col1"] = [{"en": it["en"], "hi": it["hi"]} for it in q["column1"]]
        obj["col2"] = [{"en": it["en"], "hi": it["hi"]} for it in q["column2"]]
        obj["opts"] = [{"en": it["en"], "hi": it["hi"]} for it in q["column2"]]
        obj["correct"] = q["correct_mapping"]
    return obj


def q_block(questions):
    lines = ["const Q = ["]
    for i, q in enumerate(questions):
        comma = "," if i < len(questions) - 1 else ""
        lines.append("  " + json.dumps(question_to_html_obj(q), ensure_ascii=False) + comma)
    lines.append("];")
    return "\n".join(lines)


def page_shell(title, h1, q_block_text, css, js, assets_prefix="", body_extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="{assets_prefix}assets/style.css">
</head>
<body>
<div class="container">
  <header>
    <h1>{h1}</h1>
    <div class="sub">Bilingual Indian Polity  |  Chapter-wise Sections  |  One question at a time</div>
  </header>

  <div class="controls">
    <button id="btnAll" class="active">All Sections</button>
    <button id="btnReset">Reset Progress</button>
  </div>
  <div class="controls section-list" id="sectionButtons"></div>
  <div class="lang-toggle">
    <button id="langBoth" class="active">Both</button>
    <button id="langEn">English</button>
    <button id="langHi">हिन्दी</button>
  </div>

  <div class="progress-wrap">
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <div class="progress-text">
      <span id="qCounter">Question <span id="curQ">1</span> of <span id="totQ">10</span></span>
      <span id="scoreDisplay">Score: 0</span>
    </div>
  </div>

  <div class="question-card" id="quizArea">
    <div class="q-section" id="qSection"></div>
    <div class="q-number" id="qNumber"></div>
    <div id="arHeader" class="hide"></div>
    <div class="q-en" id="qEn"></div>
    <div class="q-hi" id="qHi"></div>
    <div class="options" id="optionsArea"></div>
    <div class="feedback" id="feedback">
      <h4 id="fbTitle"></h4>
      <div class="tag" id="fbTag"></div>
      <p id="fbEn"></p>
      <p id="fbHi"></p>
      <div class="ref" id="fbRef"></div>
    </div>
    <button class="btn-next" id="btnNext" disabled>Next Question</button>
  </div>

  <div class="result-card hide" id="resultArea">
    <div class="score-big" id="finalScore">0 / 10</div>
    <div class="result-msg" id="finalMsg"></div>
    <div class="weak-list">
      <h4>Weak Topics &amp; Revision</h4>
      <ul id="weakList"></ul>
    </div>
    <button class="btn-restart" onclick="restartTest()">Restart Test</button>
  </div>
</div>

<script>{q_block_text}</script>
<script src="{assets_prefix}assets/quiz.js"></script>
</body>
</html>"""


def write_sections(grouped, order, css, js):
    sections_dir = ROOT / "sections"
    sections_dir.mkdir(exist_ok=True)
    index_rows = []
    for i, sec in enumerate(sorted(order), 1):
        qs = grouped[sec]
        slug = f"{i:02d}-{slugify(sec)}"
        qb = q_block(qs)
        html = page_shell(
            title=f"UPPCS 2026 Polity — {sec}",
            h1=f"UPPCS 2026 Polity — {sec}",
            q_block_text=qb,
            css=css,
            js=js,
            assets_prefix="../",
        )
        (sections_dir / f"{slug}.html").write_text(html, encoding="utf-8")
        index_rows.append((slug, sec, len(qs)))
    return index_rows


def write_index(index_rows, css):
    rows = "\n".join(
        f'<li><a href="sections/{slug}.html">{sec}</a> <span class="count">({n} questions)</span></li>'
        for slug, sec, n in index_rows
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UPPCS 2026 Polity — Section-wise Tests</title>
<link rel="stylesheet" href="assets/style.css">
<style>
  .home {{ max-width: 700px; margin: 40px auto; padding: 0 16px; }}
  .home h2 {{ color: #38bdf8; margin-bottom: 16px; }}
  .home ul {{ list-style: none; padding: 0; }}
  .home li {{ background: #1e293b; border: 1px solid #334155; border-radius: 10px;
              margin: 8px 0; padding: 14px 18px; }}
  .home a {{ color: #38bdf8; text-decoration: none; font-weight: 600; }}
  .home a:hover {{ text-decoration: underline; }}
  .count {{ float: right; color: #94a3b8; font-weight: normal; }}
  .btn {{ display: inline-block; margin-top: 22px; background: #38bdf8; color: #0f172a;
          padding: 12px 24px; border-radius: 10px; text-decoration: none;
          font-weight: 600; }}
  .btn:hover {{ background: #7dd3fc; }}
</style>
</head>
<body>
<div class="container home">
  <header style="text-align:center; margin-bottom:26px;">
    <h1 style="color:#38bdf8;">UPPCS 2026 Polity — Master Test</h1>
    <div class="sub" style="color:#94a3b8;">Bilingual Indian Polity &bull; Chapter-wise sections &bull; One question at a time</div>
  </header>
  <h2>Choose a Section ({len(index_rows)} chapters)</h2>
  <ul>
    {rows}
  </ul>
  <a class="btn" href="all.html">Full Test — All Sections ({sum(n for _, _, n in index_rows)} questions)</a>
</div>
</body>
</html>"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def write_all(questions, css, js):
    qb = q_block(questions)
    html = page_shell(
        title="UPPCS 2026 Polity — Full Test (All Sections)",
        h1="UPPCS 2026 Polity — Full Test (All Sections)",
        q_block_text=qb,
        css=css,
        js=js,
    )
    (ROOT / "all.html").write_text(html, encoding="utf-8")


def main():
    questions, total = load_bank()
    with open(SINGLE_HTML, encoding="utf-8") as f:
        single_html = f.read()
    css, js = extract_assets(single_html)

    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    (assets / "style.css").write_text(css, encoding="utf-8")
    (assets / "quiz.js").write_text(js, encoding="utf-8")

    grouped, order = section_questions(questions)
    index_rows = write_sections(grouped, order, css, js)
    write_index(index_rows, css)
    write_all(questions, css, js)

    print(f"Bank questions: {len(questions)} (total_questions={total})")
    print(f"Sections: {len(order)}")
    print(f"Wrote: assets/style.css, assets/quiz.js, index.html, all.html, sections/ ({len(index_rows)} files)")


if __name__ == "__main__":
    main()
