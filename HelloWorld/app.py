# Formatted string example
name = input("What's your name? ")
msg = f'Your name is {name}'
length = len(msg)
print(msg.upper())
print(msg, " [", length,"]")
print("Msg contains word Mark at index: ",msg.find('Mark'))
print("Msg contains word Mark? ",'Mark' in msg)
print("I replaced your name in the msg: ", msg.replace(name, 'Frank'))
print("Capitalized message: ",msg.title())

#operators precedence
print(2*5/2)

#Some math function
print(round(2.9))
print(round(2.5))
print(abs(-2.98))