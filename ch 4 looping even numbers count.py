for i in range (1 , 11):
    if i % 2 == 0: 
        print(i) 

for i in range(2 , 11 , 2):
    print(i)

for i in range(1, 11 , 2):
    print(i)  

for i in range(5, 0 , -1):
    print(i) 
print("blast off!") 



total = 0
for i in range(1,6):
    total += i 
print(f"kul jama rashi : {total}") 


total_kharcha = 0 
for day in range(1 , 4):
    kharcha = int(input(f"day {day} ka kharcha:"))
    total_kharcha += kharcha 
print(f"kul kharcha : {total_kharcha}") 

pass_count = 0
for i in range(1 , 5):
    marks = int(input(f"subject {i} marks: ")) 
    if marks >= 33:
        pass_count += 1 
print(f"kul pass huye subjects : {pass_count}") 

for coupen in range(1 , 6):
    coupen = int(input(f"coupen {coupen} number ; "))
    if coupen == 7 :
        print("winner mil gaya ! lucky coupen 7 hai ! ")
        break 
    else:
        print("try next time") 

for i in range(1, 7):
    if i == 3:
        continue
    print(i)  

i = 1
while i <= 5:
    print(i)
    i += 1 


guess = 0
while guess != 5:
    guess = int(input("guess the number (1 to 10):  "))
    print("galat! dobara try karo.  ")
print("arey wah! sahi number pehchan liya ! ") 