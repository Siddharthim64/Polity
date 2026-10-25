"""Bulk-add bilingual polity questions to UPPCS_2026_Polity_Question_Bank.json."""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BANK_PATH = ROOT / "UPPCS_2026_Polity_Question_Bank.json"

LETTER_TO_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

# Question data is imported from a separate module
# Assertion-Reason options
AR_OPTIONS = [
    {"en": "Both A and R are true and R is the correct explanation of A", "hi": "A और R दोनों सत्य हैं और R, A की सही व्याख्या है"},
    {"en": "Both A and R are true but R is NOT the correct explanation of A", "hi": "A और R दोनों सत्य हैं परंतु R, A की सही व्याख्या नहीं है"},
    {"en": "A is true but R is false", "hi": "A सत्य है परंतु R असत्य है"},
    {"en": "A is false but R is true", "hi": "A असत्य है परंतु R सत्य है"},
    {"en": "Both A and R are false", "hi": "A और R दोनों असत्य हैं"},
]

# Question data is imported from a separate module (e.g. batch1.py exposing
# NEW_QUESTIONS = [...]).  Pass the module name as the first arg, else
# default "batch_questions".
import sys

MODULE_NAME = sys.argv[1] if len(sys.argv) > 1 else "batch_questions"
try:
    mod = __import__(MODULE_NAME)
    NEW_QUESTIONS = mod.NEW_QUESTIONS
except (ImportError, AttributeError) as e:
    raise SystemExit(f"Could not import NEW_QUESTIONS from module {MODULE_NAME!r}: {e}")


def load_bank():
    with open(BANK_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_bank(data):
    with open(BANK_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def next_id(data):
    nums = [int(q["id"][4:]) for q in data["questions"]]
    return f"POL-{max(nums) + 1:03d}"


def mastery_defaults():
    return {
        "pyq_based": False,
        "exam_year": None,
        "attempts": 0,
        "correct_count": 0,
        "incorrect_count": 0,
        "streak": 0,
        "last_attempt": None,
        "next_review": None,
        "mastery_status": "Not started",
        "mistake_categories": [],
    }


def _norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def _dup_key(q):
    """Key used to detect duplicate questions within a chapter."""
    if q.get("question_en"):
        return _norm(q["question_en"])
    if q.get("assertion_en"):
        return "AR::" + _norm(q["assertion_en"]) + "::" + _norm(q.get("reason_en", ""))
    if q.get("col1"):
        return "MATCH::" + _norm(json.dumps(q["col1"], ensure_ascii=False))
    return _norm(json.dumps(q, ensure_ascii=False))


def _opts(q):
    """Get options as dict {letter: {en, hi}} from various formats."""
    opts = q.get("options")
    if opts is None:
        opts = q.get("opts", {})
    if isinstance(opts, list):
        return {LETTER_TO_INDEX_inv[i]: o for i, o in enumerate(opts) if isinstance(o, dict)}
    return opts or {}


def _correct(q, qtype):
    """Get correct answer as letter(s) from various formats."""
    c = q.get("correct")
    if c is None:
        return "A"  # Default fallback
    if isinstance(c, int):
        return LETTER_TO_INDEX_inv.get(c, str(c))
    if isinstance(c, list):
        return [LETTER_TO_INDEX_inv.get(x, x) for x in c]
    if isinstance(c, dict):
        result = {}
        for k, v in c.items():
            try:
                result[LETTER_TO_INDEX_inv.get(int(k), k)] = LETTER_TO_INDEX_inv.get(int(v), v)
            except (ValueError, TypeError):
                result[k] = v
        return result
    return c  # Already a letter string like "A" or "AB"


def option_to_html(letter, opt):
    return {"en": opt.get("en", ""), "hi": opt.get("hi", "")}


def build_question(qid, q):
    """Return a fully-formed bank question dict from a content dict + id."""
    chapter = q.get("chapter") or q.get("section") or q.get("chapter_name", "")
    subtopic = q.get("subtopic") or q.get("sub_topic") or q.get("sub_topic_name", "")
    qtype = q.get("type", "mcq_single")

    base = {
        "id": qid,
        "chapter": chapter,
        "subtopic": subtopic,
        "type": qtype,
        "question_en": q.get("question_en", q.get("question", "")),
        "question_hi": q.get("question_hi", ""),
    }
    base.update(mastery_defaults())

    opts = _opts(q)

    if qtype == "mcq_single":
        base["opts"] = [option_to_html(k, opts.get(k, {"en": "", "hi": ""})) for k in ("A", "B", "C", "D")]
        base["correct"] = LETTER_TO_INDEX[_correct(q, qtype)]
    elif qtype == "mcq_multi":
        base["opts"] = [option_to_html(k, opts.get(k, {"en": "", "hi": ""})) for k in ("A", "B", "C", "D")]
        base["correct"] = [LETTER_TO_INDEX[c] for c in _correct(q, qtype)]
    elif qtype == "assertion_reason":
        base["assertion_en"] = q.get("assertion_en", "")
        base["assertionHi"] = q.get("assertion_hi", "")
        base["reason_en"] = q.get("reason_en", "")
        base["reasonHi"] = q.get("reason_hi", "")
        base["opts"] = [{"en": o["en"], "hi": o["hi"]} for o in AR_OPTIONS]
        base["correct"] = LETTER_TO_INDEX[_correct(q, qtype)]
    elif qtype == "matching":
        base["col1"] = q.get("col1", q.get("column1", []))
        base["column2"] = q.get("col2", q.get("column2", []))
        base["correct_mapping"] = q.get("correct_mapping", {})
    else:
        raise ValueError(f"unknown type {qtype!r}")

    base["explanation_en"] = q.get("explanation_en", "")
    base["explanation_hi"] = q.get("explanation_hi", "")
    base["ref"] = q.get("ref", "")
    return base


def main():
    data = load_bank()
    existing = data["questions"]

    # Track existing question text per chapter for duplicate detection.
    seen = {}
    for q in existing:
        seen.setdefault(q["chapter"], set()).add(_dup_key(q))

    qid_num = max(int(q["id"][4:]) for q in existing) + 1
    added = 0
    skipped = 0

    for q in NEW_QUESTIONS:
        chap = q.get("chapter") or q.get("section") or q.get("chapter_name", "")
        key = _dup_key(q)
        if key in seen.setdefault(chap, set()):
            print(f"SKIP duplicate in {chap!r}: {q.get('question_en') or q.get('assertion_en') or q.get('col1',[{}])[0].get('en','')[:70]}...")
            skipped += 1
            continue
        seen[chap].add(key)

        qid = f"POL-{qid_num:03d}"
        qid_num += 1
        full = build_question(qid, q)
        existing.append(full)
        data["questions"] = existing
        added += 1

    data["total_questions"] = len(existing)
    data["last_updated"] = date.today().isoformat()
    save_bank(data)
    print(f"Added {added} question(s), skipped {skipped} duplicate(s). "
          f"Bank now has {data['total_questions']} questions.")


if __name__ == "__main__":
    main()