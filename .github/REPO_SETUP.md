# GitHub Repository Settings

This file contains the recommended **description** and **topics** for this repository to
maximize discoverability and stars. You can apply them automatically (recommended) or
manually through the GitHub UI.

---

## 🚀 Option 1 — Apply Automatically (Recommended)

A GitHub Actions workflow is included at `.github/workflows/set-repo-metadata.yml`.

1. Go to **Actions → Set Repository Description and Topics** on your repository page
2. Click **"Run workflow"** → **"Run workflow"**
3. The workflow sets the description, homepage URL, and all 20 topics in one step

> **Note:** The `GITHUB_TOKEN` used by the workflow needs `administration: write`
> permission. If the run fails with a 403, go to **Settings → Actions → General →
> Workflow permissions** and enable **"Read and write permissions"**, then re-run.

---

## 🛠️ Option 2 — Apply Manually via GitHub UI

### 📝 Repository Description

Click the ⚙️ gear icon next to **"About"** on your repository page and paste this into
the **"Description"** field (228 characters — within GitHub's 350-character limit):

```
🧠 AI-powered Feature Engineering Mentor for ML students. Upload any CSV → get smart preprocessing recommendations with Google Gemini explanations. Learn WHY, not just HOW. Built with Streamlit + Python. ⭐ Star if useful!
```

### 🌐 Homepage URL

```
https://featurementor-ai-7fgt3wychg7xj6ltklge7w.streamlit.app/
```

### 🏷️ Repository Topics

In the same **"About"** dialog, add each of these topics:

```
machine-learning
feature-engineering
data-science
python
streamlit
google-gemini
generative-ai
artificial-intelligence
data-preprocessing
educational
open-source
beginner-friendly
pandas
scikit-learn
explainable-ai
ml-education
kaggle
data-analysis
pdf-report
genai
```

---

## 💡 Why These Topics?

| Topic | Reason |
|:--|:--|
| `machine-learning` | Core domain — very high search traffic |
| `feature-engineering` | The exact problem this tool solves |
| `data-science` | Broad audience — beginner data scientists |
| `python` | Language filter — huge GitHub community |
| `streamlit` | Framework filter — active Streamlit community |
| `google-gemini` | Trending AI tag |
| `generative-ai` / `genai` | Trending tag — high discoverability |
| `explainable-ai` | Growing niche with engaged audience |
| `beginner-friendly` | Attracts students and learners |
| `educational` | Differentiates from pure AutoML tools |
| `kaggle` | Ties to datasets used (Titanic, House Prices) |
