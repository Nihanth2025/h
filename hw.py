decimal = int(input("Enter the number: "))
def fun1(n):
    
    if n > 1:
        
     fun1(n // 2)
   
    print(n % 2, end='')


print("Binary representation of the number is:")
fun1(decimal)
