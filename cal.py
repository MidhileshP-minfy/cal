def add(*num):
    val=0
    for i in range(len(num)):
        val+=num[i]
    return val
def sub(*num):
    val=0
    for i in range(len(num)):
        val-=num[i]
    return val
def mul(*num):
    val=1
    for i in range(len(num)):
        val*=num[i]
    return val
def div(*nums):
    try:
        return nums[0]/nums[1]
    except ZeroDivisionError:
        print("Error:Zero cannot divide any number")


while True:
    try:

        print("Available operations:\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exit")
        choice = input("\nEnter the operation (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        numbers=int(input("Enter number of inputs"))
        nums=[]
        for i in range(numbers):
            nums.append(float(input("Enter the value:")))
    
        val=0
        if choice == '1':
            print(f"The result is: {add(*nums)}")
        elif choice == '2':
            print(f"The result is: {sub(*nums)}")
        elif choice == '3':
            print(f"The result is: {mul(*nums)}")
        elif choice == '4':
            print(f"The result is: {div(*nums)}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("Exiting in middle")
        break
    

           
