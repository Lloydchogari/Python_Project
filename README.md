A Readme file for the automated payslip project 

PAYROLL AUTOMATED SCRIPT

Description
This Python script automates the payroll process by calculating employees' net salaries, generating personalized payslip PDFs, and emailing them directly to employees.
It ensures accuracy and efficiency in salary processing while providing a simple and scalable solution for businesses.

FEATURES
Excel integrations: Reads Employee data from an excel file(employeepays.xlsx), including essential salary details.
Net Salary calculation: Computes the net salary with the formula: Net Salary = Basic Slary + Allowances - Deductions.
PDF Payslip Generation: Creates individual PDF payslips for each employee usig the [fpdf] library.
Email Delivery: Sends payslips to employees via email using the [yagmail] library.
Customizable Output: Allows users to specify the folder for saving generated payslip PDFs 

REQUIREMENTS
>Python 3.x
>libraries > pandas
           > fpdf
           >yagmail 
           >os

NB* Install the required libraries with: "pip install ..." 

SETUP INSTRUCTIONS
1. Prepare the excel file names employeepays.xlsx containing the following columns
    Employee id 
    Name 
    Email 
    Basic Salary
    AllowancesDeductions

2. Output folder:
    Specify the path to the folder where the generated pdf files will be stored.
    Ensurethe folder exists or is created during script execution.

3. Email Configuration:
    Replace the placeholder values in the script with your Gmail account credentilas:

    * SENDER_MAIL: Your Gmail Address.
    *SENDER PASSSWORD: A valid Gmail App Password

(use an app password for better security. Do not hard-code sensitive credentials; consuder using environment variables or a secrets manager)

4 Run the scripts
    Execute the script to calculate salaries, generate payslips and email them.

OUTPUTS
1st  PDF Payslips:
    Saved in the specified output folder with filenames based on the [Employee Id]

2nd  Emails
    Sent to employees with their individual payslip attached, along with a personalized message.  

EXAPMLE WORKFLOW
1 The script reads the employees.xlsx file to gather employee data
2 It calculates the Net Salary for each employee.
Individual Payslips are generated as PDF files in the specified folder.
Payslips are emailed to employees using Gmail SMTP.

TROUBLESHOOTING
Excel File Issues: Verify that the column match exactly with the required names in the script.
Email Issues: Ensure you have enabled Gmail App Passwords and the sender has the correct email credentials.

License
This project is licensed under the MIT License.

Developed by LLOYD DONNEL CHOGARI & open for modifications
