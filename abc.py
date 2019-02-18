# coding = utf-8
a = []

for i in range(65, 91):
    a.append(chr(i))

while True:
    b = input('请输入大写字母:')
    if b in a:
        print(a.index(b)+1)


