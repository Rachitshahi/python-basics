#Access index of String
message = "Hello world"
print(message[6])

#print range of characters in string
print(message[0:5])

#Datatype methods
print(message.upper())
print(f"the total count is {message.count('l')}") #counts how many times the letter/word is on the string
print(f"the word is at {message.find('world')}'s index") #Finds keywords

new_message = message.replace('world','universe') #Replace keywords
print(new_message)

#check all methods u can use
name = 'Rachit'
print(dir(name))
print(help(str)) #check more detailed guide
print(help(str.upper)) #check detailed specific one