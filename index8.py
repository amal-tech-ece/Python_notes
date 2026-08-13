# f=open("sample.txt","w")
# f.write("Learn Python")
# f.close()


# f=open(r"D:\python\data.txt","w")
# f.close()


# f=open("sample.txt","r")
# print(f.read())
# f.close()

# f=open("sample.txt","r")
# # f.write("Learn Javascript\n")
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# print(f.readlines())
# f.close()


# f=open("sample1.txt","x")
# f.close()


# f=open("WhatsApp Image 2025-10-30 at 21.09.39_065aaa7d.jpg","rb")
# # print(f.read())
# print(f.read(20))
# f.close()

# f=open("sample.txt","r+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close
# f=open("sample.txt","r+")
# print(f.read())
# f.close


# f=open("sample.txt","w+")
# print(f.read())
# f.write("goodbye\n")
# print(f.read())
# f.close()

f=open("sample.txt","a+")
print(f.read())
f.write("goodbye\n")
print(f.read())
f.close()