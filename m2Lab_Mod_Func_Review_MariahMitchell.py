#Dollar store program as a modularized menu
#14 Sep 2025 
#CSC121 m2Lab- Modularized Function Review
#Mariah Mitchell


def main():
    """
    Function ask user to enter number of items, if 0 than terminate. Menu is displayed
    
    Returns
    -------
    None.

    """
    #Created a menu
    choice = 0
    while choice != 2:
        
        print("-----Menu-------")
        print("1) Enter a Number")
        print("2) Exit")
        print("----------------")
        print()
        
        choice = int(input("Enter choice:"))
        #Ask user to input number of items
        if choice == 1:
            items = 1
            if items != 0:  
                items = int(input("Enter number of items: "))
        
                if items == 0:
                    print("Program terminated.")
                    break
                #Calculate the cost and tax    
                cost = calcCost(items)
                tax = cost * 0.075
                    
                display(cost, tax)
                print()
                
        elif choice ==2:
            print("Program terminated.\n")
            return
        else:
            print("Invalid Entry.\n")

def calcCost(count):
    """
    Calculate the total cost of items, applying a 5% discount if 10 or more items.
    
    Parameters
    ----------
    count : int
                The number of items purchased
    Returns
    -------
    cost : float
                The total cost after applying discount
    """
    cost = count
    #if count is over 10 add a discount
    if count >= 10:
        cost = cost - (cost * 0.05)
    return cost


def displayLine(label, amount):
    """
    Displays a single line with a label and a numeric amount formatted to 2 decimal
    places.
    
    Parameters
    ----------
    label : string
                The label text to display before the number
    amount : fLoat
                Numeric variable formatted to two decimal places.
    Returns
    -------
    None.
    """
    print(f"{label}: {amount:.2f}")
    
    
def display(cost, tax):
    """
    Displays the net cost, tax, and total cost after tax.
    
    Parameters
    ----------
    cost : float
            The total cost before tax
    tax : float
            The calculated tax amount
    Returns
    -------
    None.
    """
    total = cost + tax
    displayLine("Net cost", cost)
    displayLine("Tax", tax)
    displayLine("After tax", total)

if __name__ == "__main__":
    main()
   
