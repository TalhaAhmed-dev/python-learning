def build_profile(first, second,**user_info):
    profile = {}
    profile["first"] = first.title()
    profile["second"] = second.title()
    for k,v in user_info.items():
        profile[k] = v
    return profile

user_profile = build_profile("talha","ahmed",location="Islamabad",hobby= "wife beating")
print(user_profile)