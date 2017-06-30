#Calculates Monthly Expenses and divides them in half.  Calculating a half for yourself and half for Elisha.

#Internet
#car insurance
#energy bill
#phone bill 
#rent

def payBills():
    internet = raw_input("Please enter the total for your internet bill: ")
    carI = raw_input("Please enter the total for your car insurance: ")
    energy = raw_input("Please enter the total for your energy bill: ")
    phone = raw_input("Please enter the total for your phone bill: ")
    rent = raw_input("Please enter the total for your rent: ")
    misc = raw_input("Do you want to add another expense? Y or N: ")
    month = raw_input("What month and year is this for?: ")
    otherBill = 0
    while misc == 'Y':
        other = raw_input("Please enter a name for this bill: ")
        otherBill = raw_input("How much is this bill? : ")
        misc = raw_input("Do you want to add another expense? Y or N: ")
    
    total = float(internet) + float(carI) + float(energy) + float(phone) + float(rent) + float(otherBill) + float(otherBill)
    print("The total expenses for this month are ", total)
    print("Elisha's total for this month is ", total/2)
    
    extra = raw_input("Do you want to add another expense for yourself? ")
    while extra == 'Y':
        extraName = raw_input("Please enter a name for this bill: ")
        extraBill = raw_input("How much is this bill? : ")
        extra = raw_input("Do you want to add another expense? Y or N: ")
        print("Joseph your total this month is ", total/2 + float(extraBill))
    print("Thank you and Goodbye")
    


payBills()



