# Created a program to process a sales file. (main.py)
# 2 November 2025
# CSC 121 M5Lab
# Mariah Mitchell


import m5lab_FileProcessing_Functions_MariahMitchell as fn

def part1():
    #Part 1: Calculate total sales per product.
    data = fn.read_sales_data("sales.csv")
    totals = fn.total_sales_by_product(data)
    print("\nProduct ID      Total Sales")
    print("-" * 30)
    for pid, total in totals.items():
        print(f"{pid:<15}${total:.2f}")
    fn.write_totals_to_csv("total_sales.csv", totals, "Product ID", "Total Sales")
    print("\nFile 'total_sales.csv' created.")


def part2():
    #Part 2: Calculate total sales per customer.
    data = fn.read_sales_data("sales.csv")
    totals = fn.total_sales_by_customer(data)
    print("\nCustomer ID     Total Sales")
    print("-" * 30)
    for cid, total in totals.items():
        print(f"{cid:<15}${total:.2f}")
    fn.write_totals_to_csv("cus_total.csv", totals, "Customer ID", "Total Sales")
    fn.write_totals_to_txt("cus_total_txt.txt", totals, "Customer ID", "Total Sales")
    print("\nFiles 'cus_total.csv' and 'cus_total_txt.txt' created.")


def part3_lookup_product():
    #Part 3: Look up product total sales.
    part1()  #total_sales.csv
    prod = input("\nEnter Product ID to look up: ")
    result = fn.lookup_total("total_sales.csv", prod)
    if result:
        print(f"Product {prod} total sales = {result}")
    else:
        print("Product not found.")


def part4_lookup_customer():
    #Part 4: Look up customer total sales.
    part2()  #  cus_total.csv
    cust = input("\nEnter Customer ID to look up: ")
    result = fn.lookup_total("cus_total.csv", cust)
    if result:
        print(f"Customer {cust} total sales = {result}")
    else:
        print("Customer not found.")


def main():
    """
    Menu-driven main program without using while True.
    Returns
    -------
    None.

    """
    choice = 0
    while choice != 5:
        print("\n--- SALES MENU ---")
        print("1) Read file and Calculate Total Sales (write to csv file)")
        print("2) Calculate Sales Per Customer and Write to 'cus_total' txt file")
        print("3) Lookup Product Sales")
        print("4) Lookup Total Sales for Customer")
        print("5) Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            part1()
        elif choice == 2:
            part2()
        elif choice == 3:
            part3_lookup_product()
        elif choice == 4:
            part4_lookup_customer()
        elif choice == 5:
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

#Program start
main()