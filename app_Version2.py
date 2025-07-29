import streamlit as st
from recommendation_engine import InternshipRecommender

st.set_page_config(page_title="Internship Domain Recommendation", layout="centered")
st.title("Internship Domain Recommendation Engine")

st.write("""
Enter your profile information (skills, interests, experience, etc.), and get personalized internship domain recommendations!
""")

uploaded_file = st.file_uploader("Upload Internship Domains CSV (or use default)", type=['csv'])
if uploaded_file is not None:
    csv_path = uploaded_file
else:
    csv_path = "internship_domains.csv"

profile_text = st.text_area("Enter your profile/skills/interests here:", height=150)

top_n = st.slider("Number of recommendations:", 1, 10, 5)

if st.button("Get Recommendations"):
    if profile_text.strip():
        recommender = InternshipRecommender(csv_path)
        recs = recommender.recommend(profile_text, top_n=top_n)
        st.success("Recommended Internship Domains:")
        st.dataframe(recs, use_container_width=True)
    else:
        st.warning("Please enter your profile information.")