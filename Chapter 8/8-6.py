def city_country(city, country):
    """Describe a country"""
    describe_city = city + "," + country
    return describe_city.title()
while True:
    city_n = input("Enter a city: ")
    if city_n == "q":
        print("Thank you for your time!")
        break
    country_n = input("Enter a country: ")
    if city_n == "q":
        print("Thank you for your time!")
        break

    formatted_name = city_country(city_n, country_n)
    print(f"\n{formatted_name}\n Enter 'q' to quit.")


