# Batch 34: More questions for sections that need them
NEW_QUESTIONS = []

# =====================================================================
# CHAPTER: Elections, electoral reforms, and representation   (need +12 -> 25)
# =====================================================================
CH = "Elections, electoral reforms, and representation"
NEW_QUESTIONS += [
    {
        "chapter": CH, "subtopic": "Elections",
        "type": "mcq_single",
        "question_en": "Elections to Lok Sabha are held on the basis of:",
        "question_hi": "लोकसभा के चुनाव किस आधार पर होते हैं:",
        "options": {
            "A": {"en": "Adult suffrage", "hi": "वयस्क मताधिकार"},
            "B": {"en": "Property qualification", "hi": "संपत्ति योग्यता"},
            "C": {"en": "Education qualification", "hi": "शिक्षा योग्यता"},
            "D": {"en": "Tax payment", "hi": "कर भुगतान"}
        },
        "correct": "A",
        "explanation_en":"Article 326 provides that elections to House of People shall be on basis of adult suffrage.",
        "explanation_hi":"अनुच्छेद 326 के अनुसार लोकसभा के चुनाव वयस्क मताधिकार के आधार पर होंगे।",
        "ref":"Article 326, Constitution of India"
    },
    {
        "chapter": CH, "subtopic": "Elections",
        "type": "mcq_single",
        "question_en": "The voting age was reduced from 21 to 18 years by:",
        "question_hi":"मतदान की आयु 21 से घटाकर 18 वर्ष किसके द्वारा की गई:",
        "options":{"A":{"en":"61st Amendment","hi":"61वां संशोधन"},"B":{"en":"42nd Amendment","hi":"42वां संशोधन"},"C":{"en":"44th Amendment","hi":"44वां संशोधन"},"D":{"en":"73rd Amendment","hi":"73वां संशोधन"}},"correct":"A","explanation_en":"61st Constitutional Amendment Act, 1988 reduced voting age from 21 to 18 years.","explanation_hi":"61वां संवैधानिक संशोधन अधिनियम, 1988 ने मतदान की आयु 21 से घटाकर 18 वर्ष कर दी।","ref":"61st Constitutional Amendment, 1988"},
    {
        "chapter": CH, "subtopic": "Elections",
        "type": "mcq_single",
        "question_en": "NOTA (None of the Above) option was introduced by:",
        "question_hi":"NOTA (उपरोक्त में से कोई नहीं) विकल्प किसने शुरू किया:",
        "options":{"A":{"en":"Supreme Court","hi":"सर्वोच्च न्यायालय"},"B":{"en":"Election Commission","hi":"निर्वाचन आयोग"},"C":{"en":"Parliament","hi":"संसद"},"D":{"en":"President","hi":"राष्ट्रपति"}},"correct":"A","explanation_en":"Supreme Court in PUCL v. Union of India (2013) directed EC to provide NOTA option in EVMs.","explanation_hi":"सर्वोच्च न्यायालय ने पीयूसीएल बनाम भारत संघ (2013) में निर्वाचन आयोग को ईवीएम में नोटा विकल्प प्रदान करने का निर्देश दिया।","ref":"PUCL v. Union of India (2013)"},
    {
        "chapter": CH, "subtopic": "Elections",
        "type": "mcq_single",
        "question_en": "Election Commission is constituted under Article:",
        "question_hi":"निर्वाचन आयोग का गठन किस अनुच्छेद के तहत किया गया है:",
        "options":{"A":{"en":"324","hi":"324"},"B":{"en":"325","hi":"325"},"C":{"en":"326","hi":"326"},"D":{"en":"327","hi":"327"}},"correct":"A","explanation_en":"Article 324 provides superintendence, direction and control of elections shall be vested in Election Commission.","explanation_hi":"अनुच्छेद 324 चुनावी नामावलियों के तैयार करने और सभी चुनावों के संचालन का अधीक्षण निर्वाचन आयोग में निहित होगा।","ref":"Article 324, Constitution of India"},{"chapter":CH,"subtopic":"Elections","type":"mcq_single","question_en":"Adult suffrage means voting right to all citizens above the age of:","question_hi":"वयस्क मताधिकार का अर्थ है सभी नागरिकों को मतदान का अधिकार जिनकी आयु ऊपर है:","options":{"A":{"en":"18 years","hi":"18 वर्ष"},"B":{"en":"21 years","hi":"21 वर्ष"},"C":{"en":"25 years","hi":"25 वर्ष"},"D":{"en":"30 years","hi":"30 वर्ष"}},"correct":"A","explanation_en":"Article 326 provides adult suffrage i.e. right to vote to all citizens above 18 years of age.","explanation_hi":"अनुच्छेद 326 वयस्क मताधिकार का प्रावधान करता है i.e. 18 वर्ष से अधिक आयु के सभी नागरिकों को मतदान का अधिकार।","ref":"Article 326, Constitution of India"},{"chapter":CH,"subtopic":"Elections","type":"mcq_multi","question_en":"Which of the following Articles deal with elections:","question_hi":"निम्नलिखित में से कौन से अनुच्छेद चुनावों से संबंधित हैं:","options":{"A":{"en":"324","hi":"324"},"B":{"en":"325","hi":"325"},"C":{"en":"326","hi":"326"},"D":{"en":"327","hi":"327"},"E":{"en":"352","hi":"352"}},"correct":"ABCD","explanation_en":"Articles 324, 325, 326 and 327 deal with elections. Article 352 deals with National Emergency.","explanation_hi":"अनुच्छेद 324, 325, 326 और 327 चुनावों से संबंधित हैं। अनुच्छेद 352 राष्ट्रीय आपातकाल से संबंधित है।","ref":"Articles 324-327, Constitution of India"},{"chapter":CH,"subtopic":"Elections","type":"assertion_reason","question_en":None,"question_hi":None,"assertion_en":"Elections to Lok Sabha and State Legislative Assemblies are held on basis of adult suffrage.","assertion_hi":"लोकसभा और राज्य विधान सभाओं के चुनाव वयस्क मताधिकार के आधार पर होते हैं।","reason_en":"Article 326 provides that elections to House of People and Legislative Assemblies of States shall be on basis of adult suffrage.","reason_hi":"अनुच्छेद 326 के अनुसार लोकसभा और राज्य विधान सभाओं के चुनाव वयस्क मताधिकार के आधार पर होंगे।","correct":"A","explanation_en":"Both A and R are true and R correctly explains A - Article 326 provides for adult suffrage.","explanation_hi":"A और R दोनों सत्य हैं और R सही ढंग से A की व्याख्या करता है - अनुच्छेद 326 वयस्क मताधिकार का प्रावधान करता है।","ref":"Article 326, Constitution of India"},{"chapter":CH,"subtopic":"Elections","type":"matching","question_en":None,"question_hi":None,"column1":[{"en":"Article 324","hi":"अनुच्छेद 324"},{"en":"Article 325","hi":"अनुच्छेद 325"},{"en":"Article 326","hi":"अनुच्छेद 326"},{"en":"Article 327","hi":"अनुच्छेद 327"},{"en":"Article 329","hi":"अनुच्छेद 329"}],"column2":[{"en":"Superintendence of elections","hi":"चुनावों का अधीक्षण"},{"en":"No discrimination on grounds of religion","hi":"धर्म के आधार पर कोई भेदभाव नहीं"},{"en":"Adult suffrage","hi":"वयस्क मताधिकार"},{"en":"Parliament power to make provisions","hi":"संसद की व्यवस्था करने की शक्ति"},{"en":"Bar to courts in electoral matters","hi":"चुनावी मामलों में अदालतों पर रोक"}]},{"correct_mapping":{"0":"0","1":"1","2":"2","3":"3","4":"4"}},{"chapter":CH,"subtopic":"Elections","type":"matching","question_en":None,"question_hi":None,"column1":[{"en":"First past the post","hi":"पहले पोस्ट के बाद"},{"en":"Adult suffrage","hi":"वयस्क मताधिकार"},{"en":"NOTA","hi":"NOTA"},{"en":"Model Code of Conduct","hi":"आदर्श आचरण संहिता"}],"column2":[{"en":"Candidate with most votes wins","hi":"सबसे अधिक वोट वाला उम्मीदवार जीतता है"},{"en":"Right to vote to all citizens above 18 years","hi":"18 वर्ष से अधिक आयु के सभी नागरिकों को मतदान का अधिकार"},{"en":"None of the Above option","hi":"उपरोक्त में से कोई नहीं विकल्प"},{"en":"Code of conduct for political parties and candidates during elections","hi":"चुनावों के दौरान राजनीतिक दलों और उम्मीदवारों के लिए आचरण संहिता"}]},{"correct_mapping":{"0":"0","1":"1","2":"2","3":"3"}},{"chapter":CH,"subtopic":"Elections","type":"assertion_reason","question_en":None,"question_hi":None,"assertion_en":"Election Commission is an independent constitutional body.","assertion_hi":"निर्वाचन आयोग एक संवैधानिक निकाय है।","reason_en":"Article 324 provides that superintendence direction and control of elections shall be vested in Election Commission.","reason_hi":"अनुच्छेद 324 चुनावी नामावलियों के तैयार करने और सभी चुनावों के संचालन का अधीक्षण निर्वाचन आयोग में निहित होगा।","correct":"A","explanation_en":"Both A and R are true and R correctly explains A - Election Commission is established under Article 324.","explanation_hi":"A और R दोनों सत्य हैं और R सही ढंग से A की व्याख्या करता है - निर्वाचन आयोग अनुच्छेद 324 के तहत स्थापित है।","ref":"Article 324, Constitution of India"}]
print(f"batch34 Elections prepared: {len(NEW_QUESTIONS)} questions")
