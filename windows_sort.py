import os
import shutil
import random

ranFlag=False

if not os.path.exists("sort_folder"):
    os.makedirs("sort_folder")

arrayLen=int(input("The length of your array is? (0 for random): "))

if(arrayLen==0):
    arrayLen=random.randint(2,50)
    ranFlag=True

for i in range(0,arrayLen,1):
    if(ranFlag==False):
        open("./sort_folder/"+input("What do you want to sort?: "),"a").close()
    else:
        open("./sort_folder/"+str(random.randint(0,4294967296)),"a").close() #generate random string, maybe?

print(os.listdir("./sort_folder"))

shutil.rmtree("./sort_folder")