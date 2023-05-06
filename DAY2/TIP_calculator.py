print("Welcome to the Tip Calculator.")
bill = float(input("What is the total bill ₹"))
tip_per = int(input("How much tip would you like to give? 5,10,15,20,25,30 : "))
people = int(input("How many people split the bill? : "))
tip_as_per = tip_per / 100
total_tip = tip_as_per * bill
total_bill = bill + total_tip
bill_as_per = total_bill/people
final_bill_amount = round(bill_as_per, 2)
print(f"Each person should pay : ${final_bill_amount}")
