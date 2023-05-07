
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm : "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Child tickets are ₹50.")
    elif age <= 18:
        bill = 100
        print("Youth tickets are ₹100.")
    else:
        bill = 200
        print("Adult tickets are ₹200.")

    wants_photo = input("Do you want a photo taken? y or n. ")
    if wants_photo == "y":
        bill += 10

    print(f"Your final bill is ₹{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
