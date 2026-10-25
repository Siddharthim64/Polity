# Batch 24: Constitutional bodies (remaining); Cooperative societies; Statutory bodies (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Constitutional bodies   (remaining +10 -> 25)
# =====================================================================
CH = "Constitutional bodies"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Election Commission",
        "type": "mcq_single",
        "question_en": "The Chief Election Commissioner holds office for a term of:",
        "question_hi": "मुख्य निर्वाचन आयुक्त कितने वर्षों के कार्यकाल के लिए पद धारण करता है?",
        "options": {
            "A": {"en": "6 years or age 65, whichever is earlier", "hi": "6 वर्ष या 65 वर्ष की आयु, जो पहले हो"},
            "B": {"en": "5 years", "hi": "5 वर्ष"},
            "C": {"en": "6 years", "hi": "6 वर्ष"},
            "D": {"en": "5 years or age 65", "hi": "5 वर्ष या 65 वर्ष की आयु"},
        },
        "correct": "A",
        "explanation_en": "The Chief Election Commissioner holds office for a term of 6 years or until he attains the age of 65 years, whichever is earlier.",
        "explanation_hi": "मुख्य निर्वाचन आयुक्त 6 वर्ष या 65 वर्ष की आयु प्राप्त करने तक, जो पहले हो, पद धारण करता है।",
        "reference": "Article 324; Election Commission (Conditions of Service) Act",
    },
    {
        "chapter": CH, "subtopic": "CAG",
        "type": "mcq_single",
        "question_en": "The CAG holds office for a term of:",
        "question_hi": "नियंत्रक और महालेखा परीक्षक कितने वर्षों के कार्यकाल के लिए पद धारण करता है?",
        "options": {
            "A": {"en": "6 years or age 65, whichever is earlier", "hi": "6 वर्ष या 65 वर्ष की आयु, जो पहले हो"},
            "B": {"en": "5 years", "hi": "5 वर्ष"},
            "C": {"en": "6 years", "hi": "6 वर्ष"},
            "D": {"en": "5 years or age 65", "hi": "5 वर्ष या 65 वर्ष की आयु"},
        },
        "correct": "A",
        "explanation_en": "The CAG holds office for a term of 6 years or until he attains the age of 65 years, whichever is earlier.",
        "explanation_hi": "नियंत्रक और महालेखा परीक्षक 6 वर्ष या 65 वर्ष की आयु प्राप्त करने तक, जो पहले हो, पद धारण करता है।",
        "reference": "Article 148, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "UPSC",
        "type": "mcq_single",
        "question_en": "The Chairman and members of UPSC are appointed by:",
        "question_hi": "संघ लोक सेवा आयोग के अध्यक्ष और सदस्यों की नियुक्ति किसके द्वारा की जाती है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Prime Minister", "hi": "प्रधानमंत्री"},
            "C": {"en": "The Parliament", "hi": "संसद"},
            "D": {"en": "The President on advice of PM", "hi": "राष्ट्रपति प्रधानमंत्री की सलाह पर"},
        },
        "correct": "A",
        "explanation_en": "Article 316 provides that the Chairman and other members of a Public Service Commission shall be appointed by the President.",
        "explanation_hi": "अनुच्छेद 316 के अनुसार, लोक सेवा आयोग के अध्यक्ष और अन्य सदस्यों की नियुक्ति राष्ट्रपति द्वारा की जाएगी।",
        "reference": "Article 316, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "National Commission for SCs",
        "type": "mcq_single",
        "question_en": "The National Commission for Scheduled Castes is constituted under Article:",
        "question_hi": "अनुसूचित जातियों के लिए राष्ट्रीय आयोग किस अनुच्छेद के तहत गठित किया गया है?",
        "options": {
            "A": {"en": "338", "hi": "338"},
            "B": {"en": "338A", "hi": "338ए"},
            "C": {"en": "338B", "hi": "338बी"},
            "D": {"en": "339", "hi": "339"},
        },
        "correct": "A",
        "explanation_en": "Article 338 provides for the National Commission for Scheduled Castes.",
        "explanation_hi": "अनुच्छेद 338 अनुसूचित जातियों के लिए राष्ट्रीय आयोग का प्रावधान करता है।",
        "reference": "Article 338, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "National Commission for STs",
        "type": "mcq_single",
        "question_en": "The National Commission for Scheduled Tribes is constituted under Article:",
        "question_hi": "अनुसूचित जनजातियों के लिए राष्ट्रीय आयोग किस अनुच्छेद के तहत गठित किया गया है?",
        "options": {
            "A": {"en": "338A", "hi": "338ए"},
            "B": {"en": "338", "hi": "338"},
            "C": {"en": "338B", "hi": "338बी"},
            "D": {"en": "339", "hi": "339"},
        },
        "correct": "A",
        "explanation_en": "Article 338A provides for the National Commission for Scheduled Tribes.",
        "explanation_hi": "अनुच्छेद 338ए अनुसूचित जनजातियों के लिए राष्ट्रीय आयोग का प्रावधान करता है।",
        "reference": "Article 338A, Constitution of India",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Constitutional bodies",
        "type": "mcq_multi",
        "question_en": "Which of the following are Constitutional bodies?",
        "question_hi": "निम्नलिखित में से कौन सी संवैधानिक निकाय हैं?",
        "options": {
            "A": {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            "B": {"en": "UPSC", "hi": "संघ लोक सेवा आयोग"},
            "C": {"en": "CAG", "hi": "नियंत्रक और महालेखा परीक्षक"},
            "D": {"en": "NITI Aayog", "hi": "नीति आयोग"},
            "E": {"en": "Finance Commission", "hi": "वित्त आयोग"},
        },
        "correct": "ABCE",
        "explanation_en": "Election Commission, UPSC, CAG and Finance Commission are Constitutional bodies. NITI Aayog is a non-constitutional body.",
        "explanation_hi": "निर्वाचन आयोग, संघ लोक सेवा आयोग, नियंत्रक और महालेखा परीक्षक और वित्त आयोग संवैधानिक निकाय हैं। नीति आयोग एक गैर-संवैधानिक निकाय है।",
        "reference": "Articles 324, 315, 148, 280",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Constitutional bodies",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "The Election Commission is a Constitutional body.",
        "assertion_hi": "निर्वाचन आयोग एक संवैधानिक निकाय है।",
        "reason_en": "Article 324 of the Constitution provides for the Election Commission.",
        "reason_hi": "संविधान का अनुच्छेद 324 निर्वाचन आयोग का प्रावधान करता है।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — the Election Commission is established under Article 324.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — निर्वाचन आयोग अनुच्छेद 324 के तहत स्थापित है।",
        "reference": "Article 324, Constitution of India",
    },
    # ---- matching ----
    {
        "chapter": CH, "subtopic": "Bodies",
        "type": "matching",
        "question_en": None,
        "question_hi": None,
        "column1": [
            {"en": "Article 324", "hi": "अनुच्छेद 324"},
            {"en": "Article 148", "hi": "अनुच्छेद 148"},
            {"en": "Article 315", "hi": "अनुच्छेद 315"},
            {"en": "Article 338", "hi": "अनुच्छेद 338"},
        ],
        "column2": [
            {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            {"en": "CAG", "hi": "नियंत्रक और महालेखा परीक्षक"},
            {"en": "UPSC", "hi": "संघ लोक सेवा आयोग"},
            {"en": "National Commission for SCs", "hi": "अनुसूचित जातियों के लिए राष्ट्रीय आयोग"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch24 prepared: {len(NEW_QUESTIONS)} questions")
