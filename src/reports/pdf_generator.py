from fpdf import FPDF


class FeatureReportPDF(FPDF):

    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AI Feature Engineering Advisor Report", ln=True, align="C")
        self.ln(5)

    def add_section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, title, ln=True)
        self.ln(2)

    def add_text(self, text):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 6, text)
        self.ln(1)


def generate_pdf(report, output_path="feature_engineering_report.pdf"):
    pdf = FeatureReportPDF()
    pdf.add_page()

    # Intro
    pdf.add_section_title("1. About This Report")
    pdf.add_text(
        "This report provides feature engineering recommendations "
        "generated to help beginner data science students understand "
        "how to prepare data for machine learning models."
    )

    # Feature-wise recommendations
    pdf.add_section_title("2. Feature Recommendations")

    for item in report:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 7, f"Feature: {item['column']} ({item['dtype']})", ln=True)

        for rec in item["recommendations"]:
            pdf.add_text(f"- {rec['explanation']}")

        pdf.ln(2)

    pdf.output(output_path)
