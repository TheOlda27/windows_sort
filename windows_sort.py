import os
import shutil
import random
import string

ranFlag=False

if not os.path.exists("sort_folder"):
    os.makedirs("sort_folder")

arrayLen=int(input("The length of your array is? (0 for random): "))

if(arrayLen==0):
    arrayLen=random.randint(10,50)
    ranFlag=True

for i in range(0,arrayLen,1):
    if(ranFlag==False):
        open("./sort_folder/"+input("What do you want to sort?: "),"a").close()
    else:
        open("./sort_folder/"+"".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10)),"a").close()

fileList=os.listdir("./sort_folder")

for i in range(len(fileList)):
    print(fileList[i])

shutil.rmtree("./sort_folder")