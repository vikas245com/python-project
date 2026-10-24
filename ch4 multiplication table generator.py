n = int(input("Enter any +ve number \n "))
t = 1
while t <= 10: 
    value = n*t 
    print(n, "x" , t , "=" , value )
    t += 1

n = int(input("Enter any +ve number : "))

# 1 se lekar 10 tak chalega (11 par rukega)
for t in range(1, 11):
    print(f"{n} x {t} = {n * t}")