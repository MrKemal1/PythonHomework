def calculator():
    while True:
        number1=int(input("Please enter first number: "))
        number2=int(input("Please enter second number: "))
        sign=input("Please enter sign (+ - * /): ")

        if sign == "+":
            result= number1+number2
            break
        elif sign == "*":
            result=number1*number2
            break
        elif sign == "-":
            result=number1-number2
            break
        elif sign == "/":
            
            if number2==0:
                print("Any number is not divisible by zero")
            else:
                result = number1/number2
                break
        else:
            print("Invalid operation type")
    return result
    


calculator()






