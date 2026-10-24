def replace_char_at(text , index, new_char):
    new_name = text[:index] + "z" + text[index + 1:]
    return new_name
result1 = replace_char_at("python" , 2 , "Z")
print(result1)
result2 = replace_char_at("python" , 0 , "M")
print(result2) 
 
