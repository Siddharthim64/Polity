# Batch 26: Statutory bodies; Elections; Landmark Judgments; UP-specific Polity; Historical background (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Statutory bodies   (need +23 -> 25)
# =====================================================================
CH = "Statutory bodies"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Statutory vs Constitutional",
        "type": "mcq_single",
        "question_en": "Which of the following is NOT a Constitutional body?",
        "question_hi": "निम्नलिखित में से कौन सा संवैधानिक निकाय नहीं है?",
        "options": {
            "A": {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            "B": {"en": "CAG", "hi": "नियंत्रक और महालेखा परीक्षक"},
            "C": {"en": "NITI Aayog", "hi": "नीति आयोग"},
            "D": {"en": "UPSC", "hi": "संघ लोक सेवा आयोग"},
        },
        "correct": "C",
        "explanation_en": "NITI Aayog is a non-constitutional (extra-constitutional) body established by a resolution of the Union Cabinet in 2015.",
        "explanation_hi": "नीति आयोग एक गैर-संवैधानिक निकाय है जो 2015 में केंद्रीय मंत्रिमंडल के एक प्रस्ताव द्वारा स्थापित किया गया था।",
        "reference": "NITI Aayog",
    },
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "mcq_single",
        "question_en": "The National Human Rights Commission was established under:",
        "question_hi": "राष्ट्रीय मानवाधिकार आयोग की स्थापना किसके तहत की गई?",
        "options": {
            "A": {"en": "Protection of Human Rights Act, 1993", "hi": "मानवाधिकार संरक्षण अधिनियम, 1993"},
            "B": {"en": "Constitution of India", "hi": "भारत का संविधान"},
            "C": {"en": "RTI Act, 2005", "hi": "सूचना का अधिकार अधिनियम, 2005"},
            "D": {"en": "CVC Act, 2003", "hi": "सीवीसी अधिनियम, 2003"},
        },
        "correct": "A",
        "explanation_en": "The National Human Rights Commission (NHRC) is a statutory body established under the Protection of Human Rights Act, 1993.",
        "explanation_hi": "राष्ट्रीय मानवाधिकार आयोग (एनएचआरसी) मानवाधिकार संरक्षण अधिनियम, 1993 के तहत स्थापित एक सांविधिक निकाय है।",
        "reference": "Protection of Human Rights Act, 1993",
    },
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "mcq_single",
        "question_en": "The Central Information Commission was established under:",
        "question_hi": "केंद्रीय सूचना आयोग की स्थापना किसके तहत की गई?",
        "options": {
            "A": {"en": "Right to Information Act, 2005", "hi": "सूचना का अधिकार अधिनियम, 2005"},
            "B": {"en": "Constitution of India", "hi": "भारत का संविधान"},
            "C": {"en": "CVC Act, 2003", "hi": "सीवीसी अधिनियम, 2003"},
            "D": {"en": "NHRC Act, 1993", "hi": "एनएचआरसी अधिनियम, 1993"},
        },
        "correct": "A",
        "explanation_en": "The Central Information Commission (CIC) is a statutory body established under the Right to Information Act, 2005.",
        "explanation_hi": "केंद्रीय सूचना आयोग (सीआईसी) सूचना का अधिकार अधिनियम, 2005 के तहत स्थापित एक सांविधिक निकाय है।",
        "reference": "Right to Information Act, 2005",
    },
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "mcq_single",
        "question_en": "NITI Aayog was established in:",
        "question_hi": "नीति आयोग की स्थापना कब की गई?",
        "options": {
            "A": {"en": "2015", "hi": "2015"},
            "B": {"en": "1950", "hi": "1950"},
            "C": {"en": "1991", "hi": "1991"},
            "D": {"en": "2000", "hi": "2000"},
        },
        "correct": "A",
        "explanation_en": "NITI Aayog (National Institution for Transforming India) was established on 1 January 2015, replacing the Planning Commission.",
        "explanation_hi": "नीति आयोग (राष्ट्र परिवर्तन के लिए राष्ट्रीय संस्थान) की स्थापना 1 जनवरी 2015 को की गई, जिसने योजना आयोग का स्थान लिया।",
        "reference": "NITI Aayog",
    },
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "mcq_single",
        "question_en": "The Central Vigilance Commission was established under:",
        "question_hi": "केंद्रीय सतर्कता आयोग की स्थापना किसके तहत की गई?",
        "options": {
            "A": {"en": "CVC Act, 2003", "hi": "सीवीसी अधिनियम, 2003"},
            "B": {"en": "Constitution of India", "hi": "भारत का संविधान"},
            "C": {"en": "RTI Act, 2005", "hi": "सूचना का अधिकार अधिनियम, 2005"},
            "D": {"en": "NHRC Act, 1993", "hi": "एनएचआरसी अधिनियम, 1993"},
        },
        "correct": "A",
        "explanation_en": "The Central Vigilance Commission (CVC) is a statutory body established under the Central Vigilance Commission Act, 2003.",
        "explanation_hi": "केंद्रीय सतर्कता आयोग (सीवीसी) केंद्रीय सतर्कता आयोग अधिनियम, 2003 के तहत स्थापित एक सांविधिक निकाय है।",
        "reference": "Central Vigilance Commission Act, 2003",
    },
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "mcq_single",
        "question_en": "The National Green Tribunal was established under:",
        "question_hi": "राष्ट्रीय हरित न्यायाधिकरण की स्थापना किसके तहत की गई?",
        "options": {
            "A": {"en": "National Green Tribunal Act, 2010", "hi": "राष्ट्रीय हरित न्यायाधिकरण अधिनियम, 2010"},
            "B": {"en": "Constitution of India", "hi": "भारत का संविधान"},
            "C": {"en": "RTI Act, 2005", "hi": "सूचना का अधिकार अधिनियम, 2005"},
            "D": {"en": "CVC Act, 2003", "hi": "सीवीसी अधिनियम, 2003"},
        },
        "correct": "A",
        "explanation_en": "The National Green Tribunal (NGT) is a statutory body established under the National Green Tribunal Act, 2010 for effective expeditious disposal of cases relating to environmental protection.",
        "explanation_hi": "राष्ट्रीय हरित न्यायाधिकरण (एनजीटी) राष्ट्रीय हरित न्यायाधिकरण अधिनियम, 2010 के तहत स्थापित एक सांविधिक निकाय है जो पर्यावरण संरक्षण से संबंधित मामलों के प्रभावी और शीघ्र निस्तारण के लिए है।",
        "reference": "National Green Tribunal Act, 2010",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Types of bodies",
        "type": "mcq_multi",
        "question_en": "Which of the following are Constitutional bodies (not statutory)?",
        "question_hi": "निम्नलिखित में से कौन से संवैधानिक निकाय हैं (सांविधिक नहीं)?",
        "options": {
            "A": {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            "B": {"en": "CAG", "hi": "नियंत्रक और महालेखा परीक्षक"},
            "C": {"en": "NHRC", "hi": "राष्ट्रीय मानवाधिकार आयोग"},
            "D": {"en": "UPSC", "hi": "संघ लोक सेवा आयोग"},
            "E": {"en": "Finance Commission", "hi": "वित्त आयोग"},
        },
        "correct": "ABDE",
        "explanation_en": "Election Commission, CAG, UPSC and Finance Commission are Constitutional bodies. NHRC is a statutory body.",
        "explanation_hi": "निर्वाचन आयोग, नियंत्रक और महालेखा परीक्षक, संघ लोक सेवा आयोग और वित्त आयोग संवैधानिक निकाय हैं। एनएचआरसी एक सांविधिक निकाय है।",
        "reference": "Articles 324, 148, 315, 280",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Statutory bodies",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "NITI Aayog is not a Constitutional body.",
        "assertion_hi": "नीति आयोग एक संवैधानिक निकाय नहीं है।",
        "reason_en": "NITI Aayog was established by a resolution of the Union Cabinet and not by any provision of the Constitution.",
        "reason_hi": "नीति आयोग की स्थापना केंद्रीय मंत्रिमंडल के एक प्रस्ताव द्वारा की गई थी न कि संविधान के किसी प्रावधान द्वारा।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — NITI Aayog is an extra-constitutional body created by executive resolution.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — नीति आयोग एक गैर-संवैधानिक निकाय है जो कार्यकारी प्रस्ताव द्वारा बनाया गया है।",
        "reference": "NITI Aayog",
    },
    # ---- matching ----
    {
        "chapter": CH, "subtopic": "Bodies",
        "type": "matching",
        "question_en": None,
        "question_hi": None,
        "column1": [
            {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            {"en": "NHRC", "hi": "राष्ट्रीय मानवाधिकार आयोग"},
            {"en": "CIC", "hi": "केंद्रीय सूचना आयोग"},
            {"en": "CVC", "hi": "केंद्रीय सतर्कता आयोग"},
        ],
        "column2": [
            {"en": "Constitutional body", "hi": "संवैधानिक निकाय"},
            {"en": "Protection of Human Rights Act, 1993", "hi": "मानवाधिकार संरक्षण अधिनियम, 1993"},
            {"en": "Right to Information Act, 2005", "hi": "सूचना का अधिकार अधिनियम, 2005"},
            {"en": "Central Vigilance Commission Act, 2003", "hi": "केंद्रीय सतर्कता आयोग अधिनियम, 2003"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch26 prepared: {len(NEW_QUESTIONS)} questions")
