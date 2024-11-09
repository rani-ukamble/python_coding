account_number = int(input("account_number: "))
account_balance = int(input("account_balance: "))
salary = int(input("salary: ")) 
loan_type = input("loan_type: ")
loan_amount_expected = int(input("loan_amount_expected: "))
customer_emi_expected = int(input("customer_emi_expected: "))

# The account number should be of 4 digits and its first digit should be 1.
s_acnum = str(account_number)
if len(s_acnum)==4 and s_acnum[0]=='1':
    # The customer should have a minimum balance of Rupees 1 Lakh in the account.
    if account_balance>=100000:
        if salary>25000 and loan_type=="car":
            print("Account number eligible and \n Eligible Loan Amount will be 500000 and EMI that the bank can provide is  36")
        elif salary>50000 and loan_type=="house":
            print("Account number eligible and \n Eligible Loan Amount will be 600000 and EMI that the bank can provide is  60")
        elif salary>75000 and loan_type=="bussiness":
            print("Account number eligible and \n Eligible Loan Amount will be 750000 and EMI that the bank can provide is  84")
        else:
            print("Not applicable ")



