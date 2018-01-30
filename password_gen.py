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
    if security == 1:
        index_a = randint(0, len(words) - 1)
        index_b = randint(0, len(words[index_a]) - 1)
        password += words[index_a][index_b]
    if security == 2:
        index = []
        for i in range

    print password

password_gen(1)