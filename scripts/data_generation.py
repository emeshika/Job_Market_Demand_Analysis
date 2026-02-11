import pandas as pd
import numpy as np
import os

def generate_job_market_data():
    np.random.seed(42)
    rows = 1250
    
    # Pre-defined lists for realistic data
    titles = ['Data Scientist', 'ML Engineer', 'Full Stack Developer', 'QC Officer', 'HR Analyst', 'Cloud Architect']
    industries = ['IT & Outsourcing', 'Finance', 'Healthcare', 'Manufacturing', 'Retail']
    skills = ['Python', 'SQL', 'AWS', 'Project Management', 'Machine Learning', 'Java', 'Power BI']
    
    data = {
        'Post_Date': pd.date_range(start='2024-01-01', periods=rows, freq='h'), # 1. Timeline for forecasting
        'Job_Title': np.random.choice(titles, rows),                            # 2. To identify emerging roles
        'Industry': np.random.choice(industries, rows),                        # 3. For industry-specific demand
        'Primary_Skill': np.random.choice(skills, rows),                        # 4. To track desired skills
        'Experience_Level': np.random.choice(['Entry', 'Mid', 'Senior', 'Lead'], rows), # 5. Seniority trends
        'Min_Salary': np.random.randint(50000, 100000, rows),                   # 6. Salary benchmarking
        'Max_Salary': np.random.randint(110000, 200000, rows),                  # 7. Salary benchmarking
        'Region': np.random.choice(['Colombo', 'Kandy', 'Galle', 'Jaffna'], rows, p=[0.6, 0.2, 0.1, 0.1]), # 8. Geographic demand
        'Remote_Allowed': np.random.choice([0, 1], rows, p=[0.3, 0.7]),         # 9. Work-style trends
        'Applicant_Count': np.random.randint(5, 300, rows),                     # 10. For competition analysis
        'Job_Type': np.random.choice(['Full-time', 'Contract', 'Intern'], rows), # 11. Engagement models
        'Company_Size': np.random.choice(['Startup', 'SME', 'MNC'], rows),      # 12. Hiring source data
        'Urgency_Level': np.random.choice(['High', 'Medium', 'Low'], rows),     # 13. Demand velocity
        'Education_Required': np.random.choice(['Bachelors', 'Masters', 'PhD'], rows), # 14. Skill barrier analysis
        'Attrition_Risk': np.random.uniform(0.1, 0.9, rows),                    # 15. For scenario analysis
        'Economic_Indicator_Score': np.random.uniform(1, 10, rows),             # 16. External factor
        'Hiring_Budget_Status': np.random.choice(['Under', 'On-Track', 'Over'], rows) # 17. Budget trends
    }
    
    df = pd.DataFrame(data)
    
    # Derived column for complexity
    df['Demand_Index'] = (df['Applicant_Count'] / df['Min_Salary']) * 1000
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw_market_data.csv', index=False)
    print(f"Generated {rows} rows with {len(df.columns)} columns in data/raw_market_data.csv")

if __name__ == "__main__":
    generate_job_market_data()