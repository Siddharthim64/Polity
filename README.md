# UPPCS 2026 Polity — Chapter-wise Practice

A bilingual (English + हिन्दी) chapter-wise Indian Polity practice test for UPPCS 2026 preparation. Clean, professional UI that works on both desktop and mobile.

## Features

- **33 chapters** covering the full UPPCS Polity syllabus
- **120 questions** with detailed explanations and references
- **Bilingual**: English and हिन्दी (toggle between Both / English / हिन्दी)
- **Sections on the left**, questions on the right — desktop shows a fixed sidebar; mobile uses a slide-in drawer
- **Instant feedback** with correct answer, explanation, and reference
- **Score tracking** and weak-topic revision list
- **Light, professional theme** — simple and distraction-free

## Files

| File | Purpose |
|------|---------|
| `index.html` | Main app — single self-contained HTML page |
| `data/questions.js` | Question bank (120 questions across 33 chapters) |
| `gen_website.py` | Generator script that builds the site from the JSON bank |
| `UPPCS_2026_Polity_Question_Bank.json` | Master question bank |

## How to run

No build step required. Just open `index.html` in any modern browser, or serve the folder with any static host (GitHub Pages, Netlify, Vercel, etc.):

```bash
# Using Python
python -m http.server 8000 --directory uppcs_polity_website
# Then open http://localhost:8000
```

## How it works

1. Chapters are listed in the left sidebar — tap any chapter to start
2. Questions appear one at a time in the main area (English + हिन्दī)
3. Select an answer to see instant feedback with explanation
4. Track your score and review weak topics at the end
5. Use "Full Test — All Sections" for a mixed 120-question test

## License

MIT