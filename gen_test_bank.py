"""Generate uppcs_polity_test.html from UPPCS_2026_Polity_Question_Bank.json.

Reads the master question bank (single source of truth) and regenerates the
embedded ``const Q = [...]`` question bank inside the HTML test, keeping the
HTML/CSS/JS shell intact. Question ``correct`` values are letters (A-D) in the
JSON and are converted to 0-based indices for the HTML test.
"""

import json
import re
from pathlib import Path

NOTES_DIR = Path(__file__).resolve().parent
BANK_PATH = NOTES_DIR / "UPPCS_2026_Polity_Question_Bank.json"
HTML_PATH = NOTES_DIR / "uppcs_polity_test.html"

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}
FIELD_MAP = {
    "question_en": "qEn",
    "question_hi": "qHi",
    "correct_en": "cEn",
    "correct_hi": "cHi",
    "explanation_en": "eEn",
    "explanation_hi": "eHi",
    "reference": "ref",
}


def load_bank(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    questions = data["questions"]
    ids = [q["id"] for q in questions]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate question IDs in bank")
    if ids != [f"POL-{i:03d}" for i in range(1, len(ids) + 1)]:
        raise SystemExit("question IDs are not contiguous POL-001..N")
    for q in questions:
        if q["correct"] not in LETTER_TO_INDEX:
            raise SystemExit(f"{q['id']}: invalid correct value {q['correct']!r}")
        if sorted(q["options"].keys()) != ["A", "B", "C", "D"]:
            raise SystemExit(f"{q['id']}: options must be A-D")
        for key, html_key in FIELD_MAP.items():
            if not q.get(key):
                raise SystemExit(f"{q['id']}: missing {key}")
    return data, questions


def option_to_html(letter, opt):
    return {"en": opt["en"], "hi": opt["hi"]}


def question_to_html(q):
    correct_idx = LETTER_TO_INDEX[q["correct"]]
    obj = {
        "id": q["id"],
        "section": q["chapter"],
        "sub": q["subtopic"],
        "qEn": q["question_en"],
        "qHi": q["question_hi"],
        "opts": [option_to_html(k, q["options"][k]) for k in ("A", "B", "C", "D")],
        "correct": correct_idx,
        "cEn": q["correct_en"],
        "cHi": q["correct_hi"],
        "eEn": q["explanation_en"],
        "eHi": q["explanation_hi"],
        "ref": q["reference"],
    }
    return json.dumps(obj, ensure_ascii=False)


def regenerate_html(html_text, questions):
    start_marker = "/* ============ QUESTION BANK ============ */"
    end_marker = "/* ============ STATE ============ */"
    start = html_text.index(start_marker)
    end = html_text.index(end_marker)
    lines = ["const Q = ["]
    for i, q in enumerate(questions):
        comma = "," if i < len(questions) - 1 else ""
        lines.append("  " + question_to_html(q) + comma)
    lines.append("];")
    new_block = start_marker + "\n" + "\n".join(lines) + "\n\n" + end_marker
    return html_text[:start] + new_block + html_text[end:]


def main():
    data, questions = load_bank(BANK_PATH)
    with open(HTML_PATH, encoding="utf-8") as f:
        html_text = f.read()
    new_html = regenerate_html(html_text, questions)
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"regenerated {HTML_PATH.name} with {len(questions)} questions "
          f"(bank total_questions={data.get('total_questions')})")


if __name__ == "__main__":
    main()
