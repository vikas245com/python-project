def truncate_text(text,max_length):
    if len(text) > max_length:
        return text [:max_length] + "..."
    else:
        return text 
print(truncate_text("learn python programing from scratch" , 15))
print(truncate_text("Hello world" , 20)) 
        
