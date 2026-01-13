# Created a program to process a sales file. (functions.py)
# 2 November 2025
# CSC121 M5Lab
# Mariah Mitchell

import csv

def read_sales_data(filename):
    """
    Read sales data from the CSV file and return as a list.
    Parameters
    ----------
    filename : str
        Path to the CSV file containing sales data.

    Returns
    -------
    sales_list : list of dictionary.
       Each dictionary represents a row in the CSV with column names as keys.
    """
    with open('sales.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        sales_list = [row for row in reader]
    return sales_list


def total_sales_by_product(sales_list):
    """
    Calculate total sales for each product.
    Parameters
    ----------
    sales_list : list of dict
        Each dictionary contains a sale with keys 'prodID', 'units', and 'price'.

    Returns
    -------
    product_totals : dict
        Keys are product IDs and values are total sales (float) for each product.

    """
    product_totals = {}
    for sale in sales_list:
        prod_id = sale["prodID"]
        total = float(sale["units"]) * float(sale["price"])
        if prod_id in product_totals:
            product_totals[prod_id] += total
        else:
            product_totals[prod_id] = total
    return product_totals


def total_sales_by_customer(sales_list):
    """
    Calculate total sales per customer.
    Parameters
    ----------
    sales_list : list of dict
        Each dictionary contains a sale with keys custID, units, and price.

    Returns
    -------
    cust_totals : dict
        Keys are customer IDs and values are total sales (float) for each customer.

    """
    cust_totals = {}
    for sale in sales_list:
        cust_id = sale["custID"]
        total = float(sale["units"]) * float(sale["price"])
        if cust_id in cust_totals:
            cust_totals[cust_id] += total
        else:
            cust_totals[cust_id] = total
    return cust_totals


def write_totals_to_csv(filename, totals, header1, header2):
    """
    Write totals dictionary to a CSV file.
    Parameters
    ----------
   filename : str
        The path to the output CSV file.
    totals : dict
        Dictionary with keys as IDs (product or customer) and values as totals (float).
    header1 : str
        Column header for the first column ('Product ID' or 'Customer ID').
    header2 : str
        Column header for the second column ( 'Total Sales').

    Returns
    -------
    None.

    """
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([header1, header2])
        for k, v in totals.items():
            writer.writerow([k, f"${v:.2f}"])


def write_totals_to_txt(filename, totals, header1, header2):
    """
    Write totals dictionary to a text file with headers.
    Parameters
    ----------
    filename : str
        The path to the output text file.
    totals : dict
        Dictionary with keys as IDs (product or customer) and values as totals (float).
    header1 : str
        Header for the first column ('Product ID' or 'Customer ID').
    header2 : str
        Header for the second column ('Total Sales').


    Returns
    -------
    None.

    """
    with open(filename, "w") as f:
        f.write(f"{header1:<15}{header2}\n")
        f.write("-" * 30 + "\n")
        for key, value in totals.items():
            f.write(f"{key:<15}${value:.2f}\n")


def lookup_total(filename, search_id):
    """
    Look up a total in a CSV file by key.
    Parameters
    ----------
    filename : str
        Path to the CSV file containing totals.
    search_id : str or int
        The ID to search for in the first column..

    Returns
    -------
    str
        The total associated with the search_id as a string ('$123.45').
        Returns None if the search_id is not found.


    """
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        next(reader)  # skip header
        for row in reader:
            if row[0] == str(search_id):
                return row[1]
    return None