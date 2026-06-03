
current_users = ["rinku", "pinku", "tiNku", "kinku", "dinku"]
new_users = ["bunty", "Tinku", "slanty", "fanty", "dinku"]
current_users_lower = []
for u in current_users:
    current_users_lower.append(u.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"this user name {user} is not available")
    else:
        print(f"this user name {user} is available")