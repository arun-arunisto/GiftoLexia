import pandas as pd

data_file = pd.read_csv("org_data.csv")

#print(data_file)

def get_employee_data(emp_id, data):
    if emp_id == 0:
        return data
    employee = data[data["id"]==emp_id]
    if employee.empty:
        return pd.DataFrame()
    result = pd.concat([pd.DataFrame(), employee])
    subordinate = data[data["manager_id"]==emp_id]
    if subordinate.empty:
        return result
    for _, row in subordinate.iterrows():
        result = pd.concat([result, get_employee_data(row["id"], data)])
    return result

def filter_employee_data(emp_id, data):
    hierarchy = get_employee_data(emp_id, data)
    return hierarchy

print(filter_employee_data(0, data_file))