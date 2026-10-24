s = "python"
x = 1 
print(s[0])  
print(s[x]) 
print(s[x-2]) 
x = 2 
print(s[x*2 + 1]) 

t = "programing" 
print(t[0:7])
print(t[2 : 7])
print(t[3 : 7])
print(t[1 : 4]) 
print(t[  : 7 ])
print(t[ :  7  ])
print(t[ 2 : ])
print(t[:])
print(t[: : 2])
print(t [ : : -1])
print(t[-1])
print(t[: -1])
print(t[-6 : - 1])
print(t[6 : 0 : - 1])
print(t[: - 2 ]) 
msg = "Hello" 
new_msg = "M" + msg[1 : ]
print(new_msg) 

text = "  python programming language  "

# 1. Case Badalna
print(text.upper())       # Sab CAPITAL
print(text.lower())       # Sab small
print(text.title())       # Har word ka pehla letter capital

# 2. Extra Spaces Hatana (Clean karna)
clean_text = text.strip()
print(f"'{clean_text}'")  # Aage-peeche ke spaces gayab

# 3. Dhoondna aur Badalna (Search & Replace)
print(clean_text.replace("language", "core"))  # Badal dega
print(clean_text.find("prog"))                # Index batayega (kahan se shuru hai)
print(clean_text.count("m"))                  # Kitni baar aaya

# 4. Check Karne Wale Methods (True / False return karte hain)
print(clean_text.startswith("python"))  # True
print(clean_text.endswith("language"))  # True
print("12345".isdigit())                # True (kya sab digits hain?)
print("Python".isalpha())               # True (kya sab alphabets hain?)

# String se List banana (Tukde karna)
sentence = "Math,Science,English,Hindi"
subjects = sentence.split(",")
print(subjects)  # Output: ['Math', 'Science', 'English', 'Hindi']

# List se wapas String banana (Jodna)
words = ["Python", "is", "awesome"]
joined_sentence = " ".join(words)
print(joined_sentence)  # Output: Python is awesome

first_name = "Vikas"
last_name = "Pareek"

# 1. Concatenation (+)
full_name = first_name + " " + last_name
print(full_name)  # Output: Vikas Pareek

# 2. Repetition (*)
border = "-" * 15
print(border)     # Output: ---------------

# 3. in operator
msg = "Welcome to Python"
print("Python" in msg)  # Output: True
print("Java" in msg)    # Output: False

# 4. not in operator
print("admin" not in msg)  # Output: True

def format_banner(title, is_urgent):
    if is_urgent == True:
        s3 = "ALERT : " + title
        print("*" * 20)
        print(title)
        print("*" * 20)
        if "free" in title.lower():
            return True
        else:
            return False

result = format_banner("claim free pass" , True)
print("contains 'free' ?: " , result) 

name = "python"
print("---Direct traversal ---")
for letter in name:
    print(letter) 

print("\n --- Index ke sath traversal ---")
for i in range(len(name)):
    print(f"index {i} par letter hai: {name[i]} ")

 # 1. Equality check
print("apple" == "apple")  # True
print("apple" == "Apple")  # False (Case-sensitive)

# 2. Dictionary order check
print("bat" > "ball")      # True (Kyunki 3rd letter 't' ka code 'l' se bada hai)

# 3. Capital vs Small
print("A" < "a")           # True (65 < 97)

# 4. ASCII value check karne ke built-in functions
print(ord("A"))            # Output: 65
print(ord("a"))            # Output: 97
print(chr(65))             # Output: 'A'        


