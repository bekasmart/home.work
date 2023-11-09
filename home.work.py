# > Beka: 
# LEVEL 1 
# task 1 
word = list () 
empty_list = list () 
# print(len(empty_list)) 
print(empty_list) 
 
 
# task 2 
siti = ['Kanada','Switzerland','Monaco','Singapore','Luxembourg'] 
print(siti) 
 
 
# task 3 
siti = ['Kanada','Switzerland','Monaco','Singapore','Luxembourg'] 
print(len(siti)) 
 
 
# task 4 
siti = ['Kanada','Switzerland','Monaco','Singapore','Luxembourg'] 
first_country = siti [0] 
print (first_country) 
third_country = siti [2] 
print (third_country) 
fifth_country = siti [4] 
print (fifth_country) 
 
 
# task 5 
mixed_data_types = {'name':'Malika','age':'17','height':'162','marital status':'single','address':'Turkebaeva 59'} 
print(mixed_data_types) 
 
 
# task 6 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
print(it_companies) 
 
 
# task 7 
fruits = ['banana', 'orange', 'mango', 'lemon'] 
print(fruits) 
 
 
# task 8 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
print(len(it_companies)) 
 
 
# task 9 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
first_company = it_companies [0] 
print(first_company) 
forth_company = it_companies [3] 
print(forth_company) 
seventh_company = it_companies [6] 
print(seventh_company) 
 
 
# task 10 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies [-1] = 'Alphabet'  
print(it_companies) 
 
 
# task 11 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies [0] = 'Alphabet' 
print (it_companies) 
 
 
# task 12 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies [4] = 'Alphabet' 
print (it_companies) 
  
  
# task 13? 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
print(it_companies.upper()) 
 
 
#task 14 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
 
 
# task 15 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
does_exist = 'Facebook' in it_companies  
print(does_exist) 
 
 
# task 16 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.sort() 
print(it_companies) 
 
 
# task 17 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.reverse() 
print(it_companies) 
 
 
# task 18 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
first_company = it_companies[3:] 
print(first_company) 
 
 
# task 19 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
first_company = it_companies[:-3] 
print(first_company) 
 
 
# task 20 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.remove('Apple') 
print(it_companies) 
 
 
# task 21 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.remove('Facebook') 
print(it_companies) 
 
 
# task 22 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.remove('Apple') 
print(it_companies) 
 
 
# task 23 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.remove('Amazon') 
print(it_companies) 
 
 
# task 24? 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
it_companies.remove('it_companies') 
print(it_companies) 
 
lst = ['item1', 'item2'] 
lst.pop() 
 
 
# task 25 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'] 
 
 
 
# task 26 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 
integers = front_end + back_end 
print(integers) 
 
 
# task 27? 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 
integers = front_end + back_end



# 1-t
thirty = "Thirty"
days = "Days"
of = 'Of'
python = 'Python'
print("{} {} {} {}".format(thirty,days,of,python))

thirty = "Thirty"
days = "Days"
of = 'Of'
python = 'Python'
print(f"{thirty} {days} {of} {python}")

# 2-t
thirty = "Coding"
days = "For"
of = 'All'
print("{} {} {}".format(thirty,days, of))

thirty = "Coding"
days = "For"
of = 'All'
print(f"{thirty} {days} {of}")

# 3-4-5t
company = "Coding For All"
print(len(company))

# 6-t
company = "Coding For All"
up = company.upper()
print(up)

# 7-t
company = "CODING FOR ALL"
up = company.lower()
print(up)

# 8-t
company = "Coding For All"
up = company.swapcase()
print(up)

company = "Coding For All"
up = company.title()
print(up)

company = "Coding For All"
up = company.capitalize()
print(up)

# 9-t
company = "Coding For All"
up = company.strip("Coding ")
print(up)

# 10-t
company = "Coding For All"
p = 'Coding'
up = company.index(p)
print(up)

# 11-t
company = "Coding For All"
up = company.replace("Coding For All","coding ")
print(up)

# 12-t
company = "Python for Everyone"
up = company.replace("Python for Everyone","Python for All")
print(up)

company = "Python for Everyone"
up = company.split()
print(up)

company =  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
up = company.split()
print(up)

company = "Coding For All"
print(f"character at index 0 in the string Coding For All: {company[0]}")

company = "Coding For All"
print(company.endswith('All'))

company = "Coding For All"
print(f"character is at index 10 in Coding For All string: {company[10]}")

company = "Coding For All"
print(company[0+7+11])
print(company[7])
print(company[11])

company = "Coding For All"
inde = "C"
print(f"Позиция символа C в строке: {company.index(inde)}")

company = "Coding For All"
inde = "F"
print(f"Позиция символа F в строке: {company.index(inde)}")

company = "Coding For All"
inde = input("text: ")
print(f"Позиция символа в строке: {company.index(inde)}")

company = "Coding For All"
inde = "i"
print(f"Позиция символа i в строке: {company.index(inde)}")

text = "You cannot end a sentence with because because because is a conjunction"
print(f"первого вхождения слова because начинается с позиции: {text.find('because')}")

text = "You cannot end a sentence with because because because is a conjunction"
print(f"первого вхождения слова because начинается с позиции: {text.index('because')}")

text = "You cannot end a sentence with because because because is a conjunction"
print(f"последнего вхождения слова because начинается с позиции: {text.rindex('because')}")

text = "You cannot end a sentence with because because because is a conjunction"
print(text[31:54])

company = "Coding For All"
inde = company.split()
print(f"Строка начинается с подстроки {inde[0]}")

company = "Coding For All"
inde = company.split()
print(f"Строка заканчивается с подстроки {inde[-1]}")

company = "Coding For All"
print(company[7:10])

text = "30DaysOfPython"
print(text.isidentifier())
p = "thirty_days_of_python"
print(p.isidentifier())

lis = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(lis)
print(result)

text = "I am enjoying this challenge.\nI just wonder what is next."
print(text)

text = "Name \tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki"
print(text)

radius = 10
area = 3.14 * radius ** 2
result = "The area of a circle with radius {} is {} meters square.".format(radius,area)
print(result)

radius = 10
area = 3.14 * radius ** 2
result = f"The area of a circle with radius {radius} is {area} meters square."
print(result)

num = 8
number = 6
print("{} + {} = {}".format(num, number, num + number))
print("{} - {} = {}".format(num, number, num - number))
print("{} * {} = {}".format)







parents = family_members[:2]
siblings = family_members[2:]

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'lettuce', 'broccoli')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle_item = food_stuff_tp[len(food_stuff_tp)//2]
middle_items = food_stuff_lt[len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1]

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries
