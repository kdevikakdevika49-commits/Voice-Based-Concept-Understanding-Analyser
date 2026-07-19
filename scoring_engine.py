def calculate_final_score(semantic_score, filler_count):
    """
    Calculate the final understanding score.
    """

    # Fluency score based on filler words
    fluency_score = max(0, 100 - (filler_count * 5))

    # Final weighted score
    final_score = (semantic_score * 0.7) + (fluency_score * 0.3)

    # Feedback
    if final_score >= 85:
        feedback = "Excellent Understanding"
    elif final_score >= 70:
        feedback = "Good Understanding"
    elif final_score >= 50:
        feedback = "Moderate Understanding"
    else:
        feedback = "Needs Improvement"

    return {
        "semantic_score": round(semantic_score, 2),
        "fluency_score": round(fluency_score, 2),
        "final_score": round(final_score, 2),
        "feedback": feedback
    }