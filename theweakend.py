#!/usr/bin/env python3
import sys
from itertools import permutations

results = []
salt_list = ["1", "69","123", "420", "12345", "69420", "123456", "1337", "xinh", "cute","dangiu", "deptrai", "deptraivcl", "vip", "pro", "vippro", "!", "@", "$"]

# worker
def generator_for_fullname(perm,dob, results):
    for i in perm:
        for j in salt_list:
            pw1 = ''.join(i).lower()
            pw2 = pw1 + str(dob[0])
            pw3 = pw2 + str(dob[1])
            pw4 = pw1 + str(dob[2])
            pw5 = pw1 + str(dob[2][-2]) + str(dob[2][-1])
            pw6 = pw1 + j 
            pw7 = pw6 + str(dob[0])
            pw8 = pw7 + str(dob[1])
            pw9 = pw8 + str(dob[2])
            pw10 = pw8 + str(dob[2][-2]) + str(dob[2][-1])
            pw11 = pw3 + str(dob[2])
            results.append(pw1)
            results.append(pw2)
            results.append(pw3)
            results.append(pw4)
            results.append(pw5)
            results.append(pw6)
            results.append(pw7)
            results.append(pw8)
            results.append(pw9)
            results.append(pw10)
            results.append(pw11)

def generator_for_nickname(nickname, dob, results):
    for i in salt_list:
        pw1 = nickname + str(i)
        pw2 = pw1 + str(dob[0])
        pw3 = pw2 + str(dob[1])
        pw4 = pw3 + str(dob[2][-2]) + str(dob[2][-1])
        results.append(pw1)
        results.append(pw2)
        results.append(pw3)
        results.append(pw4)
    pw5 = nickname + str(dob[0])
    pw6 = pw5 + str(dob[1])
    pw7 = nickname + str(dob[2])
    pw8 = pw6 + str(dob[2][-2]) + str(dob[2][-1])
    pw9 = nickname + str(dob[2][-2]) + str(dob[2][-1])

    results.append(pw5)
    results.append(pw6)
    results.append(pw7)
    results.append(pw8)
    results.append(pw9)
# password generator function that based on the fullname and dob provided
def name_and_dob_based_gen():
    stack1 = sys.argv[1].split(" ")
    stack2 = [stack1[-2], stack1[-1]]
    stack3 = [stack1[0], stack1[-1]]
    stack4 = [stack1[0][0], stack1[-2][0], stack1[-1]]
    dob = sys.argv[3].split("-")
    perm1 = list(permutations(stack1))
    perm2 = list(permutations(stack2))
    perm3 = list(permutations(stack3))
    perm4 = list(permutations(stack4))
    generator_for_fullname(perm1, dob, results)
    generator_for_fullname(perm2, dob, results)
    generator_for_fullname(perm3, dob, results)
    generator_for_fullname(perm4, dob, results)
  

# password generator function that based on the nickname and dob provided
def nickname_and_dob_based_gen():
    nickname = sys.argv[2]
    dob = sys.argv[3].split("-")
    generator_for_nickname(nickname,dob, results)

# password generator function that based on the fullname and the nickname provided
def name_and_nickname_based_gen():
    pass

def main():
    # Banner ngầu vl
    banner = r"""_________          _______             _______  _______  _          _______  _        ______  
\__   __/|\     /|(  ____ \  |\     /|(  ____ \(  ___  )| \    /\  (  ____ \( (    /|(  __  \ 
   ) (   | )   ( || (    \/  | )   ( || (    \/| (   ) ||  \  / /  | (    \/|  \  ( || (  \  )
   | |   | (___) || (__      | | _ | || (__    | (___) ||  (_/ /   | (__    |   \ | || |   ) |
   | |   |  ___  ||  __)     | |( )| ||  __)   |  ___  ||   _ (    |  __)   | (\ \) || |   | |
   | |   | (   ) || (        | || || || (      | (   ) ||  ( \ \   | (      | | \   || |   ) |
   | |   | )   ( || (____/\  | () () || (____/\| )   ( ||  /  \ \  | (____/\| )  \  || (__/  )
   )_(   |/     \|(_______/  (_______)(_______/|/     \||_/    \/  (_______/|/    )_)(______/ 
"""

    #print usage if improper # of args
    if len(sys.argv) == 1 or len(sys.argv) != 4:
        print(banner)
        print('[+] Cách sử dụng: ./theweakend.py <full name> <nickname> <dob(date-month-year)>')
        print('[+] Ví dụ: ./theweakend.py "Le Van A" "ale123" "1-1-2000"')
        print('[+] Nếu không có nickname hay tên gọi khác, bạn có thể điền vào kí tự khoảng trắng điền như này " "')
        quit()

    #quit if fullname is only a single word
    if len(sys.argv[1].split(" ")) == 1:
        print("[-] Họ tên gì chỉ một từ thế bro ?")
        quit()
    if sys.argv[2] == " ":
        print("[+] Đợi chút nha bro :D", end="\r")
        file_name = "passwords.txt"
        name_and_nickname_based_gen()
        with open(file_name, 'w') as file:
            for pw in list(set(results)):
                file.write(pw + "\n")
        print("[+] Done, enjoy <3 ")
        quit()

    file_name = "passwords.txt"
    print("[+] Đợi chút nha bro :D")
    name_and_dob_based_gen()
    nickname_and_dob_based_gen()
    with open(file_name, 'w') as file:
        for pw in list(set(results)):
            file.write(pw + "\n")
    print("[+] Done, enjoy <3 ")
    quit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass