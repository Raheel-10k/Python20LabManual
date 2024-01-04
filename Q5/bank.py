import time
import random
def get_account_number():
    while True:
        account_no = int(input("Enter your card number: "))
        if 10000000 <= account_no <= 99999999:
            return account_no
        else:
            print("Account number should be of 8 mnumbers :) \n")
def withdraw_money(balance):
    while True:
        money = float(input("\nEnter the money you want to withdraw ₹"))
        if money > balance:
            time.sleep(1)
            print("\nYour balance is lower than the amount you want to withdraw")
        elif money < 100:
            print("Minimal amount should be ₹100")
        else:
            return money
def deposit_money(balance):
    money = float(input("\nEnter the amount you want to deposit ₹"))
    return balance + money
def transfer_money(balance, account_no):
    while True:
        money = float(input("\nEnter the amount you want to transfer : ₹"))
        ac = float(input("\nEnter the account you want to transfer to "))
        if ac == account_no:
            print("\nCan't send money to yourself, can you? \n")
        elif not (10000000 <= ac < 99999999):
            print("\nAccount no. should be of 8 digits\n")
        elif money > balance or money < 100:
            if money > balance:
                print("Not enough money in your account.")
            else:
                print("Minimal transfer amount is ₹100")
        else:
            time.sleep(2)
            balance -= money
            print(f"\nTransferred amount ₹ {money:.3f} To Account with account no: {int(ac)}\n")
            print(f"Your bank now has ₹ {balance:.3f}")
            return balance