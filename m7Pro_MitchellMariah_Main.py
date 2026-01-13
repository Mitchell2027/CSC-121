#Program of a company database using classes (Main.py)
#Mariah Mitchell
#CSC 121 0901
#12/10/2025

import m7Pro_MitchellMariah_Functions as fn

def menu():
    """
    Displays the main menu for the Company Management System and prompts the 
    user to the main menu.

    Returns
    -------
    choice : str
        The user's menu selection from 1-8.
    """
    print("\n" + "=" * 40)
    print("COMPANY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Get Employee Info")
    print("2. Get Employee Department")
    print("3. Get Department Info")
    print("4. Calculate Department Payroll")
    print("5. Get Salary Statistics")
    print("6. Find Highest Paid Employees")
    print("7. Generate Department Report")
    print("8. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-8): ").strip()
    return choice


def main():
    """
    Runs the main program, displays a menu, and calls the function based on user input.
    Returns
    -------
    None.

    """
    emp_instances, dept_instances = fn.create_instances(fn.company_db)
    
    choice = menu()
    # While loop that allows users input for 8 selections.
    while choice != "8":
        if choice == "1":
            # Option 1: Create Employee instances and write CSV
            fn.write_employee(list(emp_instances.values()))
            print("All employee instances created.")

        elif choice == "2":
            emp_id = input("Enter Employee ID: ").strip()
            valid_id = fn.validate_employee_id(emp_id)
            if valid_id:
                fn.get_employee_department(valid_id)
            else:
                print("Invalid Employee ID format.")

        elif choice == "3":
            # Ask for department name
            dept_name_input = input("Enter the department name: ").strip()
            dept_key = dept_name_input.lower()

            # Search department
            if dept_key in dept_instances:
                dept = dept_instances[dept_key]
                fn.write_department(dept)
            else:
                print(f"No department named '{dept_name_input}' found.")


        elif choice == "4":
            dept_name = input("Enter Department Name: ").strip()
            dept_key = dept_name.lower()
            
            if dept_key in dept_instances:
                dept = dept_instances[dept_key]
                emp_list = dept.get_employees()
                fn.write_employee(emp_list,dept_name)
                print(f"Employee CSV for {dept_name.title()} created.")
            else:
                print(f"Department '{dept_name}' not found.")

        elif choice == "5":
            dept_name = input("Enter Department Name: ").strip()
            fn.get_salary_statistics(dept_name)

        elif choice == "6":
            print("Displaying the 2 highest paid employees...")
            fn.find_highest_paid_employees(2)

        elif choice == "7":
            dept_name = input("Enter Department Name: ").strip()
            fn.generate_department_report(dept_name)

        else:
            print("Invalid option! Please try again.")

        choice = menu()

    print("Program will now exit. Goodbye!")


if __name__ == "__main__":
    main()



