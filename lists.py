fruit_list = ['apple', 'orange', 'peach', 'pear', 'plum']
print(fruit_list)
print(fruit_list[1])
fruit_list.append('strawberry')
print(fruit_list)
veg_list = ['tomato', 'cucumber']
fruit_veg_list = fruit_list + veg_list
print(fruit_veg_list)

books = {}
books['The Hunger Games'] = 'Susan Collins'
books['Harry Potter'] = 'J K Rowling'
books['Lord of the Rings'] = 'Tolkien'
books2 = {
'The Hunger Games' : 'Susan Collins',
'Harry Potter' : 'J K Rowling',
'Lord of the Rings' : 'Tolkien'
}

for book, author in books.items():
    print("Author of %s is %s" % (book, author))

for book, author in books2.items():
    print("Author or %s is %s" % (book, author))

a = set("my name is Susan and Susan is my name".split())
print(a)
b = set("my month is june and june is my month".split())
print(b)
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.union(b))

for book, author in books.items():
    if book == "Harry Potter" and author == "J K Rowling":
        print("Author of %s is %s" % (book, author))
		
if "appled" in fruit_list:
    print("yes")
else:
    print("no")	

cars = ['honda', 'toyota', 'bmw']
for car in cars:
    print(car)
for x in range(5):
    print(x)

x = 1
while x < 5:
    x += 1
    print(x)

for fruit in fruit_list:
    print(fruit)
    if fruit == 'pear':
	    break

def some_function():
    print("print in the function")

some_function()	    

def some_function2(username):
    print("Welcome, %s" % username)

some_function2('Jerry')

def times_function(num_1, num_2):
    return num_1 * num_2

result = times_function(5, 6)
print(result)

def some_function3(user, first_name, *other_info):
    print(user)
    print(first_name)
    print(other_info)

some_function3("steph", "stephanie", "rabbani", "june")

def some_function4(user, first_name, **other_info):
    print(other_info.get("last_name"))
    print(other_info.get("zip"))

some_function4("steph", "stephanie", zip = "90210", last_name =
"rabbani")    