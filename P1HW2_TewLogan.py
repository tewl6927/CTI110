Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# This program calculates and displays travel expenses
... 
... # 10/3/23
... 
... # CTI-110 P1HW2 - Travel Expense
... 
... # Logan Tew
... 
... #
>>> 
>>> 
>>> print("The program calculate and display travel expenses")
... #taking input budget from user
... budget=float(input("Enter the budget: "))
... #taking input destination from user
... dest=input("Enter your travel destination: ")
... #taking input fuel from user
... gas=float(input("How much do you think will spend on gas? "))
... #taking input accomodation from user
... hotel=float(input("Approximately, how much will you need for accomodation/hotel? "))
... #taking input food from user
... food=float(input("Last how much do you need for food? "))
... #printing travel expenses
... print("---------Travel Expenses-----------")
... #printing Location and budget
... print("Location: ",dest)
... print("Initial Budet: ",budget)
... #moving cursor to next line as per question
... print("\n");
... #printing fuel,Accomodation,Food
... print("Fuel: ",gas)
... print("Accomodation: ",hotel)
... print("Food: ",food)
... #calculating total_expense
... total_expense=gas+hotel+food
... #calculating Remaining Balance
... rem=budget-total_expense
... #moving cursor to next
... print("\n");
... #printing Remaining Balance
