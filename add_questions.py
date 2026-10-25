"""Add a new bilingual polity question to UPPCS_2026_Polity_Question_Bank.json.

Interactive CLI. Assigns the next available POL-NNN id, validates the input,
and appends the question while keeping the bank's format (indent=2, UTF-8,
letter-based correct answer A-D).
"""

import json
from datetime import date
from pathlib import Path

NOTES_DIR = Path(__file__).resolve().parent
BANK_PATH = NOTES_DIR / "UPPCS_2026_Polity_Question_Bank.json"


def load_bank():
    with open(BANK_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_bank(data):
    with open(BANK_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def next_id(data):
    nums = []
    for q in data["questions"]:
        m = q["id"][4:]
        nums.append(int(m))
    return f"POL-{max(nums) + 1:03d}"


def prompt(label, required=True):
    while True:
        val = input(f"{label}: ").strip()
        if val or not required:
            return val
        print("This field is required.")


def prompt_options():
    opts = {}
    for letter in ("A", "B", "C", "D"):
        opts[letter] = {
            "en": prompt(f"Option {letter} (English)", True),
            "hi": prompt(f"Option {letter} (Hindi)", True),
        }
    while True:
        correct = prompt("Correct option (A-D)", True).upper()
        if correct in ("A", "B", "C", "D"):
            return opts, correct
        print("Enter A, B, C or D.")


def main():
    data = load_bank()
    qid = next_id(data)
    print(f"Adding new question (assigned id: {qid})")

    question = {
        "id": qid,
        "chapter": prompt("Chapter", True),
        "subtopic": prompt("Subtopic", True),
        "question_en": prompt("Question (English)", True),
        "question_hi": prompt("Question (Hindi)", True),
        "options": {},
        "correct": "",
        "correct_en": "",
        "correct_hi": "",
        "explanation_en": prompt("Explanation (English)", True),
        "explanation_hi": prompt("Explanation (Hindi)", True),
        "reference": prompt("Reference (Article / amendment / judgment)", True),
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
    question["options"], question["correct"] = prompt_options()
    question["correct_en"] = question["options"][question["correct"]]["en"]
    question["correct_hi"] = question["options"][question["correct"]]["hi"]

    data["questions"].append(question)
    data["total_questions"] = len(data["questions"])
    data["last_updated"] = date.today().isoformat()
    save_bank(data)
    print(f"Saved {qid}. Bank now has {data['total_questions']} questions.")


if __name__ == "__main__":
    main()
