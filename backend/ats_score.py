from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text: str, jd_text: str) -> float:
    # Combine both texts into a corpus
    corpus = [resume_text, jd_text]

    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Compute cosine similarity between resume and JD
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # Convert to percentage and round
    score_percentage = round(similarity * 100, 2)
    return score_percentage
