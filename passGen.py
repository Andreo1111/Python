import random, string
import platform
import os


osVers = platform.system()
curDirs = os.getcwd()
path_file = ""

def gen():
    passw = ''
    dig = string.digits
    simb = string.punctuation
    strg = string.ascii_letters
    res = dig+simb+strg
    for i in range(random.randrange(14,16)):
        passw +=random.choice(res)
    return passw

def in_file(path_file):
    with open (path_file,'a',encoding='utf-8') as file_pass:
        finalFile = file_pass.write(gen()+"\n")

print(osVers)
for i in range(10):
    in_file(curDirs +'/'+'passwd.txt')
