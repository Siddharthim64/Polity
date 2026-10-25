# Batch 23: Constitutional bodies; Cooperative societies; Statutory bodies; Elections; Landmark Judgments (~18 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Constitutional bodies   (need +19 -> 25)
# =====================================================================
CH = "Constitutional bodies"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Election Commission",
        "type": "mcq_single",
        "question_en": "The Election Commission of India is constituted under Article:",
        "question_hi": "भारत के निर्वाचन आयोग का गठन किस अनुच्छेद के तहत किया गया है?",
        "options": {
            "A": {"en": "324", "hi": "324"},
            "B": {"en": "325", "hi": "325"},
            "C": {"en": "326", "hi": "326"},
            "D": {"en": "327", "hi": "327"},
        },
        "correct": "A",
        "explanation_en": "Article 324 provides that the superintendence, direction and control of the preparation of electoral rolls and the conduct of all elections shall be vested in the Election Commission.",
        "explanation_hi": "अनुच्छेद 324 के अनुसार, चुनावी नामावलियों के तैयार करने और सभी चुनावों के संचालन का अधीक्षण, निर्देशन और नियंत्रण निर्वाचन आयोग में निहित होगा।",
        "reference": "Article 324, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Election Commission",
        "type": "mcq_single",
        "question_en": "The Chief Election Commissioner and other Election Commissioners are appointed by:",
        "question_hi": "मुख्य निर्वाचन आयुक्त और अन्य निर्वाचन आयुक्तों की नियुक्ति किसके द्वारा की जाती है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Prime Minister", "hi": "प्रधानमंत्री"},
            "C": {"en": "The Parliament", "hi": "संसद"},
            "D": {"en": "The Law Minister", "hi": "कानून मंत्री"},
        },
        "correct": "A",
        "explanation_en": "Article 324(2) provides that the Election Commission shall consist of the Chief Election Commissioner and such number of other Election Commissioners as the President may from time to time fix.",
        "explanation_hi": "अनुच्छेद 324(2) के अनुसार, निर्वाचन आयोग में मुख्य निर्वाचन आयुक्त और राष्ट्रपति द्वारा समय-समय पर निर्धारित अन्य निर्वाचन आयुक्त शामिल होंगे।",
        "reference": "Article 324(2), Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "CAG",
        "type": "mcq_single",
        "question_en": "The Comptroller and Auditor General of India is appointed by:",
        "question_hi": "भारत के नियंत्रक और महालेखा परीक्षक की नियुक्ति किसके द्वारा की जाती है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Prime Minister", "hi": "प्रधानमंत्री"},
            "C": {"en": "The Finance Minister", "hi": "वित्त मंत्री"},
            "D": {"en": "The Supreme Court", "hi": "उच्चतम न्यायालय"},
        },
        "correct": "A",
        "explanation_en": "Article 148 provides that there shall be a Comptroller and Auditor General of India who shall be appointed by the President.",
        "explanation_hi": "अनुच्छेद 148 के अनुसार, भारत का एक नियंत्रक और महालेखा परीक्षक होगा जिसकी नियुक्ति राष्ट्रपति द्वारा की जाएगी।",
        "reference": "Article 148, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "UPSC",
        "type": "mcq_single",
        "question_en": "The Union Public Service Commission is established under Article:",
        "question_hi": "संघ लोक सेवा आयोग की स्थापना किस अनुच्छेद के तहत की गई है?",
        "options": {
            "A": {"en": "315", "hi": "315"},
            "B": {"en": "324", "hi": "324"},
            "C": {"en": "148", "hi": "148"},
            "D": {"en": "338", "hi": "338"},
        },
        "correct": "A",
        "explanation_en": "Article 315 provides that there shall be a Public Service Commission for the Union and a Public Service Commission for each State.",
        "explanation_hi": "अनुच्छेद 315 के अनुसार, संघ के लिए और प्रत्येक राज्य के लिए एक लोक सेवा आयोग होगा।",
        "reference": "Article 315, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Finance Commission",
        "type": "mcq_single",
        "question_en": "The Finance Commission is constituted under Article:",
        "question_hi": "वित्त आयोग का गठन किस अनुच्छेद के तहत किया जाता है?",
        "options": {
            "A": {"en": "280", "hi": "280"},
            "B": {"en": "275", "hi": "275"},
            "C": {"en": "270", "hi": "270"},
            "D": {"en": "324", "hi": "324"},
        },
        "correct": "A",
        "explanation_en": "Article 280 provides for the constitution of a Finance Commission by the President.",
        "explanation_hi": "अनुच्छेद 280 राष्ट्रपति द्वारा एक वित्त आयोग के गठन का प्रावधान करता है।",
        "reference": "Article 280, Constitution of India",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Constitutional bodies",
        "type": "mcq_multi",
        "question_en": "Which of the following are Constitutional bodies?",
        "question_hi": "निम्नलिखित में से कौन सी संवैधानिक निकाय हैं?",
        "options": {
            "A": {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            "B": {"en": "Union Public Service Commission", "hi": "संघ लोक सेवा आयोग"},
            "C": {"en": "Comptroller and Auditor General", "hi": "नियंत्रक और महालेखा परीक्षक"},
            "D": {"en": "NITI Aayog", "hi": "नीति आयोग"},
            "E": {"en": "Finance Commission", "hi": "वित्त आयोग"},
        },
        "correct": "ABCE",
        "explanation_en": "Election Commission, UPSC, CAG and Finance Commission are Constitutional bodies. NITI Aayog is a non-constitutional (extra-constitutional) body.",
        "explanation_hi": "निर्वाचन आयोग, संघ लोक सेवा आयोग, नियंत्रक और महालेखा परीक्षक और वित्त आयोग संवैधानिक निकाय हैं। नीति आयोग एक गैर-संवैधानिक निकाय है।",
        "reference": "Articles 324, 315, 148, 280",
    },
    {
        "chapter": CH, "subtopic": "Commissions",
        "type": "mcq_multi",
        "question_en": "Which of the following are Constitutional commissions?",
        "question_hi": "निम्नलिखित में से कौन से संवैधानिक आयोग हैं?",
        "options": {
            "A": {"en": "National Commission for Scheduled Castes", "hi": "अनुसूचित जातियों के लिए राष्ट्रीय आयोग"},
            "B": {"en": "National Commission for Scheduled Tribes", "hi": "अनुसूचित जनजातियों के लिए राष्ट्रीय आयोग"},
            "C": {"en": "National Commission for Backward Classes", "hi": "पिछड़े वर्गों के लिए राष्ट्रीय आयोग"},
            "D": {"en": "National Human Rights Commission", "hi": "राष्ट्रीय मानवाधिकार आयोग"},
            "E": {"en": "National Commission for Women", "hi": "महिलाओं के लिए राष्ट्रीय आयोग"},
        },
        "correct": "ABC",
        "explanation_en": "National Commission for SCs (Art 338), STs (Art 338A) and BCs (Art 338B, 102nd Amendment) are Constitutional commissions. NHRC and NCW are statutory bodies.",
        "explanation_hi": "अनुसूचित जातियों के लिए राष्ट्रीय आयोग (अनुच्छेद 338), अनुसूचित जनजातियों के लिए राष्ट्रीय आयोग (अनुच्छेद 338ए) और पिछड़े वर्गों के लिए राष्ट्रीय आयोग (अनुच्छेद 338बी, 102वां संशोधन) संवैधानिक आयोग हैं। एनएचआरसी और एनसीडब्ल्यू सांविधिक निकाय हैं।",
        "reference": "Articles 338, 338A, 338B",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Election Commission",
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
            {"en": "Article 280", "hi": "अनुच्छेद 280"},
        ],
        "column2": [
            {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            {"en": "CAG", "hi": "नियंत्रक और महालेखा परीक्षक"},
            {"en": "UPSC", "hi": "संघ लोक सेवा आयोग"},
            {"en": "Finance Commission", "hi": "वित्त आयोग"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch23 prepared: {len(NEW_QUESTIONS)} questions")
