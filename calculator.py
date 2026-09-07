from calculatorfunction import*


while True:

     num1=int(input("Enter the Number:"))
     num2=int(input("Enter the Number:"))


     print("\n************Calculator Menu****************")
     print("\t1. Addition")
     print("\t2. Subtraction")
     print("\t3. Multiplication")
     print("\t4. Division")
     print("\t5. Quit")


     choice=int(input("Enter your choice:"))

     if (choice==1):
        result=add(num1,num2)
        print("Answer =",result)

     elif (choice==2):
         result=subtract(num1,num2)
         print("Answer =",result)

     elif (choice==3):
         result=multiply(num1,num2)
         print("Answer =",result)

     elif (choice==4):
         result=division(num1,num2) 
         print("Answer =",result)

     elif (choice==5):
         quit(0)

     else:
         print("Enter a valid choice")   
    