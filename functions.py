def some_functionXXX(amount, tax_rate):
    return tax_rate/100 * amount

x = some_functionXXX(150,5)
print(x)

def some_functionYYY(amount, tax_rate, *other_info):
    print(other_info)
    return (tax_rate/100) * amount

x = some_functionYYY(150, 5, "Jerry", "Bill", "Fred")
print(x)

#def zzzfuntion(city, **other_info):
#    print(city)
#    print(other_info.get("first_name"))
#    print(other_info.get("middle_initial"))
#    print(other_info.get("last_name"))

#zzzfuntion("New York", first_name = "Jerry", middle_initial = "T", last_name = "Newburg")