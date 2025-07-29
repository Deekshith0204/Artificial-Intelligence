import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class InternshipRecommender:
    def __init__(self, internship_data_path):
        self.df = pd.read_csv(internship_data_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['description'].fillna(''))

    def recommend(self, profile_text, top_n=5):
        profile_vec = self.vectorizer.transform([profile_text])
        cosine_similarities = linear_kernel(profile_vec, self.tfidf_matrix).flatten()
        top_indices = cosine_similarities.argsort()[-top_n:][::-1]
        return self.df.iloc[top_indices][['domain', 'description', 'required_skills']]