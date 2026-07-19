def generate_report(result):
    report = f"""
===============================
VOICE BASED CONCEPT ANALYSIS
===============================

Semantic Score : {result['semantic_score']}

Fluency Score  : {result['fluency_score']}

Final Score    : {result['final_score']}

Feedback       : {result['feedback']}

===============================
"""

    return report