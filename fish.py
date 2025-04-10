import pandas as pd
from fpdf import FPDF
import yagmail
import os 

df = pd.read_excel('employeepays.xlsx',)

# Display the DataFrame
print(df)

df["Net Salary"] = df["Basic Salary"] + df["Allowances"] - df["Deductions"]
print(df[["Net Salary"]])

# Load Excel File
df = pd.read_excel("employeepays.xlsx")


# Strip whitespace from column names to prevent lookup errors
df.columns = df.columns.str.strip()

# Verify Column Names (For Debugging)
print("Updated Columns in Excel File:", df.columns)

# Ensure Required Columns Exist
expected_columns = ["Employee id", "Name", "Email", "Basic Salary", "Allowances", "Deductions"]
for col in expected_columns:
    if col not in df.columns:
        raise KeyError(f"Column '{col}' is missing from the Excel file!")

# Calculate Net Salary
df["Net Salary"] = df["Basic Salary"] + df["Allowances"] - df["Deductions"]

# Function to Generate Payslip PDFs
class PayslipPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 26)
        self.cell(200, 10, "AIRWELL DEALERSHIP", ln=True, align="C")
        self.ln(10)

    def generate_payslip(self, employee):
        self.set_font("Arial", size=12)
        
        details = [
            f"Employee ID: {employee['Employee id']}",
            f"Name: {employee['Name']}",
            f"Email: {employee['Email']}",
            f"Basic Salary: ${employee['Basic Salary']:.2f}",
            f"Allowances: ${employee['Allowances']:.2f}",
            f"Deductions: ${employee['Deductions']:.2f}",
            f"Net Salary: ${employee['Net Salary']:.2f}"
        ]
        
        for line in details:
            self.cell(0, 10, line, ln=True, align="L")
        
        self.ln(10)
        self.cell(0, 10, "Signature: ___________________", ln=True, align="L")
        self.cell(0, 10, "Date: April 2025", ln=True, align="L")


# Generate Payslip PDFs
for _, row in df.iterrows():
    pdf = PayslipPDF()
    pdf.add_page()
    pdf.generate_payslip(row)
    filename = f"{row['Employee id']}_payslip.pdf"
    pdf.output(filename)

print("Payslips generated successfully!")

output_folder = "C:/Users/Quinton Bakasa/Desktop/python_PDFs/"  # Ensure this folder exists
for _, row in df.iterrows():
    filename = f"{output_folder}{row['Employee id']}_payslip.pdf"  # Save to the desired folder
    pdf = PayslipPDF()
    pdf.add_page()
    pdf.generate_payslip(row)
    pdf.output(filename)
print("Payslips generated successfully!")


output_folder = "C:/Users/Quinton Bakasa/Desktop/python_PDFs/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Email Setup
SENDER_EMAIL = "lloyddonnel@gmail.com"
SENDER_PASSWORD = "ssfdwizzdgropeac"  # Use a valid Gmail App Password

try:
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Connected to Gmail SMTP server.")
except Exception as e:
    print(f"❌ Failed to connect to Gmail SMTP: {e}")
    exit()

# Send Payslips via Email
for _, row in df.iterrows():
    try:
        filename = f"{row['Employee id']}_payslip.pdf"
        print(f"📤 Sending to {row['Email']}...")

        yag.send(
            to=row["Email"],
            subject="Your Monthly Payslip",
            contents=f"Dear {row['Name']},\n\nPlease find your payslip attached.\n\nBest regards,\nYour Company",
            attachments=filename
        )
        print(f"✅ Sent to {row['Email']}")
    except Exception as e:
        print(f"❌ Failed to send to {row['Email']}: {e}")

print("🏁 All payslips sent!")
