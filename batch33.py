# Batch 33: Additional questions for sections that need more questions to reach 25
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: UP-specific Polity   (need +19 -> 25)
# =====================================================================
CH = "UP-specific Polity"
NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Uttar Pradesh Polity",
        "type": "mcq_single",
        "question_en": "Uttar Pradesh Legislative Assembly has how many seats?",
        "question_hi": "उत्तर प्रदेश विधान सभा में कितनी सीटें हैं?",
        "options": {
            "A": {"en": "403", "hi": "403"},
            "B": {"en": "400", "hi": "400"},
            "C":{"en": "350", "hi":"350"},
            "D":{"en":"500","hi":"500"}
        },
        "correct": "A",
        "explanation_en": "Uttar Pradesh Legislative Assembly has 403 elected members.",
        "explanation_hi":"उत्तर प्रदेश विधान सभा में 403 निर्वाचित सदस्य हैं।",
        "ref":"Uttar Pradesh Legislative Assembly"
    },
    {
        "chapter": CH, "subtopic": "Uttar Pradesh Polity",
        "type": "mcq_single",
        "question_en": "Uttar Pradesh Reorganisation Act created Uttarakhand in:",
        "question_hi": "उत्तर प्रदेश पुनर्गठन अधिनियम ने उत्तराखंड कब बनाया:",
        "options": {
            "A": {"en": "2000", "hi": "2000"},
            "B": {"en": "2001", "hi": "2001"},
            "C":{"en":"1999","hi":"1999"},
            "D":{"en":"2002","hi":"2002"}
        },
        "correct": "A",
        "explanation_en":"Uttar Pradesh Reorganisation Act, 2000 created Uttarakhand on 9 November 2000.",
        "explanation_hi":"उत्तर प्रदेश पुनर्गठन अधिनियम, 2000 ने 9 नवंबर 2000 को उत्तराखंड बनाया।",
        "ref":"Uttar Pradesh Reorganisation Act, 2000"},
    {
        "chapter": CH, "subtopic": "Uttar Pradesh Polity",
        "type": "mcq_single",
        "question_en": "Uttar Pradesh has a bicameral legislature consisting of:",
        "question_hi":"उत्तर प्रदेश में द्विसदनीय विधानमंडल में शामिल हैं:",
        "options":{"A":{"en":"Legislative Assembly and Legislative Council","hi":"विधान सभा और विधान परिषद"},"B":{"en":"Lok Sabha and Rajya Sabha","hi":"लोकसभा और राज्यसभा"},"C":{"en":"Assembly only","hi":"केवल सभा"},"D":{"en":"Council only","hi":"केवल परिषद"}},"correct":"A","explanation_en":"Uttar Pradesh has a bicameral legislature with Legislative Assembly (403 members) and Legislative Council (100 members).","explanation_hi":"उत्तर प्रदेश में द्विसदनीय विधानमंडल है जिसमें विधान सभा (403 सदस्य) और विधान परिषद (100 सदस्य) शामिल हैं।","reference":"UP Legislature"},{"chapter":CH,"subtopic":"High Court","type":"mcq_single","question_en":"The highest court in Uttar Pradesh is:","question_hi":"उत्तर प्रदेश का उच्चतम न्यायालय है:","options":{"A":{"en":"Allahabad High Court","hi":"इलाहाबाद उच्च न्यायालय"},"B":{"en":"Lucknow High Court","hi":"लखनऊ उच्च न्यायालय"},"C":{"en":"Supreme Court","hi":"उच्चतम न्यायालय"},"D":{"en":"District Court","hi":"जिला न्यायालय"}},"correct":"A","explanation_en":"The Allahabad High Court is the highest court in Uttar Pradesh.","explanation_hi":"इलाहाबाद उच्च न्यायालय उत्तर प्रदेश का उच्चतम न्यायालय है।","reference":"Allahabad High Court"},{"chapter":CH,"subtopic":"Uttarakhand","type":"mcq_single","question_en":"Uttarakhand Legislative Assembly has how many seats:","question_hi":"उत्तराखंड विधान सभा में कितनी सीटें हैं:","options":{"A":{"en":"70","hi":"70"},"B":{"en":"60","hi":"60"},"C":{"en":"80","hi":"80"},"D":{"en":"100","hi":"100"}},"correct":"A","explanation_en":"The Uttarakhand Legislative Assembly has 70 elected members.","explanation_hi":"उत्तराखंड विधान सभा में 70 निर्वाचित सदस्य हैं।","reference":"Uttarakhand Legislative Assembly"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"Who is the head of the state government in Uttar Pradesh?","question_hi":"उत्तर प्रदेश की राज्य सरकार का प्रमुख कौन है:","options":{"A":{"en":"Governor","hi":"राज्यपाल"},"B":{"en":"Chief Minister","hi":"मुख्यमंत्री"},"C":{"en":"Chief Secretary","hi":"मुख्य सचिव"},"D":{"en":"President","hi":"राष्ट्रपति"}},"correct":"B","explanation_en":"The Chief Minister is the head of the state government in Uttar Pradesh.","explanation_hi":"उत्तर प्रदेश की राज्य सरकार के प्रमुख मुख्यमंत्री हैं।","reference":"UP Polity"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"Which of the following is NOT a division of Uttar Pradesh?","question_hi":"निम्नलिखित में से कौन सा उत्तर प्रदेश का मंडल नहीं है:","options":{"A":{"en":"Lucknow","hi":"लखनऊ"},"B":{"en":"Varanasi","hi":"वाराणसी"},"C":{"en":"Prayagraj","hi":"प्रयागराज"},"D":{"en":"Jaipur","hi":"जयपुर"}},"correct":"D","explanation_en":"Jaipur is in Rajasthan, not Uttar Pradesh.","explanation_hi":"जयपुर राजस्थान में है, उत्तर प्रदेश में नहीं।","reference":"UP Geography"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"The High Court of Uttarakhand is located at:","question_hi":"उत्तराखंड उच्च न्यायालय कहां स्थित है:","options":{"A":{"en":"Nainital","hi":"नैनीताल"},"B":{"en":"Dehradun","hi":"देहरादून"},"C":{"en":"Haridwar","hi":"हरिद्वार"},"D":{"en":"Rishikesh","hi":"ऋषिकेश"}},"correct":"A","explanation_en":"The Uttarakhand High Court is located at Nainital.","explanation_hi":"उत्तराखंड उच्च न्यायालय नैनीताल में स्थित है।","reference":"Uttarakhand High Court"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"Which of the following is NOT a district of Uttar Pradesh?","question_hi":"निम्नलिखित में से कौन सा उत्तर प्रदेश का जिला नहीं है:","options":{"A":{"en":"Lucknow","hi":"लखनऊ"},"B":{"en":"Kanpur","hi":"कानपुर"},"C":{"en":"Jaipur","hi":"जयपुर"},"D":{"en":"Varanasi","hi":"वाराणसी"}},"correct":"C","explanation_en":"Jaipur is in Rajasthan, not Uttar Pradesh.","explanation_hi":"जयपुर राजस्थान में है, उत्तर प्रदेश में नहीं।","reference":"UP Geography"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"The first Chief Minister of Uttar Pradesh was:","question_hi":"उत्तर प्रदेश के पहले मुख्यमंत्री थे:","options":{"A":{"en":"Govind Ballabh Pant","hi":"गोविंद बल्लभ पंत"},"B":{"en":"Jawaharlal Nehru","hi":"जवाहरलाल नेहरू"},"C":{"en":"Sardar Patel","hi":"सरदार पटेल"},"D":{"en":"Dr. Rajendra Prasad","hi":"डॉ. राजेंद्र प्रसाद"}},"correct":"A","explanation_en":"Govind Ballabh Pant was the first Chief Minister of Uttar Pradesh.","explanation_hi":"गोविंद बल्लभ पंत उत्तर प्रदेश के पहले मुख्यमंत्री थे।","reference":"UP Polity"},{"chapter":CH,"subtopic":"Uttar Pradesh Polity","type":"mcq_single","question_en":"Which of the following is NOT a division of Uttar Pradesh?","question_hi":"निम्नलिखित में से कौन सा उत्तर प्रदेश का मंडल नहीं है:","options":{"A":{"en":"Lucknow","hi":"लखनऊ"},"B":{"en":"Agra","hi":"आगरा"},"C":{"en":"Jaipur","hi":"जयपुर"},"D":{"en":"Gorakhpur","hi":"गोरखपुर"}},"correct":"C","explanation_en":"Jaipur is in Rajasthan, not Uttar Pradesh.","explanation_hi":"जयपुर राजस्थान में है, उत्तर प्रदेश में नहीं।","reference":"UP Geography"}]
print(f"batch33 part 1 prepared: {len(NEW_QUESTIONS)} questions")
