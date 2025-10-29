expenses=[] 
def add_expense():
    print("add new expense")
    name=input("enter expense name:")
    category=input("enter category(e.g,food,travel,shopping):")
    amount=float(input("enter amount:"))
    expenses.append(expenses)
    print("expense added successfully!")
def view_expenses():
    print("view all expenses yet!")
    if len(expenses)==0:
        print("no expenses recorded yet!")
    else:
        print(f"{'name':<15} {'category':<15}{'amount':<10}")
        print("_"*40)
        for expenses in expenses:
            print(f"{expenses[0]:<15}{expenses[1]:<15}{expenses[2]:<10.2f}")
            print()
def show_summary():
    print("expense summary")
    if len (expenses)==0:
        print("not expense recorded yet")
        return
    total=0
    category_total={}
    for expense in expenses:
        name,category,amount=expense
        total+=amount
        if category in category_total:
            category_total[category]+=amount
        else:
            category_total[category]=amount
    print(f" total spending:rupees{total:2f}")
    print("category_wise breakdown:")
    for category,amount in category_total.items():
        print(f"{category}:rupees{amount:2f}")
    print()
def exit_program():
    print("thank you for using personal expense tracker! ")
    exit()
def main():
    while True:
        print("personal expense tracker")
        print("1. add expense")
        print("2.view expense")
        print("3. summary")
        print("4. exit")
        choice=input("enter your choice(1-4):")
        if choice=='1':
            add_expense()
        elif choice=='2':
            view_expenses()
        elif choice=='3':
            show_summary()
        elif choice=='4':
            exit_program()
        else:
            print("invalid choice! please try again!") 
if"__name__"=="__main__":
    main()
print(add_expense())
    
    
            


