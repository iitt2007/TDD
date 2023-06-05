import unittest
import json

class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

class CompanyData:
    def __init__(self, id, name, store_size, employees):
        self.id = id
        self.name = name
        self.store_size = store_size
        self.employees = employees

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        company_id = data['id']
        name = data['properties']['name']
        store_size = data['properties']['store_size']

        employees = []
        for emp in data['employees']:
            emp_id = emp['emp_id']
            emp_name = emp['emp_name']
            employee = Employee(emp_id, emp_name)
            employees.append(employee)

        return cls(company_id, name, store_size, employees)

class TestCompanyData(unittest.TestCase):
    def test_from_json(self):
        json_data = '''
        {
            "id": 1001,
            "properties": {
                "name": "ABC Pvt Ltd",
                "store_size": "Medium"
            },
            "employees": [
                {
                    "emp_id": 1001,
                    "emp_name": "Divesh"
                },
                {
                    "emp_id": 1002,
                    "emp_name": "Rajesh"
                },
                {
                    "emp_id": 1003,
                    "emp_name": "David"
                }
            ]
        }
        '''

        company = CompanyData.from_json(json_data)

        # Assert the properties of the company object
        self.assertEqual(company.id, 1001)
        self.assertEqual(company.name, "ABC Pvt Ltd")
        self.assertEqual(company.store_size, "Medium")

        # Assert the employee data
        self.assertEqual(len(company.employees), 3)
        self.assertEqual(company.employees[0].emp_id, 1001)
        self.assertEqual(company.employees[0].emp_name, "Divesh")

if __name__ == '__main__':
    unittest.main()
