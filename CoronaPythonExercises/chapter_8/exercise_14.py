def make_car(manuf_name, model_name, **user_info):
    user_info['manufacture'] = manuf_name
    user_info['model'] = model_name
    return user_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)