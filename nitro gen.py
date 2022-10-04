import os, random, string
os.system("cls")
total=input("how many codes u want?: ")
num = int(total)
file = ("Nitro codes.txt")
file2 = 'codes generated.txt'
for i in range(num):
    c="https://discord.gift/"
    code= ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
    kk = c+code
    newline = "\n"
    with open(file, 'a') as out:
        out.write(kk+newline)
        os.system("cls")
print("Thanks for using")