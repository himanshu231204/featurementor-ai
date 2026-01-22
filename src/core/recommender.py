from src.core.feature_rules import generate_feature_recommendations
from src.ai.explainer import explain_recommendation

def recommend_features(profile):
    final_report = []

    for feature in profile:
        recs = generate_feature_recommendations(feature)
        explained_recs = []

        for rec in recs:
            explanation = explain_recommendation(
                feature["column"],
                rec["action"],
                rec["reason"]
            )

            explained_recs.append({
                "action": rec["action"],
                "reason": rec["reason"],
                "explanation": explanation
            })

        final_report.append({
            "column": feature["column"],
            "dtype": feature["dtype"],
            "recommendations": explained_recs
        })

    return final_report
