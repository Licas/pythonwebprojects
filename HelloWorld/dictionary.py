customer = {
    'name':'John',
    'email':'john@email.com',
    'phone':'333123915',
    'age':32,
    'isMale':True
}

print(customer)
customer["name"]="Mark"
print(f"Customer name is {customer.get('name')}")
for entry in customer:
    print(entry,customer[entry])


for index,key in enumerate(customer):
    print(key)