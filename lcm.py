a=int(input("enter the num1: "))
b=int(input("enter the num2: "))
if(a>b):
    big=a
else:
    big=b
step=big
while True:
    if big % a == 0 and big % b == 0:
        break
    else:
         big += step
print("lcm is :",big)
