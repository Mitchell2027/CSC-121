#Program manages company employees and departments. (Main.py)
#Mariah Mitchell
#CSC-121
#28 Oct 2025

import m4Pro_Mariah_Mitchell_Functions as fn
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
    choice = menu()
    # While loop that allows users input for 8 selections.
    while choice != "8":
        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            fn.get_employee_info(emp_id)

        elif choice == "2":
            emp_id = input("Enter Employee ID: ").strip()
            fn.get_employee_department(emp_id)

        elif choice == "3":
            dept_name = input("Enter Department Name: ").strip()
            fn.get_department_info(dept_name)

        elif choice == "4":
            dept_name = input("Enter Department Name: ").strip()
            fn.calculate_department_payroll(dept_name)

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



