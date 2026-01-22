# ---------------- PATH FIX (IMPORTANT) ----------------
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# ---------------- IMPORTS ----------------
import streamlit as st
import pandas as pd

from src.core.data_profiler import profile_data
from src.core.recommender import recommend_features
from src.reports.pdf_generator import generate_pdf

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FeatureMentor AI",
    layout="wide"
)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div style="padding:32px; border-radius:18px;
background:linear-gradient(135deg,#4F46E5,#6366F1);">
    <h1 style="color:white; margin-bottom:5px;">🧠 FeatureMentor AI</h1>
    <p style="color:#E0E7FF; font-size:18px;">
        Learn Feature Engineering the Right Way.<br>
        AI-powered explanations • Student-friendly • Practical ML insights
    </p>
    <p style="color:#C7D2FE;">
        Developed by <b>Himanshu Kumar</b>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "🟢 **Status:** Ready &nbsp;&nbsp; 🧪 **Mode:** Learning &nbsp;&nbsp; 🤖 **AI:** Gemini Powered"
)

# ---------------- LEARNING PANEL ----------------
st.markdown("""
<div style="padding:18px; border-radius:14px; background:#020617;">
<h3>🎯 What will you learn?</h3>
<ul>
<li>How to handle missing values correctly</li>
<li>When to apply encoding techniques</li>
<li>Why some features should be dropped</li>
<li>How feature engineering impacts ML models</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "📂 Upload Dataset",
    "📊 Analysis Dashboard",
    "📘 User Manual"
])

# ======================================================
# TAB 1: UPLOAD DATASET
# ======================================================
with tab1:
    st.header("Step 1: Upload Your Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df

        st.success("Dataset uploaded successfully ✅")

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Select Target Column")
        target_column = st.selectbox(
            "Target column (value you want to predict)",
            df.columns
        )
        st.session_state["target"] = target_column

        st.info("ℹ️ Target column will be excluded from feature engineering automatically.")

        if st.button("🚀 Generate Feature Engineering Analysis"):
            with st.spinner("Analyzing features and generating explanations..."):
                profile = profile_data(df, target_column=target_column)
                report = recommend_features(profile)
                generate_pdf(report)

                st.session_state["report"] = report

            st.progress(100)
            st.success("✔ Feature engineering analysis completed")
            st.info("👉 Go to **Analysis Dashboard** tab to explore results")

# ======================================================
# TAB 2: ANALYSIS DASHBOARD
# ======================================================
with tab2:
    st.header("📊 Feature Engineering Dashboard")

    if "report" not in st.session_state:
        st.warning("⚠️ Please generate analysis first from the Upload tab.")
    else:
        df = st.session_state["df"]
        report = st.session_state["report"]

        # ---------------- SUMMARY CARDS ----------------
        missing_pct = round(df.isna().mean().mean() * 100, 2)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 📄 Rows")
            st.markdown(f"## {df.shape[0]}")
        with c2:
            st.markdown("### 📊 Columns")
            st.markdown(f"## {df.shape[1]}")
        with c3:
            st.markdown("### ⚠ Avg Missing %")
            st.markdown(f"## {missing_pct}%")

        # ---------------- RECOMMENDATION SUMMARY ----------------
        drop_count = sum(
            1 for f in report
            for r in f["recommendations"]
            if r["action"] == "Drop Feature"
        )

        encode_count = sum(
            1 for f in report
            for r in f["recommendations"]
            if "Encoding" in r["action"]
        )

        st.markdown(f"""
<div style="padding:20px; border-radius:14px; background:#020617;">
<h3>📌 Recommendation Summary</h3>
<ul>
<li>🗑 Dropped Features: <b>{drop_count}</b></li>
<li>🔠 Encoded Features: <b>{encode_count}</b></li>
</ul>
</div>
""", unsafe_allow_html=True)

        st.divider()

        # ---------------- FEATURE OUTPUT ----------------
        st.subheader("Feature-wise Recommendations")

        badge_color = {
            "Drop Feature": "#DC2626",
            "One-Hot Encoding": "#2563EB",
            "Target Encoding": "#7C3AED",
            "Median Imputation": "#059669",
            "Log Transformation": "#F59E0B",
            "No Transformation Needed": "#6B7280"
        }

        for item in report:
            with st.expander(f"🔹 Feature: {item['column']}"):
                for rec in item["recommendations"]:
                    color = badge_color.get(rec["action"], "#6B7280")
                    st.markdown(
                        f"<span style='background:{color}; padding:6px 10px; border-radius:8px;'>"
                        f"{rec['action']}</span>",
                        unsafe_allow_html=True
                    )
                    st.markdown(f"**🧠 Explanation:** {rec['explanation']}")

        st.divider()

        # ---------------- PDF DOWNLOAD ----------------
        st.subheader("📄 Download Report")
        with open("feature_engineering_report.pdf", "rb") as f:
            st.download_button(
                label="⬇ Download Feature Engineering PDF",
                data=f,
                file_name="feature_engineering_report.pdf",
                mime="application/pdf"
            )

        # ---------------- WHAT NEXT ----------------
        st.markdown("""
<div style="padding:18px; border-radius:14px; background:#020617;">
<h3>🚀 What should you do next?</h3>
<ul>
<li>Apply these transformations in your ML pipeline</li>
<li>Train a model and compare performance</li>
<li>Try this tool on another dataset (House Prices)</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ======================================================
# TAB 3: USER MANUAL
# ======================================================
with tab3:
    st.header("📘 User Manual")

    st.markdown("""
### What does FeatureMentor AI do?

FeatureMentor AI helps students **understand feature engineering decisions**
instead of blindly applying preprocessing steps.

It:
- Analyzes each feature
- Suggests correct feature engineering actions
- Explains *why* each step is useful
- Generates a learning-friendly PDF report

---

### How to use

1. Upload your CSV dataset  
2. Select the target column  
3. Click *Generate Feature Engineering Analysis*  
4. View insights in the Dashboard  
5. Download the PDF  

---

### What this tool does NOT do

- ❌ It does NOT train ML models  
- ❌ It does NOT automatically modify your dataset  
- ✅ It focuses on **learning and understanding**

---

---

## ✅ Where does this tool work?

FeatureMentor AI works on **any tabular CSV dataset**, including:

- Classification datasets  
- Regression datasets  
- Datasets with numerical and categorical features  
- Datasets containing missing values or skewed distributions  

**Example datasets:**  
Titanic, House Prices, Adult Census, Bank Marketing

---

## ⚠️ Current limitations

This tool is designed for **learning and understanding**, so:

- ❌ It does not support image, text, or audio datasets  
- ❌ Time-series–specific feature engineering is not included  
- ❌ It does not automatically train machine learning models  
- ❌ It does not modify your dataset directly  

**Important notes:**
- Very small datasets may produce unreliable statistics  
- Identifier detection depends on column naming conventions  
- The focus is on *explainability*, not full automation


""")

# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    """
    <div style="text-align:center; font-size:14px;">
        👨‍💻 Developed by <b>Himanshu Kumar</b><br><br>
        🔗 
        <a href="https://www.linkedin.com/in/himanshu231204" target="_blank">LinkedIn</a> |
        <a href="https://github.com/himanshu231204" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
