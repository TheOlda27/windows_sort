import os
import random
import shutil
import string


def sort(array):
    if not os.path.exists("sort_folder"):
        os.makedirs("sort_folder")
    
    for i in range(len(array)):
        open(("./sort_folder/"+array[i]),"a").close()
    
    fileList=os.listdir("./sort_folder")
    shutil.rmtree("./sort_folder")
    return fileList


def showcase():
    if not os.path.exists("sort_folder"):
        os.makedirs("sort_folder")
        
    for i in range(20):
        open("./sort_folder/"+"".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10)),"a").close()
    
    fileList=os.listdir("./sort_folder")
    shutil.rmtree("./sort_folder")
    
    for i in range(20):
        print(fileList[i])
