x = 0b1010
print(x) 
x = 0o12
print(x) 
x = 0xA
print(x) 
x = 0xF
print(x) 
x = 0o45
print(x) 
x = 0x34  
print(x) 
x = "A"
print(ord(x)) 
x = "a" 
print(ord(x)) 
print("Hello \t python") 
print("Hello\npthon ") 
print("Hello\rpython") 
print("Hello\bs") 
print("Hello\b ") 
print("\'Hello\'")  
print("a\\b") 
x = 3.4e+2
print(x) 
x = 2 + 3j 
print(x) 
print(x.real,x.imag) 
L = [1, 2 ,3 ,4 ] 
print(L) 
x = {'age': 12 , 'name' : 'harsh'} 
print(x.keys()) 
print(x.values())  
print(x.items()) 
name = {"juhi" , "purvi" , "purvi" , "anil" } 
print(name)  
x = (2 , 3, 4 )
print(x) 
x = (3,) 
print(x) 
x = 10*3+5-3/4+5
print(x) 
x = (10*3+5-3/4+5) 
print(x) 
x = """this is a test""" 
print(x) 
print("one") ; print("two") ; print("three") 
print("This is a long\nexample which is\nspannning multiple\nlines") 
print("01" , "01" , "2026") 
print("01" , "01" , "2026" , sep = " - ") 
print("Hello") 
print("world")  
print("Hello" , end = " " )
print("world") 
f = open("my-notes.txt" , "w") 
print("python is awesone " , file = f) 
f.close() 
print(10 , 12 , 13 , sep = " ; ") 
print(10,12,13 , sep = "\n") 
name = 'pari' 
age = 23
print("Hello" , name) 
print("you are" , age , "yours old ")
name = "vikas" 
age = 24
text = "mera naam {} hai aur main {} saal ka hu ." 
print(text. format(name,age))
name = "vikas"
age = 25
text = "Meri umar {1} saal hai aur naam {0} hai ." 
print(text.format(name,age)) 
name = "vikas"
age = 25
score = 85.5  
print("Hello %s aapki age %d hai aur score %f hai " %(name, age , score)) 
print("Hello {name} you are {age} years old ." .format(name ="pari" , age = 21))
name = "pari" 
age = 23 
print("Hello" + name + "you are " + str(age)  +  " years old") 
name = input("Enter your name") 
print("Hello" , name) 
x = int(input("Enter integer"))  
y = 10
z = y + x
print(z)   
x = int(23.45) 
print(x) 
x = int(True)
print(x) 
x = int(False) 
print(x) 
x = int('123' , 8)
print(x)  
x = int('0b1010' , 2)
print(x) 
x = int('0x123' , 16)
print(x) 
x = float('23.34') 
print(x) 
name, age = input('Enter your name and age\n',).split() 
print("hello" , name) 
print("After 10 years your age will be : " , int(age) + 10 ) 
num = int(input("Enter an integer: ")) 
print('original number : ' , num )
print('octal equivalent :' , oct(num))
print('Hex equivalent : ', hex(num)) 
print('binary equivalent: ', bin(num)) 
a , b = input('Enter two numbers : ') . split() 
a = int(a)
b = int(b) 
print('before swapping')
print('a = ' , a , '\tb = ' , b)
a,b = b , a
print('after swapping')
print(' a = ' , a , '\tb = ' , b)
