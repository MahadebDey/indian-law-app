import streamlit as st
import json

st.set_page_config(page_title="Indian Law & Bare Act Portal", page_icon="⚖️", layout="wide")

# JSON फाइल लोड करें
@st.cache_data
def load_data():
    with open("law_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

DATABASE = load_data()

# Sidebar
st.sidebar.title("⚖️ Indian Law Portal")
lang_choice = st.sidebar.radio("Language / भाषा", ["English", "हिंदी"])
lang_code = "en" if lang_choice == "English" else "hi"

selected_act = st.sidebar.selectbox("Select Act / कानून चुनें:", list(DATABASE.keys()))
view_mode = st.sidebar.radio("View Mode / देखने का तरीका:", ["Section-Wise (धारा अनुसार)", "Complete Bare Act (पूरा बेयर एक्ट)"])

search_query = st.sidebar.text_input("🔍 Search / खोजें:")

act_sections = DATABASE[selected_act]

if search_query:
    act_sections = [
        s for s in act_sections 
        if search_query.lower() in s["section"].lower() 
        or search_query.lower() in s[f"title_{lang_code}"].lower()
        or search_query.lower() in s[f"bare_{lang_code}"].lower()
    ]

# Main UI
st.title(f"📖 {selected_act}")

if view_mode == "Complete Bare Act (पूरा बेयर एक्ट)":
    st.markdown("---")
    for sec in act_sections:
        st.subheader(f"{sec['section']}: {sec[f'title_{lang_code}']}")
        st.caption(f"📂 {sec['chapter']}")
        st.info(sec[f"bare_{lang_code}"])
        with st.expander("💡 Notes & Explanations / व्याख्या"):
            st.write(sec[f"notes_{lang_code}"])
        st.markdown("---")
else:
    section_names = [f"{s['section']} - {s[f'title_{lang_code}']}" for s in act_sections]
    if not section_names:
        st.warning("No sections found matching your search. / कोई धारा नहीं मिली।")
    else:
        chosen_sec_idx = st.selectbox("Choose Section / धारा चुनें:", range(len(section_names)), format_func=lambda x: section_names[x])
        sec = act_sections[chosen_sec_idx]

        st.markdown(f"## {sec['section']}: {sec[f'title_{lang_code}']}")
        st.caption(f"📁 {sec['chapter']}")

        tab1, tab2, tab3 = st.tabs(["📜 Bare Act Text", "📌 Extra Explanations", "🎯 Exam Q&A"])

        with tab1:
            st.markdown("### Bare Act Provision")
            st.write(sec[f"bare_{lang_code}"])

        with tab2:
            st.markdown("### Practical Notes & Legal Interpretation")
            st.success(sec[f"notes_{lang_code}"])

        with tab3:
            st.markdown("### Exam Oriented Q&A")
            for q_item in sec["qa"]:
                with st.expander(f"❓ {q_item['q']}"):
                    st.write(f"**Answer:** {q_item['a']}")
