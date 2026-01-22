
# 🧠 FeatureMentor AI

**Learn Feature Engineering the Right Way**

FeatureMentor AI is a **student-focused AI Feature Engineering Advisor** that helps beginners understand **why** specific preprocessing and feature engineering steps are applied — not just *what* to do.

Unlike automated preprocessing tools, FeatureMentor AI is designed as a **learning-first system**, combining **rule-based machine learning logic** with **GenAI-powered explanations** and a **professional interactive dashboard**.

---

## 🚀 Key Features

* 📊 Analyzes any **tabular CSV dataset**
* 🧠 Rule-based feature engineering recommendations
* 🤖 AI-powered, beginner-friendly explanations (Gemini)
* 📄 Automatically generates a **learning-focused PDF report**
* 🖥️ Professional **dashboard-style UI** (Streamlit)
* 📘 Built-in **User Manual & limitations**
* 🛡️ Fail-safe AI design (never crashes if AI fails)

---

## 🎯 Why FeatureMentor AI?

Most beginners struggle with feature engineering because:

* Preprocessing steps are applied blindly
* Tutorials explain *how*, not *why*
* AutoML tools hide the reasoning

**FeatureMentor AI solves this gap** by acting like a **mentor**, not just a tool.

> **Design Principle:**
> *AI explains decisions, it does not make them.*

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
Dashboard + PDF Report
```

### Architecture Highlights

* Deterministic rule-based logic for correctness
* GenAI used **only for explanation**, not decision-making
* Modular, scalable project structure (`src/` based)

---

## 📁 Project Structure

```
ai-feature-engineering-advisor/
│
├── src/
│   ├── core/
│   │   ├── data_loader.py
│   │   ├── data_profiler.py
│   │   ├── feature_rules.py
│   │   └── recommender.py
│   │
│   ├── ai/
│   │   └── explainer.py
│   │
│   ├── reports/
│   │   └── pdf_generator.py
│   │
│   └── ui/
│       └── app.py
│
├── test_run.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ How It Works (Step-by-Step)

1. User uploads a CSV dataset
2. Selects the target column
3. System profiles each feature:

   * Missing values
   * Skewness
   * Cardinality
   * Data type
4. Rule-based engine suggests feature engineering steps
5. GenAI explains **why** each step is recommended
6. Results are shown in a dashboard
7. A detailed PDF report is generated

---

## 🧠 Feature Engineering Logic (Examples)

| Scenario                                | Recommendation     | Reason                |
| --------------------------------------- | ------------------ | --------------------- |
| Identifier column (`PassengerId`)       | Drop Feature       | No predictive meaning |
| High missing values (`Cabin`)           | Drop Feature       | Unreliable signal     |
| Numeric + missing (`Age`)               | Median Imputation  | Robust to outliers    |
| Highly skewed numeric (`Fare`)          | Log Transformation | Stabilizes learning   |
| Low-cardinality categorical (`Sex`)     | One-Hot Encoding   | Safe & interpretable  |
| High-cardinality categorical (`Ticket`) | Target Encoding    | Avoids sparsity       |

---

## 🤖 Role of GenAI (Gemini)

GenAI is used **only for explanation**, not for making decisions.

### Why?

* Prevents hallucinations
* Keeps ML logic deterministic
* Ensures trust and correctness

### Fail-Safe Design

* Model priority system
* Automatic fallback to static explanations
* App never crashes if AI is unavailable

---

## 🖥️ User Interface

* Modern SaaS-style dark theme
* Tab-based workflow:

  * Upload Dataset
  * Analysis Dashboard
  * User Manual
* Feature-wise expandable explanations
* Visual badges & summary cards
* In-app documentation for beginners

---

## ✅ Where This Tool Works

FeatureMentor AI works on:

* Any **tabular CSV dataset**
* Classification problems
* Regression problems
* Mixed numerical & categorical data
* Real-world Kaggle datasets

### Tested On:

* Titanic – Machine Learning from Disaster
* House Prices – Advanced Regression Techniques
* Adult Census Income Dataset

---

## ⚠️ Limitations (Intentional)

This tool is designed for **learning**, not full automation.

* ❌ No image, text, or audio datasets
* ❌ No time-series specific feature engineering
* ❌ No automatic model training
* ❌ Does not modify datasets directly

Very small datasets may produce weak statistical signals.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/himanshu231204/ai-feature-engineering-advisor.git
cd ai-feature-engineering-advisor
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

### Streamlit UI

```bash
streamlit run src/ui/app.py
```

### CLI Test (Optional)

```bash
python test_run.py
```

---

## 🎓 Who Should Use This?

* Beginner Data Science students
* College students learning Machine Learning
* Anyone confused about feature engineering decisions
* Educators teaching data preprocessing concepts

---

## 👨‍💻 Developed By

**Himanshu Kumar**

* 🔗 LinkedIn: [https://www.linkedin.com/in/himanshu231204](https://www.linkedin.com/in/himanshu231204)
* 🐙 GitHub: [https://github.com/himanshu231204](https://github.com/himanshu231204)

---

## ⭐ Final Note

FeatureMentor AI is not just a tool —
it is a **learning companion for understanding feature engineering**.

If you find this project useful, feel free to ⭐ the repository.

---


