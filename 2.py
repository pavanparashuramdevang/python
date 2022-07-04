
flag=1
valid=True



while flag==1:
    try:
        print("-------this is a calculator program in python--------\n")

        num1=input('enter the first number\n')
        num2=input('enter the second number\n')
        op=input('enter the operator (+-*/_)\n')

        a=int(num1)
        b=int(num2)


        if (op=='+'):
            result=a+b
        elif (op=='-'):
            result=a-b
        
        elif (op=='*'):
            result=a*b

        elif (op=='/'):
            result=a/b

        else:
            valid=False

        if valid==False:
            print("enter the valid operator")
            quit=input('enter q to quit or anything to resume\n')
            if quit=='q':
                flag=0
            else:
                flag=1

        else:
            print(f"the result is {result} : {a} {op} {b} = {result}\n")
            quit=input('enter q to quit or anything to resume\n')
            if quit=='q':
                flag=0
            else:
                flag=1


       

    except ValueError:
        print("please enter integer or float values")

    except:
        print("something went wrong please check")

    else:
        print('nothing went wrong')






            




