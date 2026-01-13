#Program a user entry multiplication table from numbers 1 to 20
#9 Sep 2025 
#CSC121 m1Lab2-Review
#Mariah Mitchell

#Ask to enter number; Use a while loop to enter another number
keep_going = "yes"
while keep_going == "yes":
    num = input("Enter number (between 1 and 20 only): ")
    
    num = int(num)
    #Validate the loop of numbers 1 to 20
    if num < 1:
        print("Invalid entry. Number must be greater than 1")
    elif num > 20:
        print("Invalid entry. Number must be 20 or less.")
    else:
        #Calculate and display the multiplication table
        for x in range(1,11):
            product = num * x
            print(f"{num} x {x} = {product}")
    #Ask the user for another number entry   
    keep_going = input("Do you want to enter another number? (yes to run again): ")
    
#Exit the program    
print("program terminated!")