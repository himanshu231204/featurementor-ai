import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ✅ New official Gemini client
client = genai.Client(api_key=API_KEY)

# 🔁 Model priority (best → fallback)
MODEL_PRIORITY = [
    "gemini-1.5-pro",
    "gemini-1.0-pro"
]


def static_fallback_explanation(feature_name, action, reason):
    """
    Guaranteed explanation if AI fails
    """
    return (
        f"For the feature '{feature_name}', the recommended action is "
        f"'{action}'. This is suggested because {reason.lower()}. "
        "Applying this step helps machine learning models learn more "
        "stable and reliable patterns from the data."
    )


def explain_recommendation(feature_name, action, reason):
    """
    AI-powered explanation with fail-safe fallback
    """

    prompt = f"""
You are a friendly and patient data science mentor teaching a beginner student.

Explain the following feature engineering decision in very simple language.

Feature Name: {feature_name}
Suggested Action: {action}
Reason: {reason}

Guidelines for explanation:
- Explain WHAT this action means in simple words
- Explain WHY this action is useful for machine learning models
- Explain WHAT problem it solves (missing values, noise, overfitting, etc.)
- Give a small real-world or intuitive example if possible
- Avoid formulas and heavy technical terms
- Write in short, clear paragraphs (5–7 lines)
- Tone should feel like a teacher explaining to a college student

Do NOT mention AI, LLMs, or prompts.
Do NOT be too short.
"""

    for model_name in MODEL_PRIORITY:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            if response and response.text:
                return response.text.strip()

        except Exception:
            continue

    # 🔒 Guaranteed fallback
    return static_fallback_explanation(feature_name, action, reason)
