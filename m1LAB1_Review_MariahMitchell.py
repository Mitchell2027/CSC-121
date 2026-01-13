#Dollar store program calculating disount and sales tax
#31 Aug 2025 
#CSC121 m1Lab1-Review
#Mariah Mitchell


#Ask user to input amount of items; from 1 to 100; 0 to quit
items = 1
while items != 0:  
    items = int(input("Enter number of items: "))

    if items == 0:
        print("Program terminated.")
        break

    #Calculate cost before discounts and tax
    gross_cost = items * 1
    
    #Apply 5% discount for 10 or more items
    discount = 0
    if items >= 10:
        discount = gross_cost * 0.05
        
    #Net_cost after discount
    net_cost = gross_cost - discount
    
    #Sales tax 7.5%
    tax = net_cost * 0.075
    
    #Cost after tax
    after_tax = net_cost + tax
    
    #Display Output
    print("")
    print(f"Gross cost: {gross_cost:.2f}")
    print(f"Disount: {discount:.2f}")
    print(f"Net cost: {net_cost:.2f}")
    print("")
    print(f"Tax: {tax:.2f}")
    print(f"After tax: {after_tax:.2f}")