def is_palindrome(text):
    # 1. Spaces hataye aur lowercase kiya
    clean_text = text.strip().lower()
    
    # 2. Ulta banaya
    reversed_text = clean_text[::-1]
    
    # 3. Check kiya ki kya seedha aur ulta barabar hain
    if clean_text == reversed_text:
        return True
    else:
        return False

# Test karein:
print(is_palindrome("RADAR"))   # True
print(is_palindrome("Madam"))   # True
print(is_palindrome("Python"))  # False 

def mask_email(email):
    # Step 1: '@' se do hisse alag kiye
    parts = email.split("@")
    username = parts[0]   # Jaise: 'vikas123'
    domain = parts[1]     # Jaise: 'gmail.com'
    
    # Step 2: Username ke shuru ke 2 letters nikale
    masked_user = username[:2] + "****"
    
    # Step 3: Wapas jod diya
    final_email = f"{masked_user}@{domain}"
    return final_email

# Test karke dekhein:
print(mask_email("vikas123@gmail.com"))
print(mask_email("rahul_sharma@yahoo.com"))

def count_words(sentence):
    clean_sentence = sentence.strip()
    words_list = clean_sentence.split()
    totalwords = len(words_list) 
    return totalwords
print(count_words("python strings are very easy to learn   "))


    
    
    
    
    
    
    
    



 