"""
Test runner for AI Feature Engineering Advisor
End-to-end pipeline:
CSV -> Profiling (skip target) -> Feature Rules -> AI Explanation -> PDF
"""

from src.core.data_loader import load_csv
from src.core.data_profiler import profile_data
from src.core.recommender import recommend_features
from src.reports.pdf_generator import generate_pdf


def main():
    FILE_PATH = "sample_data.csv"   # change if needed
    TARGET_COLUMN = "target"        # e.g. "Survived" for Titanic

    print("🔹 Loading dataset...")
    df = load_csv(FILE_PATH, TARGET_COLUMN)

    print("🔹 Profiling data (target column skipped)...")
    profile = profile_data(df, target_column=TARGET_COLUMN)

    print("🔹 Generating feature recommendations (rule-based + AI)...")
    report = recommend_features(profile)

    # Optional sanity check: print one explanation
    if report and report[0]["recommendations"]:
        print("\n🧠 Sample Explanation:")
        print(report[0]["recommendations"][0]["explanation"])

    print("\n🔹 Generating PDF report...")
    generate_pdf(report)

    print("\n✅ PDF report generated successfully!")


if __name__ == "__main__":
    main()
