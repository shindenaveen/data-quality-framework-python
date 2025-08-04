import pandas as pd
import numpy as np
import re

# Load data
df = pd.read_csv('employees_sample.csv')

# Initialize report dictionary
report = {}

# 1. Missing Values Report
missing = df.isnull().sum()
report['missing_values'] = missing.to_dict()

# 2. Invalid Email Report
def valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, str(email)))

invalid_emails = df['Email'].apply(lambda x: not valid_email(x) if pd.notnull(x) else False)
report['invalid_emails_count'] = int(invalid_emails.sum())

# 3. Negative/zero/NaN Salaries
salary_issues = df['Salary'].apply(lambda x: (not isinstance(x, float) and not isinstance(x, int)) or (pd.isnull(x)) or (float(x) <= 0 if not pd.isnull(x) else False))
report['invalid_salaries_count'] = int(salary_issues.sum())

# 4. Departments - Missing
dept_missing = df['Department'].isnull().sum()
report['department_missing'] = int(dept_missing)

# Save issues rows
issues_rows = df[invalid_emails | salary_issues | df['Department'].isnull() | df['Age'].isnull()]
issues_rows.to_csv('data_quality_report.csv', index=False)

# Print Short Report
for key, value in report.items():
    print(f"{key}: {value}")
