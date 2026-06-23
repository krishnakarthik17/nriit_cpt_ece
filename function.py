balance=987654
def Check():
    global balance
    print(f"your final balance:{balance}")
    print(balance)
def Deposit(money):
    global balance
    balance+=money
    print(f"amount{money} sucessfully creideted")
    print(f"final:{balance}")
def withdraw(money):
    global balance
    balance-=money
    print(f"{money}sucessfully debited")
    print(f"final_balance:{balance}")
while True:
    n=int(input("choose option:\n1.Check\n2.deposit\n3.withdraw\n4.exit"))
    if n==1:
        Check()
    elif n==2:
        money=int(input("enter amount to deposit"))
        deposit(money)
    elif n==3:
        money=int(input("enter amount to withdraw"))
        withdraw(money)
    elif n==4:
        break
else:
    print("wrong pin")
        
            
