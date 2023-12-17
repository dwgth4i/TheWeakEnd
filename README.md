# Overview
- Tool này sẽ generate ra các mật khẩu yếu có thể được sử dụng từ thông tin của người mà mình cung cấp theo pattern của cá nhân mà mình nghĩ là dễ đặt theo nhất (ở Việt Nam)
- Nếu cảm thấy không ổn mọi người có thể tự custom lại khiến cho tool trở nên hiệu quả hơn, và hơn nữa mình chỉ code qua cho xong để làm task nên nhiều chỗ không ổn cho lắm trông khá tệ về mặt thẩm mĩ và logic (quan trọng là kết quả, right? =)))) 
# Installation
```
 git clone https://github.com/dwgth4i/TheWeakEnd
```
# Usage
```
🐧  dwgth4i on 21DWGTH4I at …/scripts python3 theweakend.py
_________          _______             _______  _______  _          _______  _        ______
\__   __/|\     /|(  ____ \  |\     /|(  ____ \(  ___  )| \    /\  (  ____ \( (    /|(  __  \
   ) (   | )   ( || (    \/  | )   ( || (    \/| (   ) ||  \  / /  | (    \/|  \  ( || (  \  )
   | |   | (___) || (__      | | _ | || (__    | (___) ||  (_/ /   | (__    |   \ | || |   ) |
   | |   |  ___  ||  __)     | |( )| ||  __)   |  ___  ||   _ (    |  __)   | (\ \) || |   | |
   | |   | (   ) || (        | || || || (      | (   ) ||  ( \ \   | (      | | \   || |   ) |
   | |   | )   ( || (____/\  | () () || (____/\| )   ( ||  /  \ \  | (____/\| )  \  || (__/  )
   )_(   |/     \|(_______/  (_______)(_______/|/     \||_/    \/  (_______/|/    )_)(______/

[+] Usage: python3 theweakend.py [-f|--fullname] <Họ và tên> [-d|--date-of-birth] <ngày-tháng-năm>
Options:
 -f fullname, --fullname fullname
         Tên đầy đủ của đối tượng (bắt buộc)
 -d dob, --date-of-birth
         Ngày tháng năm sinh của đối tượng (bắt buộc)
 -n nickname --nickname nickname
         Nickname hoặc tên gọi khác của đối tượng
 -c      Thêm kết quả cho viết hoa chữ cái đầu
```
### Ví dụ
```
# Script sẽ generate ra các passwords, sau đó tạo và ghi thẳng vào 1 file tên là passwords.txt cùng thư mục với đoạn script này.
🐧  dwgth4i on 21DWGTH4I at …/scripts python3 theweakend.py -f "Trinh Thai Duong" -d 13-10-2003 -n dwgth4i -c
[+] Đợi chút nha bro :D
[+] Done, enjoy <3
```
# Requirements
- Tool được chạy trên máy mình với Python 3.11, không sử dụng thư viện gì nhiều, chỉ code logic, nên khả năng chỉ cần Python 3 trở lên là chạy được

