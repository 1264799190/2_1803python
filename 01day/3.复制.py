flie_name = input('请输入文件名')
f = open('1.txt','r')
content = f.read()

f1 = open('3.txt','w')
f1.write(content)

f.close()
f1.close()
