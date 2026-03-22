<div align="center">

# 🧠 FeatureMentor AI

### *The AI Mentor That Teaches You Feature Engineering — Not Just Does It For You*

<p align="center">
  <a href="https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20Now-brightgreen?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/himanshu231204/featurementor-ai/stargazers">
    <img src="https://img.shields.io/github/stars/himanshu231204/featurementor-ai?style=for-the-badge&color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/himanshu231204/featurementor-ai/network/members">
    <img src="https://img.shields.io/github/forks/himanshu231204/featurementor-ai?style=for-the-badge&color=blue" alt="Forks">
  </a>
  <a href="https://github.com/himanshu231204/featurementor-ai/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=flat-square&logo=google&logoColor=white" alt="Gemini AI">
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
</p>

<br/>

> **"Most ML beginners apply preprocessing steps blindly. FeatureMentor AI changes that — it acts as your personal mentor, explaining every decision in plain English."**

</div>

---

## ✨ What Makes This Special?

Most tools tell you **what** to do. FeatureMentor AI tells you **why**.

Upload any CSV dataset → get intelligent feature engineering recommendations → understand the *reasoning* behind every suggestion — all powered by Google Gemini AI.

| Without FeatureMentor AI | With FeatureMentor AI |
|:--|:--|
| 😕 Copy-paste preprocessing from tutorials | ✅ Understand *why* each step matters |
| 😕 AutoML hides the decision logic | ✅ Transparent, explainable recommendations |
| 😕 Guess which features to drop or encode | ✅ Rule-based + AI-backed guidance |
| 😕 No learning, just execution | ✅ Build genuine ML intuition |

---

## 🚀 Live Demo

### 🔗 [Open Live Demo](https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/)

**Try it now — no setup required!**

1. Upload the included `sample_data.csv` (or any CSV dataset)
2. Select your target column
3. Click **Generate Feature Engineering Analysis**
4. Explore AI-powered explanations for each feature
5. Download a professional PDF report

---

## 🎯 Key Features

- 🔍 **Smart Feature Profiling** — Automatically detects data types, missing values, skewness, and cardinality
- 🤖 **AI-Powered Explanations** — Google Gemini generates mentor-style explanations in plain English
- 📋 **Rule-Based Recommendations** — Deterministic, trustworthy feature engineering decisions
- 📄 **PDF Report Generation** — Download a complete feature engineering report for your dataset
- 🎨 **Beautiful Dashboard** — Modern dark-themed Streamlit UI with expandable feature cards
- 🛡️ **Fail-Safe Design** — Graceful fallback if the AI service is unavailable
- 🆓 **100% Free & Open Source** — No login, no API key required for the live app

---

## 🏗️ How It Works

```
📁 CSV Upload
     │
     ▼
📊 Data Profiler          ← Computes stats: dtype, missing%, skewness, cardinality
     │
     ▼
⚙️  Rule-Based Engine     ← Deterministic decisions (always correct)
     │
     ▼
🤖 Gemini AI Layer        ← Generates human-readable explanations only
     │
     ▼
🖥️  Interactive Dashboard + 📄 PDF Report
```

> **Core Principle:** AI explains — it never decides. Rules decide — AI teaches.

---

## 📊 Feature Engineering Decision Table

| Dataset Scenario | Recommendation | Why |
|:--|:--|:--|
| `PassengerId` (unique ID) | 🗑 Drop Feature | No predictive signal — pure identifier |
| `Cabin` (>40% missing) | 🗑 Drop Feature | Too many gaps — unreliable signal |
| `Age` (numeric, some missing) | 📉 Median Imputation | Robust to outliers; preserves distribution |
| `Fare` (highly skewed) | 📈 Log Transformation | Reduces skewness; stabilizes model training |
| `Sex` (2 categories) | 🔠 One-Hot Encoding | Low cardinality — safe and interpretable |
| `Ticket` (hundreds of values) | 🎯 Target Encoding | High cardinality — avoids sparse vectors |

---

## 🖥️ UI Overview

| Tab | Description |
|:--|:--|
| 📂 **Upload Dataset** | Upload CSV, preview data, select target column, trigger analysis |
| 📊 **Analysis Dashboard** | Summary cards, feature-wise recommendations, color-coded action badges, PDF download |
| 📘 **User Manual** | Built-in documentation explaining every concept |

---

## 🛠️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/himanshu231204/featurementor-ai.git
cd featurementor-ai

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run src/ui/app.py
```

> **Note:** The live app uses a shared Gemini API key. For local use, set your own key in `.env`: `GEMINI_API_KEY=your_key_here`

---

## 📁 Project Structure

```
featurementor-ai/
│
├── src/
│   ├── core/
│   │   ├── data_loader.py       # CSV loading utilities
│   │   ├── data_profiler.py     # Feature statistics computation
│   │   ├── feature_rules.py     # Rule-based recommendation engine
│   │   └── recommender.py       # Orchestrates profiling + rules
│   │
│   ├── ai/
│   │   └── explainer.py         # Google Gemini AI explanation layer
│   │
│   ├── reports/
│   │   └── pdf_generator.py     # PDF report generation (fpdf)
│   │
│   └── ui/
│       └── app.py               # Streamlit dashboard
│
├── sample_data.csv              # Example dataset to try immediately
├── test_run.py                  # Basic smoke tests
├── requirements.txt
└── README.md
```

---

## ✅ Supported Dataset Types

| Type | Supported |
|:--|:--:|
| Tabular CSV (classification) | ✅ |
| Tabular CSV (regression) | ✅ |
| Mixed numeric + categorical | ✅ |
| High-cardinality categoricals | ✅ |
| Image / Audio / Text datasets | ❌ |
| Time-series datasets | ❌ |

**Tested on:** Titanic · House Prices · Adult Census Income · Bank Marketing

---

## 🎓 Who Is This For?

| Audience | Benefit |
|:--|:--|
| 🧑‍🎓 Beginner data science students | Learn the *why* behind preprocessing |
| 🏫 College ML courses | Use as a teaching companion tool |
| 🔬 Kaggle competitors | Quick feature audit for any dataset |
| 👩‍🏫 Educators & instructors | Visual explainer for classroom demos |
| 🤔 Anyone confused by feature engineering | Clear, friendly, jargon-free guidance |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [open issues](https://github.com/himanshu231204/featurementor-ai/issues) for ideas.

---

## ⭐ Support This Project

If FeatureMentor AI helped you understand feature engineering better, the biggest way to say thanks is to **star this repository** ⭐

<div align="center">

[![Star this repo](https://img.shields.io/badge/⭐%20Star%20this%20repo-It%20means%20a%20lot!-yellow?style=for-the-badge)](https://github.com/himanshu231204/featurementor-ai/stargazers)

[![Sponsor](https://img.shields.io/badge/💖%20Sponsor-Support%20open--source-ff69b4?style=for-the-badge)](https://github.com/sponsors/himanshu231204)

</div>

Starring helps:
- 📈 Reach more students who need this tool
- ⏰ Motivate continued development
- 🆓 Keep the project free and open-source
- 🚀 Build new features faster

---

## 👨‍💻 Author

<div align="center">

**Himanshu Kumar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/himanshu231204)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/himanshu231204)

</div>

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free for personal, academic, and commercial use.

---

<div align="center">

**FeatureMentor AI** — *Not just a tool. A learning companion.*

⭐ Star · 🍴 Fork · 🐛 Report Bug · 💡 Request Feature

</div>