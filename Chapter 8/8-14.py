def car_info(manufacturer,model,**info):

    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for k,v in info.items():
        car[k] = v
    return car
make_car =car_info("Japan","Honda",color="blue",tow_package=True)

print(make_car)