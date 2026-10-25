# Batch 29: Landmark Judgments; UP-specific Polity; Historical background; Fundamental Rights; Parliament; Elections (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Landmark Judgments   (need +13 -> 23)
# =====================================================================
CH = "Landmark Judgments"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Basic structure",
        "type": "mcq_single",
        "question_en": "The basic structure doctrine was evolved in:",
        "question_hi": "मूल संरचना का सिद्धांत किस मामले में विकसित किया गया?",
        "options": {
            "A": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "B": {"en": "Golaknath", "hi": "गोलकनाथ"},
            "C": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
            "D": {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
        },
        "correct": "A",
        "explanation_en": "Kesavananda Bharati v. State of Kerala (1973) evolved the basic structure doctrine.",
        "explanation_hi": "केसवानंद भारती बनाम केरल राज्य (1973) ने मूल संरचना सिद्धांत विकसित किया।",
        "reference": "Kesavananda Bharati v. State of Kerala (1973)",
    },
    {
        "chapter": CH, "subtopic": "Right to privacy",
        "type": "mcq_single",
        "question_en": "Right to privacy was declared a Fundamental Right in:",
        "question_hi": "निजता का अधिकार किस मामले में मौलिक अधिकार घोषित किया गया?",
        "options": {
            "A": {"en": "Puttaswamy", "hi": "पुट्टस्वामी"},
            "B": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "C": {"en": "Maneka Gandhi", "hi": "मेनका गांधी"},
            "D": {"en": "Vishaka", "hi": "विशाका"},
        },
        "correct": "A",
        "explanation_en": "Justice K.S. Puttaswamy v. Union of India (2017) declared right to privacy a Fundamental Right under Article 21.",
        "explanation_hi": "जस्टिस के.एस. पुट्टस्वामी बनाम भारत संघ (2017) ने अनुच्छेद 21 के तहत निजता के अधिकार को मौलिक अधिकार घोषित किया।",
        "reference": "Puttaswamy v. Union of India (2017)",
    },
    {
        "chapter": CH, "subtopic": "Article 21",
        "type": "mcq_single",
        "question_en": "Article 21 (right to life and personal liberty) was given wide interpretation in:",
        "question_hi": "अनुच्छेद 21 (जीवन और व्यक्तिगत स्वतंत्रता का अधिकार) का विस्तृत व्याख्या किस मामले में की गई?",
        "options": {
            "A": {"en": "Maneka Gandhi", "hi": "मेनका गांधी"},
            "B": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "C": {"en": "Golaknath", "hi": "गोलकनाथ"},
            "D": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
        },
        "correct": "A",
        "explanation_en": "Maneka Gandhi v. Union of India (1978) gave a wide interpretation to Article 21.",
        "explanation_hi": "मेनका गांधी बनाम भारत संघ (1978) ने अनुच्छेद 21 की व्यापक व्याख्या की।",
        "reference": "Maneka Gandhi v. Union of India (1978)",
    },
    {
        "chapter": CH, "subtopic": "Triple talaq",
        "type": "mcq_single",
        "question_en": "Triple talaq was declared unconstitutional in:",
        "question_hi": "तीन तलाक किस मामले में असंवैधानिक घोषित किया गया?",
        "options": {
            "A": {"en": "Shayara Bano", "hi": "शायरा बानो"},
            "B": {"en": "Puttaswamy", "hi": "पुट्टस्वामी"},
            "C": {"en": "Navtej Singh Johar", "hi": "नवtej सिंह जौहर"},
            "D": {"en": "Vishaka", "hi": "विशाका"},
        },
        "correct": "A",
        "explanation_en": "Shayara Bano v. Union of India (2017) declared the practice of instant triple talaq unconstitutional.",
        "explanation_hi": "शायरा बानो बनाम भारत संघ (2017) ने तुरंत तीन तलाक की प्रथा को असंवैधानिक घोषित किया।",
        "reference": "Shayara Bano v. Union of India (2017)",
    },
    {
        "chapter": CH, "subtopic": "Section 377",
        "type": "mcq_single",
        "question_en": "Section 377 of IPC was partially struck down in:",
        "question_hi": "आईपीसी की धारा 377 किस मामले में आंशिक रूप से रद्द की गई?",
        "options": {
            "A": {"en": "Navtej Singh Johar", "hi": "नवtej सिंह जौहर"},
            "B": {"en": "Puttaswamy", "hi": "पुट्टस्वामी"},
            "C": {"en": "Shayara Bano", "hi": "शायरा बानो"},
            "D": {"en": "Maneka Gandhi", "hi": "मेनका गांधी"},
        },
        "correct": "A",
        "explanation_en": "Navtej Singh Johar v. Union of India (2018) decriminalized consensual same-sex relations by partially striking down Section 377 IPC.",
        "explanation_hi": "नवtej सिंह जौहर बनाम भारत संघ (2018) ने आईपीसी की धारा 377 को आंशिक रूप से रद्द करके सहमति से समलैंगिक संबंधों को अपराधमुक्त कर दिया।",
        "reference": "Navtej Singh Johar v. Union of India (2018)",
    },
    {
        "chapter": CH, "subtopic": "Vishaka",
        "type": "mcq_single",
        "question_en": "Vishaka guidelines relate to:",
        "question_hi": "विशाका दिशानिर्देश किससे संबंधित हैं?",
        "options": {
            "A": {"en": "Sexual harassment at workplace", "hi": "कार्यस्थल पर यौन उत्पीड़न"},
            "B": {"en": "Environment", "hi": "पर्यावरण"},
            "C": {"en": "Education", "hi": "शिक्षा"},
            "D": {"en": "Health", "hi": "स्वास्थ्य"},
        },
        "correct": "A",
        "explanation_en": "Vishaka v. State of Rajasthan (1997) laid down guidelines for prevention of sexual harassment of women at the workplace.",
        "explanation_hi": "विशाका बनाम राजस्थान राज्य (1997) ने कार्यस्थल पर महिलाओं के यौन उत्पीड़न की रोकथाम के लिए दिशानिर्देश तैयार किए।",
        "reference": "Vishaka v. State of Rajasthan (1997)",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Judgments",
        "type": "mcq_multi",
        "question_en": "Which of the following are basic structure cases?",
        "question_hi": "निम्नलिखित में से कौन से मूल संरचना मामले हैं?",
        "options": {
            "A": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "B": {"en": "Indira Gandhi v. Raj Narain", "hi": "इंदिरा गांधी बनाम राज नारायण"},
            "C": {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
            "D": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
            "E": {"en": "I.R. Coelho", "hi": "आई.आर. कोहली"},
        },
        "correct": "ABCE",
        "explanation_en": "Kesavananda Bharati, Indira Gandhi v. Raj Narain, Minerva Mills and I.R. Coelho are basic structure cases.",
        "explanation_hi": "केसवानंद भारती, इंदिरा गांधी बनाम राज नारायण, मिनर्वा मिल्स और आई.आर. कोहली मूल संरचना मामले हैं।",
        "reference": "Various Supreme Court judgments",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Basic structure",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "Parliament cannot destroy the basic structure by constitutional amendment.",
        "assertion_hi": "संसद संवैधानिक संशोधन द्वारा मूल संरचना को नष्ट नहीं कर सकती।",
        "reason_en": "The Supreme Court in Kesavananda Bharati held that the basic structure cannot be destroyed.",
        "reason_hi": "सर्वोच्च न्यायालय ने केसवानंद भारती में माना कि मूल संरचना को नष्ट नहीं किया जा सकता।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — the basic structure cannot be destroyed by amendment.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — मूल संरचना को संशोधन द्वारा नष्ट नहीं किया जा सकता।",
        "reference": "Kesavananda Bharati case",
    },
    # ---- matching ----
    {
        "chapter": CH, "subtopic": "Judgments",
        "type": "matching",
        "question_en": None,
        "question_hi": None,
        "column1": [
            {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            {"en": "Puttaswamy", "hi": "पुट्टस्वामी"},
            {"en": "Navtej Singh Johar", "hi": "नवtej सिंह जौहर"},
            {"en": "Shayara Bano", "hi": "शायरा बानो"},
        ],
        "column2": [
            {"en": "Basic structure doctrine", "hi": "मूल संरचना सिद्धांत"},
            {"en": "Right to privacy", "hi": "निजता का अधिकार"},
            {"en": "Section 377 decriminalized", "hi": "धारा 377 अपराधमुक्त"},
            {"en": "Triple talaq unconstitutional", "hi": "तीन तलाक असंवैधानिक"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch29 prepared: {len(NEW_QUESTIONS)} questions")
