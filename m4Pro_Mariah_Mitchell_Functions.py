##Program manages company employees and departments. (functions.py)
#Mariah Mitchell
#CSC-121
#28 Oct 2025


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
    # Get all employees in the database
    employees = dept.get("employees")
    if not employees:
        print("No employees found in this department.")
        return
    # Display payroll header
    print(f"\nPayroll for {department_name.title()} Department")
    print("-" * 40)
    print(f"{'Employee Name':<25}{'Position':<30}{'Salary':>15}")
    print("-" * 40)
    #Initialize totall payroll
    total = 0
    #For Loop (all employees in department)
    for emp in employees.values():
        info = emp.get("personal_info", {})
        name = info.get("name", "N/A")
        position = info.get("position", "N/A")
        salary = info.get("salary", 0.0)
        #Add employees salary to the total payroll
        total += salary
        #Display payroll
        print(f"{name:<25}{position:<30}${salary:>12,.2f}")

    print("-" * 40)
    print(f"{'Total Payroll:':<55}${total:>12,.2f}")


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
    # Use a list comprehension
    salaries = [emp["personal_info"]["salary"] for emp in dept["employees"].values()]
    #Display salary statistics
    print(f"\nSalary Statistics for {department_name.title()} Department")
    print("-" * 45)
    print(f"Minimum Salary: ${min(salaries):,.2f}")
    print(f"Maximum Salary: ${max(salaries):,.2f}")
    print(f"Average Salary: ${sum(salaries)/len(salaries):,.2f}")


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
    #creates an empty list to store employees
    all_emps = []
    # For Loop to collect employee information
    for dept_name, dept_data in company_db.items():
        for emp_data in dept_data["employees"].values():
            info = emp_data["personal_info"]
            info["department"] = dept_name.title()
            all_emps.append(info)
    # Sort all employees in descending order based on salary
    top_emps = sorted(all_emps, key=lambda e: e["salary"], reverse=True)[:n]
    # Display header and top-paid employees
    print(f"\nTop {n} Highest Paid Employees")
    print("-" * 40)
    for emp in top_emps:
        print(f"Name: {emp['name']}")
        print(f"Department: {emp['department']}")
        print(f"Position: {emp['position']}")
        print(f"Salary: ${emp['salary']:,.2f}")
        print("-" * 40)


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
