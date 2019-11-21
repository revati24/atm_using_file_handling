import pickle
d = {'pin': 1234,'account': 2000, 'balance': 3000}
f = open("Account.pickle", 'wb+')
pickle.dump(d,f)
f.flush()
f.close()
print("data save")
f = open("Account.pickle","rb")
data = pickle.load(f)
print(data)

def withdraw(amt):
    if (amt>=100)and(amt<=data['balance'])and(amt%100==0) :
        print('withdrawal amount=',amt)
        Balance = data['balance']-amt
        print('updated balance after withdraw=',Balance)
    else:
        print("please enter amount in multiples of 100/ Account balance insufficient")
    
    
    
def deposite(amt):
    #amt = int(input('enter the amount to be deposited'))
    Balance=data['balance'] +amt
    print("deposited amount", amt)
    print("updated balance after deposite=", Balance)
    
def balance_enquiry(account):
    print("current balance", data['balance'])
    
        
for i in range(0,3):
    upin = int(input("enter pin"))
    if upin == data['pin']:
        program =(input('select catagory from : Withdraw, Deposite, Balance enquiry'))
    
    #withdraw = 1
    #Deposite = 2
    #Balance_enquiry = 3    
        if program == 'A':
            amount= int(input("enter amount to be withdraw"))
            withdraw(amount)
        elif program == 'B':
            amount = int(input("enter amount to be deposited"))
            deposite(amount)
        elif program == 'C':
            account_no = int(input("enter account no"))
            if account_no == data['account']:
                balance_enquiry(account_no)
            else:
                print("please enter correct account")
        else:
            print("exit")
    else:
        print("incorrect pin, try again")
        
        
