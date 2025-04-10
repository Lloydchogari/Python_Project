import pandas as pd
from fpdf import FPDF
import yagmail
import os

# Load Excel File and Strip Whitespace from Column Names
df = pd.read_excel("employeepays.xlsx")
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
        
        # Header with dealership name and background color
        

        self.set_fill_color(230, 230, 230)  # Grey background
        self.rect(0, 0, self.w, self.h, 'F')  # Full-page rectangle fill

        self.set_font("Arial", "B", 20)
        self.set_text_color(0, 102, 204)  # Blue color for header text
        self.set_fill_color(200, 200, 200)  # Light gray background
        self.cell(0, 10, "AIRWELL DEALERSHIP", ln=True, align="C", fill=True)
        self.ln(0)

        self.set_font("Arial", "I", 8)
        self.set_text_color(0, 0, 0)  # Blue color for header text
        self.cell(0, 10, "All motor vehicle dearship", ln=True, align="C", fill=True)
        self.ln(0)


        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 0)  # Blue color for header text
        self.cell(0, 11, "PAY SLIP for April 2025", ln=True, align="C", fill=True, border=1)
        self.ln(15)

        image_path = "logo.jpg"  # Path to your logo
        image_width = 40  # Adjust as needed
        image_height = 20  # Adjust as needed
        x_position = 10  # 10 units from the right edge
        y_position = 10  # 10 units from the top of the page
        self.image(image_path, x=x_position, y=y_position, w=image_width, h=image_height)


    def footer(self):
        # Add page number in the footer
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Thanks for your contribution to the company, Visit the HR for inquiries {self.page_no()}", align="C")

    def generate_payslip(self, employee):
        self.set_font("Arial", size=12)
        self.set_text_color(0, 0, 0)  # Reset text color to black

        # Structured table for employee details
        details = [
            ("Employee ID", employee['Employee id']),
            ("Name", employee['Name']),
            ("Email", employee['Email']),
            ("Basic Salary", f"${employee['Basic Salary']:.2f}"),
            ("Allowances", f"${employee['Allowances']:.2f}"),
            ("Deductions", f"${employee['Deductions']:.2f}"),
            ("Net Salary", f"${employee['Net Salary']:.2f}")
        ]
        
        for label, value in details:
            self.set_font("Arial", "B", 12)  # Bold for labels
            self.cell(50, 10, f"{label}:", border=1, align="L")
            self.set_font("Arial", "", 12)  # Regular for values
            self.cell(0, 10, str(value), border=1, ln=True, align="L")

        self.set_font("Arial", "B", 20)
        self.set_text_color(0, 0, 0)  # Blue color for header text
        self.set_fill_color(200, 200, 200)  # Light gray background
        self.cell(0, 10, "REVIEW NET SALARY AS YOUR PAY", ln=True, align="C", fill=True)
        self.ln(10)


        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 0)  # Blue color for header text
        self.set_fill_color(230, 230, 230)  # Light gray background
        self.cell(0, 10, "Signature__________________", ln=True, align="L", fill=True)
        self.cell(0, 10, "Date: 10 April 2025", ln=True, align="L")
        self.ln(0)



# Generate and Save Payslip PDFs to the Specified Folder
output_folder = "C:/Users/Quinton Bakasa/Desktop/python_PDFs/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Create the folder if it doesn't exist

for _, row in df.iterrows():
    pdf = PayslipPDF()
    pdf.add_page()
    pdf.generate_payslip(row)
    
    # Explicitly save the PDF to the desired folder
    filename = os.path.join(output_folder, f"{row['Employee id']}_payslip.pdf")
    pdf.output(filename)  # Ensures the files are saved only to the specified folder
    print(f"Saved {filename}")

print("Payslips generated successfully!")

# Email Setup
SENDER_EMAIL = ""
SENDER_PASSWORD = ""  # Use a valid Gmail App Password (Consider using environment variables for better security)

try:
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Connected to Gmail SMTP server.")
except Exception as e:
    print(f"❌ Failed to connect to Gmail SMTP: {e}")
    exit()

# Send Payslips via Email
for _, row in df.iterrows():
    try:
        filename = os.path.join(output_folder, f"{row['Employee id']}_payslip.pdf")
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
