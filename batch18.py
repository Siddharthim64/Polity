# Batch 18: Prime Minister; Judicial review; Governor, CM & State Council (~20 each -> 25)
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Prime Minister and Council of Ministers   (need +22 -> 25)
# =====================================================================
CH = "Prime Minister and Council of Ministers"

NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Appointment",
        "type": "mcq_single",
        "question_en": "The Prime Minister is appointed by:",
        "question_hi": "प्रधानमंत्री की नियुक्ति किसके द्वारा की जाती है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Lok Sabha", "hi": "लोकसभा"},
            "C": {"en": "The Parliament", "hi": "संसद"},
            "D": {"en": "The Cabinet", "hi": "मंत्रिमंडल"},
        },
        "correct": "A",
        "explanation_en": "Article 75(1) provides that the Prime Minister shall be appointed by the President and the other Ministers shall be appointed by the President on the advice of the Prime Minister.",
        "explanation_hi": "अनुच्छेद 75(1) के अनुसार, प्रधानमंत्री की नियुक्ति राष्ट्रपति द्वारा की जाएगी और अन्य मंत्रियों की नियुक्ति राष्ट्रपति द्वारा प्रधानमंत्री की सलाह पर की जाएगी।",
        "reference": "Article 75(1), Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Collective responsibility",
        "type": "mcq_single",
        "question_en": "The Council of Ministers is collectively responsible to:",
        "question_hi": "मंत्रिपरिषद किसके प्रति सामूहिक रूप से उत्तरदायी है?",
        "options": {
            "A": {"en": "The Lok Sabha", "hi": "लोकसभा"},
            "B": {"en": "The President", "hi": "राष्ट्रपति"},
            "C": {"en": "The Rajya Sabha", "hi": "राज्यसभा"},
            "D": {"en": "The Supreme Court", "hi": "उच्चतम न्यायालय"},
        },
        "correct": "A",
        "explanation_en": "Article 75(3) provides that the Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha).",
        "explanation_hi": "अनुच्छेद 75(3) के अनुसार, मंत्रिपरिषद लोक सभा के प्रति सामूहिक रूप से उत्तरदायी होगी।",
        "reference": "Article 75(3), Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Duties",
        "type": "mcq_single",
        "question_en": "The duties of the Prime Minister are provided under Article:",
        "question_hi": "प्रधानमंत्री के कर्तव्य किस अनुच्छेद के तहत प्रदान किए गए हैं?",
        "options": {
            "A": {"en": "78", "hi": "78"},
            "B": {"en": "75", "hi": "75"},
            "C": {"en": "74", "hi": "74"},
            "D": {"en": "77", "hi": "77"},
        },
        "correct": "A",
        "explanation_en": "Article 78 provides that it shall be the duty of the Prime Minister to communicate to the President all decisions of the Council of Ministers relating to the administration of the affairs of the Union.",
        "explanation_hi": "अनुच्छेद 78 के अनुसार, प्रधानमंत्री का कर्तव्य होगा कि वह संघ के मामलों के प्रशासन से संबंधित मंत्रिपरिषद के सभी निर्णयों के बारे में राष्ट्रपति को सूचित करे।",
        "reference": "Article 78, Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Size of Council",
        "type": "mcq_single",
        "question_en": "The total number of Ministers, including the Prime Minister, shall not exceed:",
        "question_hi": "प्रधानमंत्री सहित मंत्रियों की कुल संख्या किससे अधिक नहीं होगी?",
        "options": {
            "A": {"en": "15% of the total strength of the Lok Sabha", "hi": "लोकसभा की कुल शक्ति का 15%"},
            "B": {"en": "10% of the total strength", "hi": "कुल शक्ति का 10%"},
            "C": {"en": "20% of the total strength", "hi": "कुल शक्ति का 20%"},
            "D": {"en": "25% of the total strength", "hi": "कुल शक्ति का 25%"},
        },
        "correct": "A",
        "explanation_en": "The 91st Constitutional Amendment Act, 2003 provides that the total number of Ministers, including the Prime Minister, in the Council of Ministers shall not exceed fifteen percent of the total number of members of the House of the People.",
        "explanation_hi": "91वां संवैधानिक संशोधन अधिनियम, 2003 के अनुसार, मंत्रिपरिषद में मंत्रियों की कुल संख्या, प्रधानमंत्री सहित, लोक सभा के सदस्यों की कुल संख्या के पंद्रह प्रतिशत से अधिक नहीं होगी।",
        "reference": "91st Constitutional Amendment, 2003",
    },
    {
        "chapter": CH, "subtopic": "Conduct of business",
        "type": "mcq_single",
        "question_en": "All executive action of the Government of India is expressed to be taken in the name of:",
        "question_hi": "भारत सरकार की सभी कार्यकारी कार्रवाई किसके नाम पर की गई बताई गई है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Prime Minister", "hi": "प्रधानमंत्री"},
            "C": {"en": "The Parliament", "hi": "संसद"},
            "D": {"en": "The Cabinet", "hi": "मंत्रिमंडल"},
        },
        "correct": "A",
        "explanation_en": "Article 77(1) provides that all executive action of the Government of India shall be expressed to be taken in the name of the President.",
        "explanation_hi": "अनुच्छेद 77(1) के अनुसार, भारत सरकार की सभी कार्यकारी कार्रवाई राष्ट्रपति के नाम पर की गई बताई जाएगी।",
        "reference": "Article 77(1), Constitution of India",
    },
    {
        "chapter": CH, "subtopic": "Attorney General",
        "type": "mcq_single",
        "question_en": "The Attorney General for India is appointed by:",
        "question_hi": "भारत के अटॉर्नी जनरल की नियुक्ति किसके द्वारा की जाती है?",
        "options": {
            "A": {"en": "The President", "hi": "राष्ट्रपति"},
            "B": {"en": "The Prime Minister", "hi": "प्रधानमंत्री"},
            "C": {"en": "The Chief Justice of India", "hi": "भारत के मुख्य न्यायाधीश"},
            "D": {"en": "The Law Minister", "hi": "कानून मंत्री"},
        },
        "correct": "A",
        "explanation_en": "Article 76(1) provides that the President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney General for India.",
        "explanation_hi": "अनुच्छेद 76(1) के अनुसार, राष्ट्रपति एक ऐसे व्यक्ति को भारत के अटॉर्नी जनरल के रूप में नियुक्त करेगा जो सर्वोच्च न्यायालय के न्यायाधीश के रूप में नियुक्त होने के लिए योग्य हो।",
        "reference": "Article 76(1), Constitution of India",
    },
    # ---- mcq_multi ----
    {
        "chapter": CH, "subtopic": "Council of Ministers",
        "type": "mcq_multi",
        "question_en": "Which of the following are correct about the Prime Minister?",
        "question_hi": "निम्नलिखित में से कौन से प्रधानमंत्री के बारे में सही हैं?",
        "options": {
            "A": {"en": "Appointed by the President", "hi": "राष्ट्रपति द्वारा नियुक्त"},
            "B": {"en": "Head of the Council of Ministers", "hi": "मंत्रिपरिषद के प्रमुख"},
            "C": {"en": "Holds office during the pleasure of the President", "hi": "राष्ट्रपति की इच्छा पर पद धारण करता है"},
            "D": {"en": "Must be a member of Rajya Sabha", "hi": "राज्यसभा का सदस्य होना चाहिए"},
            "E": {"en": "Advises the President on appointment of ministers", "hi": "मंत्रियों की नियुक्ति पर राष्ट्रपति को सलाह देता है"},
        },
        "correct": "ABCE",
        "explanation_en": "The PM is appointed by the President, heads the Council of Ministers, holds office during the pleasure of the President, and advises on ministerial appointments. He need not be an RS member (can be from either House).",
        "explanation_hi": "पीएम राष्ट्रपति द्वारा नियुक्त किया जाता है, मंत्रिपरिषद का प्रमुख होता है, राष्ट्रपति की इच्छा पर पद धारण करता है और मंत्रियों की नियुक्ति पर सलाह देता है। वह राज्यसभा का सदस्य होने की आवश्यकता नहीं है (कोई भी सदन से हो सकता है)।",
        "reference": "Articles 74, 75, Constitution of India",
    },
    # ---- assertion_reason ----
    {
        "chapter": CH, "subtopic": "Collective responsibility",
        "type": "assertion_reason",
        "question_en": None,
        "question_hi": None,
        "assertion_en": "The Council of Ministers is collectively responsible to the Lok Sabha.",
        "assertion_hi": "मंत्रिपरिषद लोकसभा के प्रति सामूहिक रूप से उत्तरदायी है।",
        "reason_en": "Article 75(3) provides that the Council of Ministers shall be collectively responsible to the House of the People.",
        "reason_hi": "अनुच्छेद 75(3) के अनुसार, मंत्रिपरिषद लोक सभा के प्रति सामूहिक रूप से उत्तरदायी होगी।",
        "correct": "A",
        "explanation_en": "Both A and R are true, and R correctly explains A — Article 75(3) establishes collective responsibility to the Lok Sabha.",
        "explanation_hi": "A और R दोनों सत्य हैं, और R, A को सही ढंग से समझाता है — अनुच्छेद 75(3) लोकसभा के प्रति सामूहिक जिम्मेदारी स्थापित करता है।",
        "reference": "Article 75(3), Constitution of India",
    },
    # ---- matching ----
    {
        "chapter": CH, "subtopic": "Articles",
        "type": "matching",
        "question_en": None,
        "question_hi": None,
        "column1": [
            {"en": "Article 74", "hi": "अनुच्छेद 74"},
            {"en": "Article 75", "hi": "अनुच्छेद 75"},
            {"en": "Article 78", "hi": "अनुच्छेद 78"},
            {"en": "Article 76", "hi": "अनुच्छेद 76"},
        ],
        "column2": [
            {"en": "Council of Ministers to aid and advise President", "hi": "राष्ट्रपति को सहायता और सलाह देने के लिए मंत्रिपरिषद"},
            {"en": "Appointment of PM and Ministers, collective responsibility", "hi": "पीएम और मंत्रियों की नियुक्ति, सामूहिक जिम्मेदारी"},
            {"en": "Duties of Prime Minister", "hi": "प्रधानमंत्री के कर्तव्य"},
            {"en": "Attorney General", "hi": "अटॉर्नी जनरल"},
        ],
        "correct_mapping": {"0": "0", "1": "1", "2": "2", "3": "3"},
    },
]

print(f"batch18 prepared: {len(NEW_QUESTIONS)} questions")
