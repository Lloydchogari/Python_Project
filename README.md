Payroll Automated Script - Readme 📄

Description
This Python script automates the payroll process by calculating employees' net salaries, generating personalized payslip PDFs, and emailing them directly to each employee. It ensures accurate and efficient salary processing for businesses. 🖥️💼

Features 🚀
Feature	Description
Excel Integration	Reads employee data from an Excel file (employeepays.xlsx), including salary details like basic salary, allowances, and deductions. 📊
Net Salary Calculation	Computes the net salary using the formula: Net Salary = Basic Salary + Allowances - Deductions 💵
PDF Payslip Generation	Creates personalized PDF payslips for each employee using the [fpdf] library. 📑
Email Delivery	Sends the payslips directly to employees via email using the [yagmail] library. 📧
Customizable Output	Users can choose the folder where the generated payslips will be saved. 🗂️
Requirements ⚙️
Requirement	Description
Python 3.x	Python version required for the script to run. 🐍
Libraries	pandas
fpdf
yagmail
os
To install the required libraries, run:
pip install pandas fpdf yagmail

Setup Instructions 🛠️
Step	Action
Prepare the Excel file	Create an Excel file named employeepays.xlsx containing the following columns:
- Employee ID
- Name
- Email
- Basic Salary
- Allowances
- Deductions
Output Folder	Specify the folder path where PDF payslips will be saved. Ensure the folder exists or it will be created. 🗂️
Email Configuration	Replace placeholders in the script with your Gmail credentials:
- SENDER_MAIL: Your Gmail address
- SENDER_PASSWORD: A valid Gmail App Password (use for better security) 🔐
Run the Script	Execute the script to calculate salaries, generate payslips, and email them to employees. 🏃‍♂️💻
Outputs 📤
Output	Description
PDF Payslips	Payslips are saved in the specified folder with filenames based on the Employee ID. 📑
Emails	Each employee receives an email with their personalized payslip attached. 📧
Example Workflow 💼
The script reads the employeepays.xlsx file to gather employee data. 📊

It calculates the net salary for each employee. 🧮

Individual payslips are generated as PDF files and saved in the specified folder. 📂

The payslips are emailed to the employees using Gmail's SMTP. 📬

Troubleshooting ⚠️
Issue	Solution
Excel File Issues	Ensure the column names in the Excel file match exactly with the required names in the script. 📝
Email Issues	Make sure Gmail App Passwords are enabled and the sender’s email credentials are correct. 🔑
License 📜
This project is licensed under the MIT License.

Developed by Lloyd Donnel Chogari and open for modifications. 🔄