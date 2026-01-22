# encoding
uni_str = "Life is too short"
byte_str = uni_str.encode('utf-8')

print(byte_str)
print(type(byte_str))

kor_str = "한글"
# kor_str.encode("ascii") > UnicodeEncodeError

print(kor_str.encode("euc-kr"))
print(kor_str.encode("utf-8"))

# decoding
euckr_str = kor_str.encode("euc-kr")
print(euckr_str.decode("euc-kr"))
# print(euckr_str.decode("utf-8")) > UnicodeDecodeError

# encoding and file io
with open("euc-kr_file.txt", encoding="euc-kr") as f:
    data = f.read()

data = data + "\n" + "안녕하세요"

with open("euc-kr_file.txt", encoding="euc-kr", mode="w") as f:
    f.write(data)

print(data)

# source code encoding
#-*-coding:utf-8 -*-
