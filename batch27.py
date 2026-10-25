# Batch 27: Elections; Landmark Judgments; UP-specific Polity; Historical background; Fundamental Rights; Parliament (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Elections   (need +23 -> 25)
# =====================================================================
CH = "Elections"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Election Commission",
        "type": "mcq_single",
        "question_en": "The superintendence, direction and control of elections is vested in:",
        "question_hi": "चुनावों का अधीक्षण, निर्देशन और नियंत्रण किसमें निहित है?",
        "options": {
            "A": {"en": "Election Commission", "hi": "निर्वाचन आयोग"},
            "B": {"en": "Parliament", "hi": "संसद"},
            "C": {"en": "President", "hi": "राष्ट्रपति"},
            "D": {"en": "Supreme Court", "hi": "उच्चतम न्यायालय"},
        },
        "correct": "A",
        "explanation_en": "Article 324 provides that the superintendence, direction and control of the preparation of electoral rolls and the conduct of all elections shall be vested in the Election Commission.",
        "explanation_hi": "अनुच्छेद 324 के अनुसार, चुनावी नामावलियों के तैयार करने और सभी चुनावों के संचालन का अधीक्षण, निर्देशन और नियंत्रण निर्वाचन आयोग में निहित होगा।",
        "reference": "Article 324, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Adult suffrage",
        "type": "mcq_single",
        "question_en": "Elections to the Lok Sabha and State Legislative Assemblies are on the basis of:",
        "question_hi": "लोकसभा और राज्य विधान सभाओं के चुनाव किस आधार पर होते हैं?",
        "options": {
            "A": {"en": "Adult suffrage", "hi": "वयस्क मताधिकार"},
            "B": {"en": "Property qualification", "hi": "संपत्ति योग्यता"},
            "C": {"en": "Education qualification", "hi": "शिक्षा योग्यता"},
            "D": {"en": "Tax payment", "hi": "कर भुगतान"},
        },
        "correct": "A",
        "explanation_en": "Article 326 provides that elections to the House of the People and to the Legislative Assemblies of States shall be on the basis of adult suffrage.",
        "explanation_hi": "अनुच्छेद 326 के अनुसार, लोकसभा और राज्यों की विधान सभाओं के चुनाव वयस्क मताधिकार के आधार पर होंगे।",
        "reference": "Article 326, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Adult suffrage",
        "type": "mcq_single",
        "question_en": "The voting age was reduced from 21 to 18 years by the:",
        "question_hi": "मतदान की आयु 21 से घटाकर 18 वर्ष किसके द्वारा की गई?",
        "options": {
            "A": {"en": "61st Amendment", "hi": "61वां संशोधन"},
            "B": {"en": "42nd Amendment", "hi": "42वां संशोधन"},
            "C": {"en": "44th Amendment", "hi": "44वां संशोधन"},
            "D": {"en": "61st Amendment", "hi": "61वां संशोधन"},
        },
        "correct": "A",
        "explanation_en": "The 61st Constitutional Amendment Act, 1988 amended Article 326 to reduce the voting age from 21 to 18 years.",
        "explanation_hi": "61वें संवैधानिक संशोधन अधिनियम, 1988 ने अनुच्छेद 326 में संशोधन करके मतदान की आयु 21 से घटाकर 18 वर्ष कर दी।",
        "reference": "61st Constitutional Amendment, 1988",
    },
    {
        "chapter": CH, "subtopic": "Bar to courts",
        "type": "mcq_single",
        "question_en": "No election to any House shall be called in question except by an election petition under Article:",
        "question_hi": "किसी भी सदन का कोई भी चुनाव केवल चुनाव याचिका द्वारा चुनौती दी जा सकती है अनुच्छेद के तहत:",
        "options": {
            "A": {"en": "329", "hi": "329"},
            "B": {"en": "324", "hi": "324"},
            "C": {"en": "326", "hi": "326"},
            "D": {"en": "327", "hi": "327"},
        },
        "correct": "A",
        "explanation_en": "Article 329 provides that no election to either House of Parliament or to the House or either House of the Legislature of a State shall be called in question except by an election petition.",
        "explanation_hi": "अनुच्छेद 329 के अनुसार, संसद के किसी भी सदन या राज्य के विधानमंडल के किसी भी सदन के चुनाव को केवल एक चुनाव याचिका द्वारा चुनौती दी जा सकती है।",
        "reference": "Article 329, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Parliament power",
        "type": "mcq_single",
        "question_en": "Parliament may make laws with respect to elections to Legislatures under Article:",
        "question_hi": "संसद विधानमंडलों के चुनावों के संबंध में कानून बना सकती है अनुच्छेद के तहत:",
        "options": {
            "A": {"en": "327", "hi": "327"},
            "B": {"en": "328", "hi": "328"},
            "C": {"en": "324", "hi": "324"},
            "D": {"en": "329", "hi": "329"},
        },
        "correct": "A",
        "explanation_en": "Article 327 empowers Parliament to make provisions with respect to all matters relating to elections to either House of Parliament or to the House or either House of the Legislature of a State.",
        "explanation_hi": "अनुच्छेद 327 संसद को संसद के किसी भी सदन या राज्य के विधानमंडल के किसी भी सदन या दोनों सदनों के चुनावों से संबंधित सभी मामलों के संबंध में प्रावधान करने का अधिकार देता है।",
        "reference": "Article 327, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "NOTA",
        "type": "mcq_single",
        "question_en": "The NOTA (None of the Above) option was introduced by the Supreme Court in:",
        "question_hi": "NOTA (उपरोक्त में से कोई नहीं) विकल्प सर्वोच्च न्यायालय द्वारा किस वर्ष शुरू किया गया?",
        "options": {
            "A": {"en": "2013", "hi": "2013"},
            "B": {"en": "2014", "hi": "2014"},
            "C": {"en": "2015", "hi": "2015"},
            "D": {"en": "2012", "hi": "2012"},
        },
        "correct": "A",
        "explanation_en": "The Supreme Court in PUCL v. Union of India (2013) directed the Election Commission to provide the NOTA option in EVMs.",
        "explanation_hi": "सर्वोच्च न्यायालय ने पीयूसीएल बनाम भारत संघ (2013) में निर्वाचन आयोग को ईवीएम में नोटा विकल्प प्रदान करने का निर्देश दिया।",
        "reference": "PUCL v. Union of India (2013)",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Articles",
        "type": "mcq_multi",
        "question_en": "Which of the following Articles deal with elections?",
        "question_hi": "निम्नलिखित में से कौन से अनुच्छेद चुनावों से संबंधित हैं?",
        "options": {
            "A": {"en": "324", "hi": "324"},
            "B": {"en": "325", "hi": "325"},
            "C": {"en": "326", "hi": "326"},
            "D": {"en": "327", "hi": "327"},
            "E": {"en": "352", "hi": "352"},
        },
        "correct": "ABCD",
        "explanation_en": "Articles 324, 325, 326 and 327 deal with elections. Article 352 deals with National Emergency.",
        "explanation_hi": "अनुच्छेद 324, 325, 326 और 327 चुनावों से संबंधित हैं। अनुच्छेद 352 राष्ट्रीय आपातकाल से संबंधित है।",
        "reference": "Articles 324-327, Constitution of India",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Adult suffrage",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "Elections to the Lok Sabha and State Legislative Assemblies are held on the basis of adult suffrage.",
        "assertion_hi": "लोकसभा और राज्य विधान सभाओं के चुनाव वयस्क मताधिकार के आधार पर होते हैं।",
        "reason_en": "Article 326 provides that elections to the House of the People and to the Legislative Assemblies of States shall be on the basis of adult suffrage.",
        "reason_hi": "अनुच्छेद 326 के अनुसार, लोक सभा और राज्यों की विधान सभाओं के चुनाव वयस्क मताधिकार के आधार पर होंगे।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — Article 326 provides for adult suffrage.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — अनुच्छेद 326 वयस्क मताधिकार का प्रावधान करता है।",
        "reference": "Article 326, Constitution of India",
    },
    # ---- matching ----
    {
        "chapter": CH, "subtopic": "Articles",
        "type": "matching",
        "question_en": None,
        "question_hi": None,
        "column1": [
            {"en": "Article 324", "hi": "अनुच्छेद 324"},
            {"en": "Article 325", "hi": "अनुच्छेद 325"},
            {"en": "Article 326", "hi": "अनुच्छेद 326"},
            {"en": "Article 329", "hi": "अनुच्छेद 329"},
        ],
        "column2": [
            {"en": "Superintendence of elections", "hi": "चुनावों का अधीक्षण"},
            {"en": "No discrimination on grounds of religion, race, caste, sex", "hi": "धर्म, जाति, लिंग के आधार पर कोई भेदभाव नहीं"},
            {"en": "Adult suffrage", "hi": "वयस्क मताधिकार"},
            {"en": "Bar to courts in electoral matters", "hi": "चुनावी मामलों में अदालतों पर रोक"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch27 prepared: {len(NEW_QUESTIONS)} questions")
