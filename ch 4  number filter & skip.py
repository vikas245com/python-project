for num in range(1 , 31):
    if num == 26:
        print("reached 26! loop stopped;")
        break
    if num % 5 == 0 :
        continue
    if num % 2 == 0:
        print(f"{num} is even") 
    else:
        print(f"{num} is odd") 