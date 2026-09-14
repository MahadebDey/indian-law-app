import streamlit as st

# Page setup (Mobile-friendly config)
st.set_page_config(page_title="Indian Law Study Hub", page_icon="⚖️", layout="wide")

# Sample Data (Major Acts, Minor Acts, Loan/Banking Laws)
LAW_DATA = {
    "Bharatiya Nyaya Sanhita (BNS) [Major Act]": {
        "Sec 103 (Murder)": {
            "en": {
                "title": "Section 103: Punishment for murder",
                "bare_act": "Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.",
                "qa": [
                    {"q": "What is the maximum punishment under Sec 103 BNS?", "a": "Death penalty or imprisonment for life, along with fine."},
                    {"q": "Which section of the IPC does Section 103 BNS replace?", "a": "Section 302 of the Indian Penal Code."}
                ]
            },
            "hi": {
                "title": "धारा 103: हत्या के लिए दंड",
                "bare_act": "जो कोई भी हत्या करेगा, उसे मृत्युदंड या आजीवन कारावास से दंडित किया जाएगा, और वह जुर्माने के लिए भी उत्तरदायी होगा।",
                "qa": [
                    {"q": "BNS की धारा 103 के तहत अधिकतम सजा क्या है?", "a": "मृत्युदंड या आजीवन कारावास, साथ में जुर्माना।"},
                    {"q": "धारा 103 BNS ने IPC की किस धारा को प्रतिस्थापित किया है?", "a": "भारतीय दंड संहिता (IPC) की धारा 302।"}
                ]
            }
        }
    },
    "Negotiable Instruments Act (NI Act) [Loan/Banking Law]": {
        "Sec 138 (Cheque Bounce)": {
            "en": {
                "title": "Section 138: Dishonour of cheque for insufficiency of funds",
                "bare_act": "Where any cheque drawn by a person on an account maintained by him with a banker for payment of any amount of money... is returned by the bank unpaid... such person shall be deemed to have committed an offence.",
                "qa": [
                    {"q": "What is the maximum imprisonment under Section 138 NI Act?", "a": "Up to two years, or with fine which may extend to twice the amount of the cheque, or with both."},
                    {"q": "Within how many days must a legal demand notice be sent to the drawer?", "a": "Within 30 days of receiving information from the bank regarding the dishonour of the cheque."}
                ]
            },
            "hi": {
                "title": "धारा 138: खाते में पर्याप्त धन न होने पर चेक का अनादर (बाउंस)",
                "bare_act": "जहाँ किसी व्यक्ति द्वारा अपने बैंक खाते से किसी राशि के भुगतान के लिए जारी किया गया चेक बैंक द्वारा बिना भुगतान लौटा दिया जाता है... तो ऐसा व्यक्ति अपराध का दोषी माना जाएगा।",
                "qa": [
                    {"q": "NI Act की धारा 138 के तहत अधिकतम सजा क्या है?", "a": "दो वर्ष तक का कारावास, या चेक की राशि के दोगुने तक का जुर्माना, या दोनों।"},
                    {"q": "चेक बाउंस होने की सूचना मिलने के कितने दिनों के भीतर लीगल डिमांड नोटिस भेजना अनिवार्य है?", "a": "बैंक से सूचना प्राप्त होने के 30 दिनों के भीतर।"}
                ]
            }
        }
    },
    "SARFAESI Act [Loan Recovery]": {
        "Sec 13 (Enforcement of Security Interest)": {
            "en": {
                "title": "Section 13: Enforcement of security interest without court intervention",
                "bare_act": "Enables banks and financial institutions to recover their non-performing assets (NPAs) without the intervention of courts or tribunals.",
                "qa": [
                    {"q": "How many days notice is required under Section 13(2)?", "a": "60 days notice to the borrower to discharge their liabilities."}
                ]
            },
            "hi": {
                "title": "धारा 13: बिना अदालती हस्तक्षेप के प्रतिभूति हित का प्रवर्तन",
                "bare_act": "बैंकों और वित्तीय संस्थानों को बिना अदालत या ट्रिब्यूनल के हस्तक्षेप के अपनी गैर-निष्पादित परिसंपत्तियों (NPA) की वसूली करने का अधिकार देता है।",
                "qa": [
                    {"q": "धारा 13(2) के तहत बकाएदार को कितने दिनों का नोटिस दिया जाता है?", "a": "अपनी देनदारियों का भुगतान करने के लिए 60 दिनों का नोटिस।"}
                ]
            }
        }
    }
}

# Sidebar Controls
st.sidebar.title("⚙️ Settings / सेटिंग्स")
lang_choice = st.sidebar.radio("Select Language / भाषा चुनें", ["English", "हिंदी"])
lang_key = "en" if lang_choice == "English" else "hi"

st.sidebar.markdown("---")
selected_act = st.sidebar.selectbox(
    "Select Act / कानून चुनें:",
    options=list(LAW_DATA.keys())
)

available_sections = list(LAW_DATA[selected_act].keys())
selected_section = st.sidebar.selectbox(
    "Select Section / धारा चुनें:",
    options=available_sections
)

# Main UI Display
data = LAW_DATA[selected_act][selected_section][lang_key]

st.title("⚖️ Indian Law & Exam Prep")
st.subheader(data["title"])

# Bare Act Section
st.markdown("### 📖 Bare Act Text" if lang_key == "en" else "### 📖 मूल बेयर एक्ट (Bare Act)")
st.info(data["bare_act"])

# Question & Answer Section
st.markdown("### 🎯 Exam Oriented Q&A" if lang_key == "en" else "### 🎯 परीक्षा उपयोगी प्रश्नोत्तरी")
for item in data["qa"]:
    with st.expander(f"❓ {item['q']}"):
        st.write(f"**Ans:** {item['a']}")
