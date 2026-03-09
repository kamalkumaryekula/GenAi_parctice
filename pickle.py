import pickle

employee_data = {
    "id": 12345,
    "name": "kamal",
    "salary": 900000
}

with open("employee_data.pkl", "wb") as f:
    pickle.dump(employee_data, f)

with open("employee_data.pkl", "rb") as f:
    loaded_employee_data = pickle.load(f)

print(loaded_employee_data)
#{'id': 12345, 'name': 'kamal', 'salary': 900000}