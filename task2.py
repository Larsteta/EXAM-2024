# 2. String Manipulation and Regular Expressions (20%)

import re

# Task 2.1: Validate Email
def validate_email(email):
    reg = re.compile('^[a-zA-Z][a-z]+@(hr|it|fin|mkt|ops)\.company\.com$') # Email pattern
    if reg.match(email):
        print('Valid Email')
        return True
    else:
        print('Invalid Email')
        return False

#Task 2.2: Get Department
def get_department(email):
    validate = validate_email(email) # Validate email
    if validate:
        department = re.search('@(hr|it|fin|mkt|ops)\.company\.com$', email).group(1) # Extract department
        return department
    else:
        return None

#Task 2.3: Categorize Emails
def categorize_emails(email_list):
    departments = {} # Departments dictionary

    # Loop through emails
    for email in email_list: 
        department = get_department(email) # Get department
        if department:
            if department in departments:
                departments[department].append(email) # Add email to department
            else:
                departments[department] = [email] # Create department and add email

    print(departments) # Output departments
    return departments

# Test Cases
email_list = [
    'jdoe@hr.company.com', # Valid
    'Lnguyen@hr.company.com', # Valid
    'asmith@it.company.com', #valid
    'bwhite@fin.company.com', #valid
    'invalidemail@company.com', #invalid
    'cjohnson@mkt.company.com', # valid
    'dlee@ops.company.com', #   valid
    'wrong.email@ops.company.com', #invalid
    'wrong@company.com' #invalid
]

print("Task 2.1 - 2.3 Test Cases:")
print("-"*100)
categorize_emails(email_list)
print("-"*100)

