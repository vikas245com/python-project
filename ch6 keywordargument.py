def generate_profile_card(name, role, city):
    template = "User: {user_name} | Role: {user_role} | Location: {user_city}"
    return template.format(user_name=name, user_role=role, user_city=city)

print(generate_profile_card("Vikas", "Developer", "Jaipur"))