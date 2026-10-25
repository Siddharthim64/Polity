# Batch 28: Landmark Judgments; UP-specific Polity; Historical background; Fundamental Rights; Parliament; Elections; Constitutional bodies (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Landmark Judgments   (need +23 -> 25)
# =====================================================================
CH = "Landmark Judgments"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Basic structure",
        "type": "mcq_single",
        "question_en": "The basic structure doctrine was propounded in:",
        "question_hi": "मूल संरचना का सिद्धांत किस मामले में प्रतिपादित किया गया?",
        "options": {
            "A": {"en": "Kesavananda Bharati v. State of Kerala", "hi": "केसवानंद भारती बनाम केरल राज्य"},
            "B": {"en": "Golaknath v. State of Punjab", "hi": "गोलकनाथ बनाम पंजाब राज्य"},
            "C": {"en": "Shankari Prasad v. Union of India", "hi": "शंकारी प्रसाद बनाम भारत संघ"},
            "D": {"en": "Minerva Mills v. Union of India", "hi": "मिनर्वा मिल्स बनाम भारत संघ"},
        },
        "correct": "A",
        "explanation_en": "The doctrine of basic structure was propounded by the Supreme Court in Kesavananda Bharati v. State of Kerala (1973).",
        "explanation_hi": "मूल संरचना का सिद्धांत सर्वोच्च न्यायालय द्वारा केसवानंद भारती बनाम केरल राज्य (1973) में प्रतिपादित किया गया।",
        "reference": "Kesavananda Bharati v. State of Kerala (1973)",
    },
    {
        "chapter": CH, "subtopic": "Judicial review",
        "type": "mcq_single",
        "question_en": "Parliament's power to amend Fundamental Rights was upheld in:",
        "question_hi": "मौलिक अधिकारों में संशोधन की संसद की शक्ति किस मामले में बरकरार रखी गई?",
        "options": {
            "A": {"en": "Shankari Prasad v. Union of India", "hi": "शंकारी प्रसाद बनाम भारत संघ"},
            "B": {"en": "Golaknath v. State of Punjab", "hi": "गोलकनाथ बनाम पंजाब राज्य"},
            "C": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "D": {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
        },
        "correct": "A",
        "explanation_en": "In Shankari Prasad v. Union of India (1951), the Supreme Court upheld Parliament's power to amend Fundamental Rights under Article 368.",
        "explanation_hi": "शंकारी प्रसाद बनाम भारत संघ (1951) में, सर्वोच्च न्यायालय ने अनुच्छेद 368 के तहत मौलिक अधिकारों में संशोधन की संसद की शक्ति को बरकरार रखा।",
        "reference": "Shankari Prasad v. Union of India (1951)",
    },
    {
        "chapter": CH, "subtopic": "Judicial review",
        "type": "mcq_single",
        "question_en": "Parliament's power to amend Fundamental Rights was curtailed in:",
        "question_hi": "मौलिक अधिकारों में संशोधन की संसद की शक्ति किस मामले में curtailed की गई?",
        "options": {
            "A": {"en": "Golaknath v. State of Punjab", "hi": "गोलकनाथ बनाम पंजाब राज्य"},
            "B": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
            "C": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "D": {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
        },
        "correct": "A",
        "explanation_en": "In Golaknath v. State of Punjab (1967), the Supreme Court held that Parliament cannot curtail Fundamental Rights.",
        "explanation_hi": "गोलकनाथ बनाम पंजाब राज्य (1967) में, सर्वोच्च न्यायालय ने माना कि संसद मौलिक अधिकारों को संकीर्ण नहीं कर सकती।",
        "reference": "Golaknath v. State of Punjab (1967)",
    },
    {
        "chapter": CH, "subtopic": "Right to life",
        "type": "mcq_single",
        "question_en": "The right to life and personal liberty was expanded in:",
        "question_hi": "जीवन और व्यक्तिगत स्वतंत्रता का अधिकार किस मामले में विस्तृत किया गया?",
        "options": {
            "A": {"en": "Maneka Gandhi v. Union of India", "hi": "मेनका गांधी बनाम भारत संघ"},
            "B": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "C": {"en": "Golaknath", "hi": "गोलकनाथ"},
            "D": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
        },
        "correct": "A",
        "explanation_en": "In Maneka Gandhi v. Union of India (1978), the Supreme Court gave a wide interpretation to Article 21, holding that the procedure must be reasonable, fair and just.",
        "explanation_hi": "मेनका गांधी बनाम भारत संघ (1978) में, सर्वोच्च न्यायालय ने अनुच्छेद 21 की व्यापक व्याख्या की, यह मानते हुए कि प्रक्रिया उचित, निष्पक्ष और न्यायसंगत होनी चाहिए।",
        "reference": "Maneka Gandhi v. Union of India (1978)",
    },
    {
        "chapter": CH, "subtopic": "Right to privacy",
        "type": "mcq_single",
        "question_en": "The right to privacy was declared a Fundamental Right in:",
        "question_hi": "निजता का अधिकार किस मामले में एक मौलिक अधिकार घोषित किया गया?",
        "options": {
            "A": {"en": "Puttaswamy v. Union of India", "hi": "पुट्टस्वामी बनाम भारत संघ"},
            "B": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "C": {"en": "Maneka Gandhi", "hi": "मेनका गांधी"},
            "D": {"en": "Vishaka", "hi": "विशाका"},
        },
        "correct": "A",
        "explanation_en": "In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), the Supreme Court declared the right to privacy a Fundamental Right under Article 21.",
        "explanation_hi": "जस्टिस के.एस. पुट्टस्वामी (सेवानिवृत्त) बनाम भारत संघ (2017) में, सर्वोच्च न्यायालय ने निजता के अधिकार को अनुच्छेद 21 के तहत एक मौलिक अधिकार घोषित किया।",
        "reference": "Justice K.S. Puttaswamy v. Union of India (2017)",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Judgments",
        "type": "mcq_multi",
        "question_en": "Which of the following are landmark judgments on basic structure?",
        "question_hi": "निम्नलिखित में से कौन से मूल संरचना पर ऐतिहासिक फैसले हैं?",
        "options": {
            "A": {"en": "Kesavananda Bharati", "hi": "केसवानंद भारती"},
            "B": {"en": "Indira Gandhi v. Raj Narain", "hi": "इंदिरा गांधी बनाम राज नारायण"},
            "C": {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
            "D": {"en": "Shankari Prasad", "hi": "शंकारी प्रसाद"},
            "E": {"en": "I.R. Coelho", "hi": "आई.आर. कोहली"},
        },
        "correct": "ABCE",
        "explanation_en": "Kesavananda Bharati, Indira Gandhi v. Raj Narain, Minerva Mills and I.R. Coelho are landmark basic structure cases. Shankari Prasad upheld Parliament's amending power (pre-basic structure).",
        "explanation_hi": "केसवानंद भारती, इंदिरा गांधी बनाम राज नारायण, मिनर्वा मिल्स और आई.आर. कोहली मूल संरचना के ऐतिहासिक मामले हैं। शंकारी प्रसाद ने संसद की संशोधन शक्ति को बरकरार रखा (मूल संरचना सिद्धांत से पहले)।",
        "reference": "Various Supreme Court judgments",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Basic structure",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "Parliament cannot amend Fundamental Rights to destroy the basic structure.",
        "assertion_hi": "संसद मूल संरचना को नष्ट करने के लिए मौलिक अधिकारों में संशोधन नहीं कर सकती।",
        "reason_en": "The basic structure of the Constitution cannot be destroyed by any constitutional amendment under Article 368.",
        "reason_hi": "संविधान की मूल संरचना को अनुच्छेद 368 के तहत किसी भी संवैधानिक संशोधन द्वारा नष्ट नहीं किया जा सकता।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — the basic structure cannot be destroyed by amendment under Article 368.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — अनुच्छेद 368 के तहत संशोधन द्वारा मूल संरचना को नष्ट नहीं किया जा सकता।",
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
            {"en": "Golaknath", "hi": "गोलकनाथ"},
            {"en": "Minerva Mills", "hi": "मिनर्वा मिल्स"},
            {"en": "Maneka Gandhi", "hi": "मेनका गांधी"},
        ],
        "column2": [
            {"en": "Basic structure doctrine", "hi": "मूल संरचना सिद्धांत"},
            {"en": "Parliament cannot curtail FR", "hi": "संसद मौलिक अधिकारों को संकीर्ण नहीं कर सकती"},
            {"en": "42nd Amendment clauses struck down", "hi": "42वें संशोधन के खंड रद्द किए गए"},
            {"en": "Article 21 expanded", "hi": "अनुच्छेद 21 विस्तृत किया गया"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch28 prepared: {len(NEW_QUESTIONS)} questions")
