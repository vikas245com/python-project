def sort_two_word(word1 , word2):
    if word1.lower() < word2.lower():
        return f"pehle aayega: {word1}  , baad mein:{word2}"
    else:
        return f"pehle aayega : {word2} , baad mein: {word1}"
result = sort_two_word("banana" , "apple")
print(result) 
