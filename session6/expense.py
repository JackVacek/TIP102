'''
You travel frequently and need to keep track of your expenses.
You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. 
At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), 
write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

'''
def calculate_expenses(expenses):
    myDict = {}
    maxSpend = 0
    which = ""
    for i in expenses:
        myDict[i[0]] = myDict.get(i[0], 0) + i[1] 
        if myDict[i[0]] > maxSpend:
            maxSpend = myDict[i[0]]
            which = i[0]
    return (myDict, which)

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))