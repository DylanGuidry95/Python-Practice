from random import *

def password_gen(security):
    f = open("passwords.txt")
    words = []    
    current_list = []
    for word in f:
        if word.__contains__(">"):
            if len(current_list) > 0: 
                words.append(current_list)
            current_list = []
            continue
        w = word.replace("\n", "")
        current_list.append(w)
    if len(current_list) > 0:
        words.append(current_list)

    password = ""
    for i in range(security):
        index_a = randint(0, len(words) - 1)
        index_b = randint(0, len(words[index_a]) - 1)
        password += words[index_a][index_b]

    conversions = open("conversions.txt")    
    for letter in conversions:
        letter = letter.replace("\n", "")
        id = letter.split('-')
        if password.__contains__(id[0]):            
            password = password.replace(str(id[0]), str(id[1]))
            
    contains_number = False
    for number in range(10):
        if password.__contains__(str(number)):
            contains_number = True

    if contains_number == False:
        password += str(randint(0, 9999))

    contains_cap_letter = False
    while contains_cap_letter == False:
        index = randint(0, len(password) - 1)
        if ord(password[index]) >= 97 and ord(password[index]) <= 122:
            password = password.replace(password[index], chr(ord(password[index]) - 32))
            contains_cap_letter = True

    passwords = open("pass.txt", 'a')
    passwords.writelines(password)
    passwords.write("\n")
    passwords.close()

    return password


password_gen(randint(0,4))