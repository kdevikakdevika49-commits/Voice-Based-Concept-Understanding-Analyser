from sentence_transformers import SentenceTransformer, util

# Load Sentence-BERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(reference_text, user_text):
    """
    Calculates semantic similarity between
    the reference text and the user's explanation.
    """

    embedding1 = model.encode(reference_text, convert_to_tensor=True)
    embedding2 = model.encode(user_text, convert_to_tensor=True)

    similarity = util.cos_sim(embedding1, embedding2)

    score = float(similarity[0][0]) * 100

    return round(score, 2)