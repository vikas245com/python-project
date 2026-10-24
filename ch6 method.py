def clean_and_verfy_id(user_id):
    user_name = user_id.strip().lower()
    if user_name .startswith("admin"):
        return "access granted : admin "
    else:
        return "access denied"
print(clean_and_verfy_id("  ADMIN99  ")) 
print(clean_and_verfy_id ("user_484")) 

