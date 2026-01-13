#Program manages company employees and departments with writing txt and csv files (functions.py)
#Mariah Mitchell
#CSC-121
#11 Nov 2025

import csv

company_db = {
    "engineering": {
        "department_info": {
            "name": "Engineering",
            "budget": 2500000,
            "manager": "emp_001",
            "location": "Building A, Floor 3"
        },
        "employees": {
            "emp_001": {
                "personal_info": {
                    "name": "Sarah Chen",
                    "email": "sarah.chen@company.com",
                    "phone": "555-0101",
                    "hire_date": "2020-03-15",
                    "position": "Engineering Manager",
                    "employee_id": "emp_001",
                    "salary": 115000
                }},
            "emp_002": {
                "personal_info": {
                    "name": "Marcus Johnson",
                    "email": "marcus.johnson@company.com",
                    "phone": "555-0102",
                    "hire_date": "2021-06-01",
                    "position": "Senior Software Engineer",
                    "employee_id": "emp_002",
                    "salary": 105000
                }},
            "emp_003": {
                "personal_info": {
                    "name": "Emily Rodriguez",
                    "email": "emily.rodriguez@company.com",
                    "phone": "555-0103",
                    "hire_date": "2022-09-12",
                    "position": "Software Engineer",
                    "employee_id": "emp_003",
                    "salary": 88000
                }}
        }
    },
    "marketing": {
        "department_info": {
            "name": "Marketing",
            "budget": 1200000,
            "manager": "emp_004",
            "location": "Building B, Floor 2"
        },
        "employees": {
            "emp_004": {
                "personal_info": {
                    "name": "David Park",
                    "email": "david.park@company.com",
                    "phone": "555-0201",
                    "hire_date": "2019-08-20",
                    "position": "Marketing Director",
                    "employee_id": "emp_004",
                    "salary": 128000
                }},
            "emp_005": {
                "personal_info": {
                    "name": "Lisa Thompson",
                    "email": "lisa.thompson@company.com",
                    "phone": "555-0202",
                    "hire_date": "2021-11-08",
                    "position": "Digital Marketing Specialist",
                    "employee_id": "emp_005",
                    "salary": 74000
                }}
        }
    },
    "finance": {
        "department_info": {
            "name": "Finance",
            "budget": 800000,
            "manager": "emp_006",
            "location": "Building A, Floor 1"
        },
        "employees": {
            "emp_006": {
                "personal_info": {
                    "name": "Robert Kim",
                    "email": "robert.kim@company.com",
                    "phone": "555-0301",
                    "hire_date": "2018-04-10",
                    "position": "Finance Manager",
                    "employee_id": "emp_006",
                    "salary": 122000
                }},
            "emp_007": {
                "personal_info": {
                    "name": "Jennifer Wu",
                    "email": "jennifer.wu@company.com",
                    "phone": "555-0302",
                    "hire_date": "2023-02-15",
                    "position": "Financial Analyst",
                    "employee_id": "emp_007",
                    "salary": 70000
                }}
        }
    }
}
def validate_employee_id(emp_id):
    """
    Validates the  format structure of an employee ID

    Parameters
    ----------
    emp_id : str
        The employee ID entered by the user (case-insensitive).

    Returns
    -------
    str or None
        Returns the corrected employee ID if valid.
        Returns None if the ID is not valid.
    """

    # Convert to lowercase 
    emp_id = emp_id.lower()

    # Must start with "emp"
    if not emp_id.startswith("emp"):
        print("Invalid ID: The ID must start with 'emp'.")
        return None

    
    # Must contain an underscore after emp
    
    if len(emp_id) < 4 or emp_id[3] != "_":
        print("Invalid ID: The characters 'emp' must be followed by an underscore '_'.")
        return None

    
    # Must have exactly 3 digits after the underscore
    
    digits = emp_id[4:]

    if len(digits) != 3:
        print("Invalid ID: The ID must end with exactly 3 digits.")
        return None

    if not digits.isdigit():
        print("Invalid ID: The last three characters must be digits (0–9).")
        return None

    
    return emp_id

def find_employee(employee_id):
    """
    find an employee and their department

    Parameters
    ----------
    employee_id : str
        The ID of the employee to find.

    Returns
    -------
    tuple
        (department_name, employee_info) or (None, None).

    """
    #Loop for each department in database
    for dept_name, dept_data in company_db.items():
        #Safely access the employees dictionary with ID
        employee = dept_data.get("employees", {}).get(employee_id)
        # If employee exist, return department name and personal info
        if employee:
            return dept_name, employee.get("personal_info", {})
    return None, None



def get_employee_info(employee_id):
    """
    Display all information for a specific employee
    Parameters
    ----------
    employee_id : str
        The employee ID entered by the user.
    Returns
    -------
    None

    """
    employee_id = employee_id.lower()
    
    dept_name, emp = find_employee(employee_id)
    if emp:
        # Access employee name
        print(f"\nEmployee Information for {emp['name']}")
        print("-" * 40)
        # Display all personal information except the ID
        for k, value in emp.items():
            if k != "employee_id":
                print(f"{k.capitalize().replace('_', ' ')}: {value}")
        # Display department name
        print(f"Department: {dept_name.title()}")
    else:
        print("No such employee found.")


def get_employee_department(employee_id):
    """
    Displays the department name where employee works.
    Parameters
    ----------
    employee_id : str
        The ID of the employee.

    Returns
    -------
    None.

    """
    # Find the employee and department using helper function
    dept_name, emp = find_employee(employee_id)
    if emp and dept_name:
        # Safely access department data using .get()
        dept_data = company_db.get(dept_name, {})
        dept_info = dept_data.get("department_info", {})

        # retrieve fields with defaults
        emp_name = emp.get("name", "N/A")
        dept_full_name = dept_info.get("name", "Unknown Department")
        location = dept_info.get("location", "Unknown Location")

        print(f"\nEmployee {emp_name} works in the {dept_full_name} Department located at {location}.")

    else:
        print("No such employee found.")

def get_department_info(department_name):
    """
    Displays department budget, location, manager ID, and manager name.

    Parameters
    ----------
    department_name : str
        The name of the department.

    Returns
    -------
    None.
    """
    # Convert department name to lowercase
    dept_key = department_name.lower()
    dept = company_db.get(dept_key)
    # Check if the department exist
    if not dept:
       print("No such department found.")
       return

   # Safely retrieve department info and employees
    info = dept.get("department_info", {})
    employees = dept.get("employees", {})
     
    # Safely get manager ID and manager information
    manager_id = info.get("manager", "Unknown Manager ID")
    manager_info = employees.get(manager_id, {}).get("personal_info", {})
    manager_name = manager_info.get("name", "Unknown Manager")
     
    # Safely get other department details
    dept_name = info.get("name", "Unknown Department")
    location = info.get("location", "Unknown Location")
    budget = info.get("budget", 0.0)
     
    # Display Department info with budget
    print(f"\nDepartment: {dept_name}")
    print("-" * 40)
    print(f"Location: {location}")
    print(f"Budget: ${budget:,.2f}")
    print(f"Manager ID: {manager_id}")
    print(f"Manager Name: {manager_name}")

def calculate_department_payroll(department_name):
    """
    Calculate and display total payroll for a department

    Parameters
    ----------
    department_name : str
        The name of the department whose payroll will be calculated.

    Returns
    -------
    None.
    """
    # Converts department name to lowercase
    dept_key = department_name.lower()
    # Retrieve the department dictionary from the company database
    dept = company_db.get(dept_key)
    if not dept:
        print("No such department found.")
        return
    employees = dept["employees"]

    # Build the file name (engineering.csv for Engineering)
    filename = dept_key + ".csv"

    # Prepare payroll values
    total_salary = 0

    # Write CSV file
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
    
            # Header row
            writer.writerow(["Employee ID", "Employee Name", "Salary"])
    
            # Write each employee row
            for emp_id, data in employees.items():
                info = data["personal_info"]
                name = info["name"]
                salary = info["salary"]
    
                total_salary += salary
    
                writer.writerow([emp_id, name, f"${salary:,.2f}"])
    
            # Write total payroll row
            writer.writerow(["", "Total Payroll", f"${total_salary:,.2f}"])
    
            # Display confirmation
            print("-" * 40)
            print(f"{'Total Payroll:':<55}${total_salary:,.2f}")
            print(f"\nPayroll file '{filename}' has been created.")
    except IOError:
        print("Error: Could not create highest_paid.csv.")
        return


def get_salary_statistics(department_name):
    """
    Displays min, max, and average salary for a department.
    
    Parameters
    ----------
    department_name : str
        The name of the department to analyze.

    Returns
    -------
    None.

    """
    # Convert the department to lowercase
    dept_key = department_name.lower()
    # Retrieve the department information from the company database
    dept = company_db.get(dept_key)
    if not dept:
        print("No such department found.")
        return
    
    employees = dept["employees"]

    # Extract salaries with employee info
    salary_list = []
    for emp_id, data in employees.items():
            info = data["personal_info"]
            salary_list.append({
                "id": emp_id,
                "name": info["name"],
                "salary": info["salary"]
            })
        
    if not salary_list:
            print("No employees found in this department.")
            return
        
        # Calculate statistics
    min_emp = min(salary_list, key=lambda x: x["salary"])
    max_emp = max(salary_list, key=lambda x: x["salary"])
    avg_salary = sum(emp["salary"] for emp in salary_list) / len(salary_list)
    
        # Create txt file name 
    filename = dept_key + "_statistics.txt"
    
    # Write to file
    try:
        with open(filename, "w") as file:
            # Centered title 
            title = f"{department_name.title()} Statistics"
            file.write(title.center(80) + "\n")
            file.write("-" * 80 + "\n") 
            # Lowest salary
            file.write(f"Lowest Salary: ${min_emp['salary']:,.2f} "
                       f"(ID: {min_emp['id']}, Name: {min_emp['name']})\n")
            # Highest salary
            file.write(f"Highest Salary: ${max_emp['salary']:,.2f} "
                       f"(ID: {max_emp['id']}, Name: {max_emp['name']})\n")
            # Average salary
            file.write(f"Average Salary: ${avg_salary:,.2f}\n")
        
        print(f"\nSalary statistics file '{filename}' has been created.")
    
    except IOError:
        print("Error: Unable to write statistics file.")
        return

def find_highest_paid_employees(n=2):
    """
    Display the top N highest-paid employees across all departments.
    
    Parameters
    ----------
    n : int
        The number of top paid employess to display. The default is 2.

    Returns
    -------
    None.

    """
    # CSV FILE
    with open("highest_paid.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Header row
        writer.writerow(["Dep Name", "EmpId", "Employee Name", "Position", "Salary"])

        # Loop through departments
        for dept_name, dept_info in company_db.items():
            employees = dept_info["employees"]

            # Build list of employee info
            salary_list = []
            for emp_id, data in employees.items():
                info = data["personal_info"]
                salary_list.append({
                    "id": emp_id,
                    "name": info["name"],
                    "position": info["position"],
                    "salary": info["salary"]
                })

            # Sort employees by highest salary
            top_two = sorted(salary_list, key=lambda x: x["salary"], reverse=True)[:2]

            # Write top 2 to CSV
            for emp in top_two:
                writer.writerow([
                    dept_name.title(),
                    emp["id"],
                    emp["name"],
                    emp["position"],
                    f"${emp['salary']:,.2f}"
                ])

    #  TXT FILE 
    with open("highest_paid.txt", "w") as txtfile:

        # Header row with spacing
        header = f"{'Dep Name':15} {'EmpId':10} {'Employee Name':25} {'Position':20} {'Salary':10}"
        txtfile.write(header + "\n")
        txtfile.write("-" * len(header) + "\n")

        # Loop through departments again
        for dept_name, dept_info in company_db.items():
            employees = dept_info["employees"]

            salary_list = []
            for emp_id, data in employees.items():
                info = data["personal_info"]
                salary_list.append({
                    "id": emp_id,
                    "name": info["name"],
                    "position": info["position"],
                    "salary": info["salary"]
                })

            # Sort highest to lowest and take top 2
            top_two = sorted(salary_list, key=lambda x: x["salary"], reverse=True)[:2]

            # Write rows to TXT
            for emp in top_two:
                row = (
                    f"{dept_name.title():15}"
                    f"{emp['id']:10}"
                    f"{emp['name']:25}"
                    f"{emp['position']:20}"
                    f"${emp['salary']:,.2f}"
                )
                txtfile.write(row + "\n")

    print("\nFiles 'highest_paid.csv' and 'highest_paid.txt' have been created.")


def generate_department_report(department_name):
    """
    Generate comprehensive department report
    
    Parameters
    ----------
    department_name : str
        The name of the department to report.

    Returns
    -------
    None.

    """
    # Convert department name to lowercase
    dept_key = department_name.lower()

    # Retrieve department info from the database
    dept = company_db.get(dept_key)
    if not dept:
        print("No such department found.")
        return  

    # Retrieve all employees safely using 
    employees = dept.get("employees", {})
    if not employees:
        print("No employees found in this department.")
        return  # Exit if no employees exist

    # Calculate total payroll by summing all employee salaries
    total_payroll = sum(emp.get("personal_info", {}).get("salary", 0.0)for emp in employees.values())

    # Calculate average salary (avoid division by zero)
    avg_salary = total_payroll / len(employees) if employees else 0.0

    # Display formatted department report
    print(f"\nComprehensive Report for {department_name.title()} Department")
    print("-" * 40)
    print(f"Employee Count: {len(employees)}")
    print(f"Total Payroll: ${total_payroll:,.2f}")
    print(f"Average Salary: ${avg_salary:,.2f}")
    print("-" * 40)
