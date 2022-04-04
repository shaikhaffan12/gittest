# bank_acc = 40
# transaction = input("What do You Want: ")

def bank(a):
    if a==0:
        return 1
    else:
        data = {'acc':0}
        transaction = input("What do You Want: ")
        if transaction == 'd' or transaction == 'D':
            deposit = int(input("How Much Amount You Want To Deposite: "))
            data['acc'] += deposit 

        if transaction == 'w' or transaction == 'W':
            withdraw = int(input("How Much Amount You Want To Withdraw: "))
            data['acc'] =  withdraw - data['acc']

    print("your Account Balance Is :",data['acc'])
    return bank(a-1)

bank(2)