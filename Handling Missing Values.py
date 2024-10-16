import numpy as np
import pandas as pd

#Making the dataset 

employee_data = {
    'Age': [30, 26, np.nan, 40, np.nan, 35, 45],
    'Salary': [60000, np.nan, 55000, 72000, 68000, np.nan, 75000],
    'Department': ['HR', 'Finance', np.nan, 'IT', 'Finance', 'IT', 'HR']
}

df = pd.DataFrame(employee_data)
# print(df)

# Mean Imputation

mean_imputed_age = df["Age"].mean()
mean_imputed_salary = df["Salary"].mean()
# print(mean_imputed_age)
df["Mean_Age_Imputed"] = df["Age"].fillna(mean_imputed_age)
df["Mean_Salary_Imputed"] = df["Salary"].fillna(mean_imputed_salary)
# print(df)


#Median Imputation

mediun_imputed_age = df["Age"].median()
mediun_imputed_salary = df["Salary"].median()
df["Medium_Age_Imputed"] = df["Age"].fillna(mediun_imputed_age)
df["Medium_Salary_Imputed"] = df["Salary"].fillna(mediun_imputed_salary)
# print(df)

# Mode Imputation

mode_imputed_dep = df["Department"].mode()
df["Mode_Dep_Imputed"] = df["Department"].fillna(mode_imputed_dep)
print(df)