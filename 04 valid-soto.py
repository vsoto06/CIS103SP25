name = input("Enter name: ")

if len(name) == 0 or name.isspace():
    print("Message: Name cannot be blank")
elif len(name) < 3:
    print("Message: Name too short")
elif not name.isalpha():
    print("Message: Name must be alphabetic")

account_number = input("Enter account number: ")

if len(account_number) == 0 or account_number.isspace():
    print("Message: Account number cannot be blank")
elif not account_number.isdigit():
    print("Message: Account number must be numeric")
elif len(account_number) != 9:
    print("Message: Account number must be 9 digits")

payment_amount = input("Enter payment amount: ")

if len(payment_amount) == 0 or payment_amount.isspace():
    print("Message: Payment cannot be blank")
elif payment_amount.count(".") > 1 or not payment_amount.replace(".", "", 1).isdigit():
    print("Message: Payment must be numeric")
elif float(payment_amount) < 0:
    print("Message: Payment cannot be negative")
elif float(payment_amount) == 0:
    print("Message: Payment cannot be zero")
