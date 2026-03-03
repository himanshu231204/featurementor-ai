# 🧠 FeatureMentor AI  

### A Student-Focused AI Feature Engineering Advisor
🔗 **Live Application:** https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/

[![Live App](https://img.shields.io/badge/Live%20App-Visit%20Now-brightgreen)](https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![GenAI](https://img.shields.io/badge/GenAI-Gemini-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

**FeatureMentor AI** is a **learning-oriented AI Feature Engineering Advisor** built for beginner and intermediate data science students.

The goal of this project is not automation, but **understanding**.

Instead of blindly applying preprocessing steps, FeatureMentor AI:
- Analyzes tabular datasets
- Recommends feature engineering actions
- Explains *why* each decision is made in simple language
- Generates a learning-focused PDF report

This makes feature engineering **transparent, explainable, and student-friendly**.

---

## 🎯 Why FeatureMentor AI?

Most beginners struggle with feature engineering because:
- Preprocessing steps are applied without reasoning
- Tutorials explain *how*, not *why*
- AutoML tools hide decision logic

👉 **FeatureMentor AI solves this gap** by acting like a **mentor**, not just a tool.

> **Core Design Principle:**  
> **AI explains decisions — it does not make decisions.**

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/

### What you can do:
- Upload any CSV dataset
- Select a target column
- View feature-wise recommendations
- Read beginner-friendly explanations
- Download a detailed PDF report

---

## 🏗️ System Architecture

```
CSV Dataset
↓
Data Profiler (Statistics)
↓
Rule-Based Feature Engine
↓
GenAI Explanation Layer
↓
Interactive Dashboard + PDF Report
```

### Key Architectural Decisions
- Deterministic rules ensure correctness
- GenAI is restricted to **explanations only**
- Fail-safe fallback if AI service is unavailable
- Modular and scalable `src/`-based structure

---

## 📊 Feature Engineering Logic (Examples)

| Scenario | Recommendation | Reason |
|--------|---------------|--------|
| Identifier column (`PassengerId`) | Drop Feature | No predictive meaning |
| High missing values (`Cabin`) | Drop Feature | Unreliable signal |
| Numeric + missing (`Age`) | Median Imputation | Robust to outliers |
| Highly skewed numeric (`Fare`) | Log Transformation | Improves model stability |
| Low-cardinality categorical (`Sex`) | One-Hot Encoding | Safe and interpretable |
| High-cardinality categorical (`Ticket`) | Target Encoding | Avoids sparse vectors |

---

## 🤖 Role of GenAI (Gemini)

GenAI is used **only for explanation**, not for decision-making.

### What AI does:
- Explains feature engineering decisions
- Uses simple, mentor-style language
- Helps students build intuition

### What AI does NOT do:
- ❌ Decide transformations  
- ❌ Modify datasets  
- ❌ Train ML models  

This ensures **trust, correctness, and explainability**.

---

## 🖥️ User Interface

- Modern SaaS-style dark theme
- Tab-based workflow:
  - 📂 Upload Dataset
  - 📊 Analysis Dashboard
  - 📘 User Manual
- Feature-wise expandable insights
- Visual badges, summary cards, and progress indicators
- Built-in documentation and limitations

---

## ✅ Where This Tool Works

FeatureMentor AI works on:
- Any **tabular CSV dataset**
- Classification problems
- Regression problems
- Mixed numerical and categorical features

**Tested on:**
- Titanic – Machine Learning from Disaster  
- House Prices – Advanced Regression Techniques  
- Adult Census Income Dataset  

---

## ⚠️ Limitations

This tool is intentionally designed for **learning**, not full automation.

- ❌ No image, text, or audio datasets
- ❌ No time-series feature engineering
- ❌ No automatic model training
- ❌ Does not directly modify datasets

Very small datasets may produce weak statistical signals.

---

## 📁 Project Structure

```
featurementor-ai/
│
├── src/
│   ├── core/        # Profiling & feature rules
│   ├── ai/          # GenAI explanations
│   ├── reports/     # PDF generation
│   └── ui/          # Streamlit dashboard
│
├── test_run.py
├── requirements.txt
├── README.md
```

---

## 🛠️ Local Setup (Optional)

```bash
git clone https://github.com/himanshu231204/featurementor-ai.git
cd featurementor-ai

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run src/ui/app.py
```

---

## 🎓 Who Should Use This?

* Beginner Data Science students
* College students learning Machine Learning
* Anyone confused about feature engineering
* Educators teaching data preprocessing concepts

---

## 👨‍💻 Developed By

**Himanshu Kumar**

* 🔗 LinkedIn: [https://www.linkedin.com/in/himanshu231204](https://www.linkedin.com/in/himanshu231204)
* 🐙 GitHub: [https://github.com/himanshu231204](https://github.com/himanshu231204)

---

## 💖 Support This Project

If this project helped you, consider supporting my work!

[![Sponsor](https://img.shields.io/badge/Sponsor-💖-ff69b4?style=for-the-badge)](https://github.com/sponsors/himanshu231204)

Every contribution helps me:
- ⏰ Spend more time on open-source
- 🆓 Keep all tools free for everyone
- 📚 Create more tutorials and guides
- 🚀 Build new developer tools

**[⭐ Star this repo](../../stargazers)** if you find it useful — it means a lot!

---

## ⭐ Final Note

FeatureMentor AI is not just a tool —
it is a **learning companion** for understanding feature engineering.

If you find this project useful, feel free to ⭐ the repository.