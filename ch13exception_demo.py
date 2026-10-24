# Safe Division Calculator using Exception Handling

def safe_divide():
    print("--- Safe Division Calculator ---")
    
    try:
        # User se input lena (Yahan ValueError aa sakti hai agar text daal diya)
        num1 = float(input("Pehla number daliye: "))
        num2 = float(input("Doosra number daliye: "))
        
        # Division karna (Yahan ZeroDivisionError aa sakti hai agar num2 = 0 hua)
        result = num1 / num2
        print(f"Division ka result hai: {result}")
        
    except ZeroDivisionError:
        print("❌ Error: Kisi bhi number ko 0 se divide nahi kiya ja sakta!")
        
    except ValueError:
        print("❌ Error: Kripya sirf valid numbers hi enter karein, letters nahi!")
        
    else:
        print("✅ Badhiya! Calculation bina kisi error ke poori ho gayi.")
        
    finally:
        print("🔒 Ye block hamesha chalega (Cleanup / Final step).\n")

# Program ko run karna
if __name__ == "__main__":
    safe_divide()


