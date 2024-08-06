name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
mobile = input("Enter Your Phone No: ")
gmail = input("Enter Your Gmail: ")

if not name.isalpha():
    print("ENTER VALID NAME")
elif age <= 0:
    print("ENTER VALID AGE")
elif not mobile.isdigit() or len(mobile) < 10:
    print("ENTER VALID PHONE NO")
elif "@" not in gmail or "." not in gmail:
    print("ENTER VALID GMAIL")
else:
    with open('test.txt', 'w') as f:   #In the place of test.txt ENTER the name of your text file
        f.write(f"NAME: {name}\n")
        f.write(f"AGE: {age}\n")
        f.write(f"MOBILE: {mobile}\n")
        f.write(f"GMAIL: {gmail}\n")
