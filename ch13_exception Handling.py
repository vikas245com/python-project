# Bina Exception Handling ke (Program yahan crash ho jayega):
# print(10 / 0) 
# Output: ZeroDivisionError: division by zero (Program aage nahi chalega!)

# Exception Handling ke sath:
try:
    # Yeh risky code hai, yahan error aa sakti hai
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    # Agar error aayi, toh program crash nahi hoga, yeh chalega!
    print("Arre bhai! Aap kisi number ko 0 se divide nahi kar sakte.")

print("Program aage chal raha hai, crash nahi hua!")
try:
    # Yahan humne 0 se divide kiya (ZeroDivisionError aayegi)
    ans = 10 / 0
    
# Yahan humne choti error ki jagah uske Parent (ArithmeticError) ko bula liya
except ArithmeticError:
    print("Ganit (Maths) se judi koi error aayi hai bhai!")

except Exception:
    print("Koi aam error aayi hai.")

try:
    # User se input lena aur divide karna
    num1 = int(input("Pehla number daalo: "))
    num2 = int(input("Doosra number daalo: "))
    result = num1 / num2
    print("Jawab hai:", result)

except ZeroDivisionError:
    print("Arre bhai! Kisi number ko 0 se divide nahi kar sakte.")

except ValueError:
    print("Kripya sirf valid numbers (integers) hi daalein, text nahi!")

try:
    # Code yahan hai...
    pass

except (ZeroDivisionError, ValueError, TypeError):
    print("Kuch toh gadbad hai! Ya toh 0 se divide kiya ya galat value daali.")

try:
    num = 10 / 0  # Yahan ZeroDivisionError aayegi
    print(x)      # Yahan NameError aayegi
    
except:
    # Yeh khaali except hai — bina kisi error name ke!
    print("Bhai, kuch toh gadbad huyi hai, par pata nahi kya!")

try:
    # Risky code
    x = 10 / 0
except Exception as e:
    # Yeh saari standard errors ko pakad lega aur unka asli naam bhi bata dega!
    print("Error aayi hai:", e)

try:
    # Yahan hum 0 se divide kar rahe hain (ZeroDivisionError aayegi)
    num = int(input("Ek number daalo: "))
    result = 10 / num
    print("Jawab:", result)

except Exception as e:
    # Yeh wali line saari aam errors ko pakad legi aur unka asli reason bata degi!
    print("Ek error aa gayi hai bhai:", type(e).__name__)
    print("Error ka detail message:", e)

def check_voting_age(age):
    if age < 0:
        # Yahan humne jaan-boojh kar error raise kar di!
        raise ValueError("Umar kabhi bhi minus (negative) mein nahi ho sakti, bhai!")
    
    if age < 18:
        print("Aap vote nahi de sakte, abhi chote hain.")
    else:
        print("Aap bilkul tayar hain, vote de sakte hain!")

# 1. Sahi age ke sath call karna:
check_voting_age(20) # Output: Aap bilkul tayar hain, vote de sakte hain!

# 2. Galat age (-5) ke sath call karna:
try:
    check_voting_age(-5)
except ValueError as e:
    print("Pakdi gayi error:", e)


try:
    print("--- Outer Try Block Shuru ---")
    
    # 1. Pehla kaam: File open karne ki koshish ya normal calculation
    num1 = int(input("Pehla number daalo: "))
    
    try:
        print("--- Inner Try Block Shuru ---")
        # 2. Doosra kaam: Inner block mein division karna
        num2 = int(input("Doosra number daalo: "))
        result = 100 / num2
        print("Division ka jawab:", result)
        
    except ZeroDivisionError:
        # Yeh sirf inner block ki 0 wali error ko pakdega
        print("Inner Error: Arre bhai! 0 se divide nahi ho sakta.")

except ValueError:
    # Yeh outer block ki galat input wali error ko pakdega
    print("Outer Error: Kripya sirf valid number hi enter karein!")

print("Program safely aage chal raha hai.")

# 1. Apni khud ki Custom Exception Class banana
class InsufficientBalanceError(Exception):
    """Jab balance kam ho aur paise nikalne ki koshish ki jaye"""
    pass

# 2. Bank Account ka class jisme yeh exception use hogi
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Yahan humne apni custom exception ko raise kar diya!
            raise InsufficientBalanceError(f"Galti! Aapke paas sirf {self.balance} rupaye hain, aap {amount} nahi nikal sakte.")
        
        self.balance -= amount
        print(f"Paise nikal gaye. Naya balance: {self.balance}")

# --- Code ko run karke dekhte hain ---
my_account = BankAccount(5000)

try:
    # 6000 nikalne ki koshish kar rahe hain jabki balance 5000 hai
    my_account.withdraw(6000)

except InsufficientBalanceError as e:
    # Yeh hamari custom exception ko pakad lega!
    print("Custom Error Pakdi Gayi:", e)

    

