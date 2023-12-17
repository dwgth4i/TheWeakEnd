#!/usr/bin/env python3
import sys
from itertools import permutations
import argparse


results = []
salt_list = ["1", "69","123", "420", "12345", "69420", "123456", "1337", "xinh", "cute","dangiu", "deptrai", "deptraivcl", "vip", "pro", "vippro", "!", "@", "$"]


# worker
def generator_for_fullname(perm, dob, results):
    for i in perm:
        for j in salt_list:
            pw1 = ''.join(i).lower()
            pw2 = pw1 + str(dob[0])
            pw3 = pw2 + str(dob[1])
            pw4 = pw1 + str(dob[2])
            pw5 = pw3 + str(dob[2][-2]) + str(dob[2][-1])
            pw6 = pw1 + j 
            pw7 = pw6 + str(dob[0])
            pw8 = pw7 + str(dob[1])
            pw9 = pw8 + str(dob[2])
            pw10 = pw8 + str(dob[2][-2]) + str(dob[2][-1])
            pw11 = pw3 + str(dob[2])
            results.extend([pw1,pw2,pw3,pw4,pw5,pw6,pw7,pw8,pw9,pw10,pw11])

def generator_for_nickname(nickname, dob, results):
    for i in salt_list:
        pw1 = nickname + str(i)
        pw2 = pw1 + str(dob[0])
        pw3 = pw2 + str(dob[1])
        pw4 = pw3 + str(dob[2][-2]) + str(dob[2][-1])
        results.extend([pw1,pw2,pw3,pw4])
    pw5 = nickname + str(dob[0])
    pw6 = pw5 + str(dob[1])
    pw7 = nickname + str(dob[2])
    pw8 = pw6 + str(dob[2][-2]) + str(dob[2][-1])
    pw9 = nickname + str(dob[2][-2]) + str(dob[2][-1])
    results.extend([pw5,pw6,pw7,pw8,pw9])
    
# password generator function that based on the fullname and dob provided
def name_and_dob_based_gen(fullname, dob):
    stack1 = fullname.split(" ")
    stack2 = [stack1[-2], stack1[-1]]
    stack3 = [stack1[0], stack1[-1]]
    stack4 = [stack1[0][0], stack1[-2][0], stack1[-1]]
    dob = dob.split("-")
    perm1 = list(permutations(stack1))
    perm2 = list(permutations(stack2))
    perm3 = list(permutations(stack3))
    perm4 = list(permutations(stack4))
    generator_for_fullname(perm1, dob, results)
    generator_for_fullname(perm2, dob, results)
    generator_for_fullname(perm3, dob, results)
    generator_for_fullname(perm4, dob, results)
  
# password generator function that based on the nickname and dob provided
def nickname_and_dob_based_gen(nickname, dob):
    dob = dob.split("-")
    generator_for_nickname(nickname,dob, results)

def main():

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

    if len(sys.argv) == 1 or len(sys.argv) < 5:
        print(banner)
        print('[+] Usage: python3 theweakend.py [-f|--fullname] <Họ và tên> [-d|--date-of-birth] <ngày-tháng-năm>')
        print('Options:')
        print(' -f fullname, --fullname fullname')
        print('         Tên đầy đủ của đối tượng (bắt buộc)')
        print(' -d dob, --date-of-birth')
        print('         Ngày tháng năm sinh của đối tượng (bắt buộc)')
        print(' -n nickname --nickname nickname')
        print('         Nickname hoặc tên gọi khác của đối tượng')
        print(' -c      Thêm kết quả cho viết hoa chữ cái đầu')
        quit()

    parser = argparse.ArgumentParser(description=banner)

    parser.add_argument("-f", "--fullname", dest="fullname", required=True)
    parser.add_argument("-d", "--date-of-birth", dest="dob", required=True)
    parser.add_argument("-n", "--nickname", dest="nickname", required=False)
    parser.add_argument("-c", "--case-sensitive", dest="case", required=False, action="store_true")

    args = parser.parse_args()
    fullname = args.fullname
    dob = args.dob
    nickname = args.nickname
    case = args.case


    #quit if fullname is only a single word
    if len(fullname.split(" ")) == 1:
        print("[-] Họ tên gì chỉ một từ thế bro ?")
        quit()

    file_name = "passwords.txt"
    print("[+] Đợi chút nha bro :D")
    name_and_dob_based_gen(fullname=fullname, dob=dob)
    if nickname:
        nickname_and_dob_based_gen(nickname=nickname, dob=dob)
    with open(file_name, 'w') as file:
        for pw in list(set(results)):
            file.write(pw + "\n")
    
    if case:
        with open(file_name, 'a') as file:
            for pw in list(set(results)):
                file.write(pw.capitalize() + "\n")

    print("[+] Done, enjoy <3 ")
    quit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
