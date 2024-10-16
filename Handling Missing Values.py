import numpy as np
import pandas as pd

#Making the dataset 

employee_data = {
    'Age': [30, 26, np.nan, 40, np.nan, 35, 45],
    'Salary': [60000, np.nan, 55000, 72000, 68000, np.nan, 75000],
    'Department': ['HR', 'Finance', np.nan, 'IT', 'Finance', 'IT', 'HR']
}

df = pd.DataFrame(employee_data)
print(df)