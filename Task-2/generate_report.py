import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# Read the CSV file
df = pd.read_csv("sample_data.csv")

# Generate summary statistics
summary = df.describe(include='all').to_string()

# Create a bar chart (Name vs Marks)
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Marks"], color='skyblue')
plt.title("Marks by Student")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# Create a timestamp for the report filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
pdf_filename = f"automated_report_{timestamp}.pdf"

# Create the PDF
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automated Report", ln=True, align='C')

# Summary Section
pdf.set_font("Arial", 'B', 12)
pdf.ln(10)
pdf.cell(200, 10, txt="Summary Statistics", ln=True)

pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 8, summary)

# Chart Section
pdf.set_font("Arial", 'B', 12)
pdf.ln(5)
pdf.cell(200, 10, txt="Marks Chart", ln=True)
pdf.image("chart.png", x=10, y=pdf.get_y() + 5, w=180)

# Output the PDF
pdf.output(pdf_filename)

print(f"Report saved as {pdf_filename}")

