def generate_feature_recommendations(feature):
    recommendations = []

    # 1️⃣ IDENTIFIER COLUMN RULE (STRICT & CORRECT)
    col_name = feature["column"].lower()

    if (
        feature["unique_values"] == feature["total_rows"]
        and feature["missing_percent"] == 0
        and col_name.endswith("id")
    ):
        return [{
            "action": "Drop Feature",
            "reason": "Identifier column with no predictive meaning"
        }]

    # 2️⃣ HIGH MISSING VALUES
    if feature["missing_percent"] > 40:
        return [{
            "action": "Drop Feature",
            "reason": "Too many missing values, model may learn wrong patterns"
        }]

    # 3️⃣ NUMERICAL FEATURES
    if feature["is_numeric"]:
        if feature["missing_percent"] > 0:
            recommendations.append({
                "action": "Median Imputation",
                "reason": "Handles missing values without being affected by outliers"
            })

        if feature["skewness"] is not None and abs(feature["skewness"]) > 1:
            recommendations.append({
                "action": "Log Transformation",
                "reason": "Reduces skewness and improves model stability"
            })

        if not recommendations:
            recommendations.append({
                "action": "No Transformation Needed",
                "reason": "Feature already well distributed"
            })

    # 4️⃣ CATEGORICAL FEATURES
    else:
        if feature["unique_values"] <= 10:
            recommendations.append({
                "action": "One-Hot Encoding",
                "reason": "Low number of categories, safe for most models"
            })
        else:
            recommendations.append({
                "action": "Target Encoding",
                "reason": "High cardinality, avoids large sparse vectors"
            })

    return recommendations
