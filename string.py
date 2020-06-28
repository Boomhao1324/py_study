print("hello world")
message = "my study of python is beginning"
print(message)

# 首字母大写
print(message.title())
name = "Boom Hao"

# 全大小写
print(name.upper())
print(name.lower())

# 合并字符串
first_name = "Boom"
last_name = "Hao"
full_name  = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
hello = "Hello, " + full_name.title() + "!"
print(hello)

# 制表符and换行符
print("languages:\nC\nC++\nJAVA\nPYTHON")
print("PYTHON")
print("\tPYTHON")
print("languages:\n\tC\n\tC++\n\tJAVA\n\tPYTHON")

# 删除空白
# 末尾
blank1 = "PY   "
print(blank1)
print(blank1.rstrip())
print(blank1)
blank1 = blank1.rstrip()
print(blank1)
# 开头
blank2 = "  py"
print(blank2)
print(blank2.lstrip())
# 两头
blank3 = "  py  "
print(blank3)
print(blank3.strip())

