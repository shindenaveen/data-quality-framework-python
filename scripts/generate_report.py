import pandas as pd

report_df = pd.read_csv('data_quality_report.csv')
print("Data Quality Issues Found:")
print(report_df)
