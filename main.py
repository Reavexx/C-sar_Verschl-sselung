output = input("Define Text: ")
number = input("Specify encryption: ")
password = input("Password: ")

if password == "M231":
    number = int(number)
    crypted = str(output)

    for i in output:
        crypted += chr(ord(i)+ number)
        print("crypted: "+ crypted)
else:
    print("Falsches Passwort Schade Marmelade")

#def range_char(start, stop):
#    return (chr(n) for n in range(ord(start), ord(stop) + 1))
#for character in range_char("a", "g"):
#    print(character)
