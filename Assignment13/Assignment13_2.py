class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.Name = 0
        self.Ammount = 0

    def deposit(self):
        print("Enter a ammount to diposite : ")
        self.Ammount = float(input(""))
        
    def withdraw(self):
        print("Enter Ammount to be withdraw : ")
        self.Ammount = float(input(""))

    def CalculateInterest(self):
        print("Interest is : ",(self.Ammount/100)*BankAccount.ROI )

        
    def display(self):
        print("Ammount is : ",self.Ammount)
        print("Account Holder Name is : ", self.Name)
        
def main(): 
    Obj1 = BankAccount()
    Obj1.deposit()
    
    Obj2 = BankAccount()
    Obj2.withdraw()
    
    Obj2.CalculateInterest()

if __name__ == '__main__':
    main()
