import random
from bank import *

c = random.randint(1000, 10000)
account_no = get_account_number()
print("\n\nChecking your card status please wait... \n")
time.sleep(2)
print("\nWELCOME TO ATM ")
while True:
    print("\n\nWhat would you like to do?\n1. Withdrawal\n2. Check balance\n3. Deposit money\n4. Transfer money \n5. Cancel \n")
    n = int(input())
    if n == 1:
        c -= withdraw_money(c)
        time.sleep(2)
    elif n == 2:
        print(f"\nYour account has ₹{c:.3f}\n")
    elif n == 3:
        c = deposit_money(c)
        print("Successfully deposited ")
    elif n == 4:
        c = transfer_money(c, account_no)
    elif n == 5:
        print("\nTHANK YOU...\n\n")
        exit()
    else:
        print("\nInvalid option.\n")
