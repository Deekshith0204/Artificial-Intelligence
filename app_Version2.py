import streamlit as st
import pandas as pd
from recommendation_engine import InternshipRecommender

st.set_page_config(page_title="Internship Domain Recommendation", layout="centered")
st.title("🎯 Internship Domain Recommendation Engine")

st.write("""
Enter your profile information (skills, interests, experience, etc.), and get personalized internship domain recommendations!
""")

uploaded_file = st.file_uploader("Upload Internship Domains CSV (or use default)", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("internship_domains.csv")

profile_text = st.text_area("Enter your profile/skills/interests here:", height=150)
top_n = st.slider("Number of recommendations:", 1, 10, 5)

if st.button("Get Recommendations"):
    if profile_text.strip():
        recommender = InternshipRecommender(df)
        with st.spinner("Generating recommendations..."):
            recs = recommender.recommend(profile_text, top_n=top_n)
        if recs is not None and not recs.empty:
            st.success("Recommended Internship Domains:")
            st.dataframe(recs, use_container_width=True)
        else:
            st.info("No matching internship domains found.")
    else:
        st.warning("Please enter your profile information.")
