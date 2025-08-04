# Data Quality Framework (Python)

This project demonstrates a simple, extensible Python framework for automated data quality assessment, focusing on:
- Missing values detection
- Invalid data formats (e.g., email)
- Business rule violations (e.g., negative salaries)
- Reporting issues for remediation

## How to Use

1. Clone the repository.
2. Install requirements: `pip install -r requirements.txt`
3. Place your datasets in the `data/` directory.
4. Run `python scripts/data_quality_checker.py` to generate data quality reports.
5. Review `outputs/data_quality_report.csv` for detailed row-level issues.

## Example

Sample dataset included as `employees_sample.csv` in the data folder.
