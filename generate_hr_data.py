import pandas as pd
import numpy as np
from datetime import datetime

np.random.seed(42)
n = 1200

data = {
    'EmpID': [f'E{1000+i}' for i in range(n)],
    'Age': np.random.randint(22, 60, n),
    'AgeGroup': np.random.choice(['18-25','26-35','36-45','46-55','56+'], n),
    'Attrition': np.random.choice(['Yes','No'], n, p=[0.16, 0.84]),
    'BusinessTravel': np.random.choice(['Non-Travel','Travel_Rarely','Travel_Frequently'], n, p=[0.1,0.7,0.2]),
    'Department': np.random.choice(['Sales','R&D','HR','Finance','IT','Marketing'], n, p=[0.25,0.35,0.08,0.12,0.15,0.05]),
    'Gender': np.random.choice(['Male','Female'], n, p=[0.6,0.4]),
    'MaritalStatus': np.random.choice(['Single','Married','Divorced'], n),
    'MonthlyIncome': np.random.randint(2500, 18000, n),
    'SalarySlab': np.random.choice(['Low','Medium','High','Very High'], n),
    'JobRole': np.random.choice(['Sales Executive','Research Scientist','Laboratory Technician','Manager','Developer','HR Specialist'], n),
    'YearsAtCompany': np.random.randint(0, 25, n),
    'YearsInCurrentRole': np.random.randint(0, 18, n),
    'PercentSalaryHike': np.random.randint(5, 25, n),
    'OverTime': np.random.choice(['Yes','No'], n, p=[0.28,0.72]),
    'WorkLifeBalance': np.random.randint(1, 5, n),
    'JobSatisfaction': np.random.randint(1, 5, n),
    'PerformanceRating': np.random.choice([1,2,3,4], n, p=[0.05,0.15,0.65,0.15]),
    'DistanceFromHome': np.random.randint(1, 30, n),
    'EmployeeNumber': range(1, n+1)
}

df = pd.DataFrame(data)
df['DiversityFlag'] = np.where(df['Gender']=='Female', 'Diverse', 'Majority')
df.to_csv('data/hr_analytics_data.csv', index=False)
print(f"✅ Generated {n} employee records → data/hr_analytics_data.csv")
