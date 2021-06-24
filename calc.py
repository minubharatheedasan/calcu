class calculator:
    
    def __init__(self):
        pass

    #def basiccalc(self,num1,num2):
     #   self.num1 = num1
      #  self.num2 = num2
            
    def add(self,num1,num2):
        print(f" \n Addition value = {num1+num2}") 
    
    def sub(self,num1,num2):
        print(f" \n Subtracted value = {num1-num2}")
        
    def mul(self,num1,num2):
        print(f" \n Multiplicated value = {num1*num2}")
    
    def div(self,num1,num2):
        print(f" \n Division value = {num1//num2}")
        
    def mod(self,num1,num2):
        print(f" \n Modulo (remainder) value = {num1%num2}")
        
    def sqr(self,num1):
        print(f" \n Square root value = {math.sqrt(num1)}")
        
    def squared(self,num1):
        print(f" \n {num1}^2 value = {num1*num1}")
            
class advcalc(calculator):
    
    def advcircle(self,num1):
        print(f"The area of circle is : {math.pi*num1*num1}")
    
    def advFactorial(self,num1):
        print(f"The factorial value of {num1} is : {math.factorial(num1)}")

    def advLog(self,num1):
        print(f"The Log value of {num1} is : {math.log10(num1)}")


    def adv_eraisepow(self,num1):
        print(f"e raised to the power x {num1} is : {math.exp(num1)}")
        
    def adv_xraisepowy(self,num1,num2):
        print(f"x raised to the power y {num1} is : {math.pow(num1,num2)}")
        
    def trigonometric(self,num1):
        print(f"Cos value {num1} is : {math.cos(num1)}")   
        print(f"Sin value {num1} is : {math.sin(num1)}")
        print(f"Tan value {num1} is : {math.tan(num1)}")
    
    def angular_conv(self,num1):
        print(f"Angular conversion value of {num1} is : {math.degrees(num1)} in degrees")   
        print(f"Angular conversion value of{num1} is : {math.radians(num1)} in radians")
        
    
        
if __name__=="__main__":
    import math
    c= calculator()
    ac = advcalc()
    option = 0
    while option != 9:
        option = int(input("Enter your option \n 1. Simple calculation \n 2. Advanced calculation\n Enter 9 to EXIT \n" ))
    
    
        if option == 1:
            ba_op = int(input("You can do following operations on basic calculator function: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulo \n 6. Square root \n 7. powered value \n 8. To go back to previous menu \n 9. To Exit\n"))

            if ba_op ==1:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number2 value: "))
                c.add(n1,n2)
            
            
            if ba_op ==2:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number2 value: "))
                c.sub(n1,n2)
        
            if ba_op ==3:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number2 value: "))
                c.mul(n1,n2)
            
            if ba_op ==4:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number2 value: "))
                c.div(n1,n2)
        
            if ba_op ==5:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number2 value: "))
                c.mod(n1,n2)
            
            if ba_op ==6:
                n1 = int(input("Enter number 1 value: "))
                c.sqr(n1)
            
            if ba_op ==7:
                n1 = int(input("Enter number 1 value: "))
                c.squared(n1)
            
            if ba_op == 8:
                option = int(input("Enter your option \n 1. Simple calculation \n 2. Advanced calculation\n" ))
            
            if ba_op ==9:
                print("Thank you for using Calculator. Have a good day")
            
        if option == 2:
            ba_op = int(input("You can do following operations on Advanced calculator function: \n 1. Area of circle \n 2. Factorial \n 3. Log value \n 4. e raised to the power x \n 5. x raised to the power y \n 6. Trigonometric functions \n 7. Angular conversion value \n 8. To go back to previous menu \n 9. To Exit\n"))
            if ba_op ==1:
                n1 = int(input("Enter number 1 value: "))
                ac.advcircle(n1)
            if ba_op ==2:
                n1 = int(input("Enter number 1 value: "))
                ac.advFactorial(n1)
            if ba_op ==3:
                n1 = int(input("Enter number 1 value: "))
                ac.advLog(n1)
            if ba_op ==4:
                n1 = int(input("Enter number 1 value: "))
                ac.adv_eraisepow(n1)
            if ba_op ==5:
                n1 = int(input("Enter number 1 value: "))
                n2 = int(input("Enter number 2 value: "))
                ac.adv_xraisepowy(n1,n2)    
            if ba_op ==6:
                n1 = int(input("Enter number 1 value: "))
                ac.trigonometric(n1) 
            if ba_op ==7:
                n1 = int(input("Enter number 1 value: "))
                ac.angular_conv(n1)
            if ba_op == 8:
                option = int(input("Enter your option \n 1. Simple calculation \n 2. Advanced calculation\n" ))
            if ba_op ==9:
                print("Thank you for using Calculator. Have a good day")
            
            
#        c.basiccalc(self,self)
 #   elif option == 2:  
  #      ac.advcalc()
  #for git
