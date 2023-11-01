# Overview
- Đây là 1 tool mình ngẫu hứng viết ra, khá hữu dụng và hiệu quả (nếu cho mục đích tốt :D)
- Tool này sẽ generate ra các mật khẩu yếu có thể được sử dụng từ thông tin của người mà mình cung cấp theo pattern của cá nhân mà mình nghĩ là dễ đặt theo nhất
- Nếu cảm thấy không ổn mọi người có thể tự custom lại khiến cho tool trở nên hiệu quả hơn, và hơn nữa code chỉ là mình code qua cho xong để làm task nên nhiều chỗ không ổn cho lắm trông khá tệ về mặt thẩm mĩ và logic =))) Enjoy <3
# Installation
```
┌──(dwgth4i👻Kali-PC)-[~/scripts]
└─$ git clone https://github.com/dwgth4i/TheWeakEnd
Cloning into 'TheWeakEnd'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 15 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (15/15), 5.42 KiB | 924.00 KiB/s, done.
Resolving deltas: 100% (2/2), done.
```
# Usage
```
python3 theweakend.py <họ và tên> <nickname> <ngày sinh (ngày-tháng-năm)>
```
### Ví dụ
```
# Script sẽ generate ra các passwords, sau đó tạo và ghi thẳng vào 1 file tên là passwords.txt cùng thư mục với đoạn script này.
┌──(dwgth4i👻Kali-PC)-[~/scripts]
└─$ python3 theweakend.py "Le Van A" "ale123" "1-1-2000"
[+] Đợi chút nha bro :D
[+] Done, enjoy <3
```
# Requirements
- Tool được chạy trên máy mình với Python 3.11, không sử dụng thư viện gì nhiều, chỉ code logic, nên khả năng chỉ cần Python 3 trở lên là chạy được

