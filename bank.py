class Person:

      def __init__(self,user_name, email,password):
            self.user_name=user_name
            self.email=email
            self.password=password
      def create_account(self):
            print("----------Creating Account----------- \nUsername is:"+self.user_name+"\nUser Email :"+self.email+"\nUser Password is:"+str(self.password))
            print("Account Create succesfuly\n")

class User(Person):

      def __init__(self,user_name,email, password):
            self.balance=0
            self.loan_get=0
            self.transaction_histories=[]
            self.bank_user=[]
            super().__init__(user_name,email,password)
      
      def deposite(self,amount):

            if amount > 0:

                  self.balance += amount

                  print("Deposited amount:",amount)

                  self.transaction_histories.append(f"Depsite:{amount}")
            else:
                  print("Please enter a valid amount to deposit.")

      def check_balance(self):
            print("Avaiable balance now in "+self.user_name+ " is "+ str(self.balance))

      def withdraw(self,amount):
            self.amount=amount
            if (amount<=self.balance and self.balance!=0):
                  self.balance-=amount
                  print("Widthdrawing taka:",amount)
                  self.transaction_histories.append(f"Widthdraw:{amount}")
            else:
                  print("OOPS!..Sorry sir.You have insufficient balance ")

      def transaction_history(self):
            print("Total number of Transaction ",len(self.transaction_histories))
            print(self.transaction_histories)



      def transfer_money(self,receiver,amount):
            if amount<=self.balance and self.balance!=0:

                  self.transaction_histories.append(f"transfer:{amount}")
                  self.balance-=amount
                  print(f"Transferring money from {self.user_name} to {receiver.user_name}")
                  receiver.deposite(amount)
                  print("Money Transfer Complete")


      def get_loan(self):
            loan_get=self.balance*2
            self.balance+=loan_get
            self.loan_get=loan_get
            print("getting loan:",loan_get)
            self.transaction_histories.append(f"Loan:{loan_get}")

      def bankrupt(self):
            Widthdraw=True
            if not Widthdraw:
                  print("The bank is bankrupt")





class Admin(Person):
      def __init__(self,user_name,email, password):
            self.total_account=[]
            self.user_account=[]
            self.total_loan=0
            self.bank_balance=0
            self.loan_feature=True
            self.total_available_balance=0
            super().__init__(user_name,email,password)
      

      def total_balance(self,*users):
            for i in users:
                  self.total_account.append(i)
            for account in self.total_account:
                  self.bank_balance+=account.balance
            return self.bank_balance




      def total_loan_given(self,*bank):
            if self.loan_feature==True:
                  for account in bank:
                        self.user_account.append(account)

                  for users in self.user_account:
                        if users.loan_get:
                              self.total_loan+=users.loan_get
                  return self.total_loan
            else:
                  print("Upsss!Loan feature is off")

      def on_loan_feature(self):
            self.loan_feature=True


      def off_loan_feature(self):
            self.loan_feature=False


User1=User("limon123","limonhasan@gmail.com", 42697)
User1.create_account()
User1.deposite(5000)
User1.withdraw(2000)
User1.get_loan()
User1.check_balance()
User2=User("Marouf123","Marouf@gmail.com", 14782)
User2.create_account()
User2.deposite(2000)
User2.withdraw(200)
User2.get_loan()
User2.check_balance()

User1.transfer_money(User2, 3000)
User1.transaction_history()
User2.transaction_history()

User2.check_balance()
User1.check_balance()


karim=Admin("ABC","abc@gmail" ,24574)

karim.on_loan_feature()

print("Total loan given by bank is",karim.total_loan_given(User1,User2))

print("Total available cash in the bank is",karim.total_balance(User1,User2))

karim.off_loan_feature()


