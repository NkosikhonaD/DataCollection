import os
import shutil

path ="C:\\Users\\DlaminiN3\Downloads\\final_data"
dest ="C:\\Users\\DlaminiN3\Downloads\\final_data"
list_char_folders = os.listdir(path)

for tr in list_char_folders:
    author_path = path+"\\"+tr
    list_authors = os.listdir(author_path)
    lastl = tr[-1:]
    for author in list_authors:
        data_path = author_path+"\\"+author
        des = dest
        try:
            os.makedirs(des+"\\testing"+"_"+str(lastl)+"\\"+author)
        except FileExistsError:
            print("Directory cannot be created")
        list_data = os.listdir(data_path)
        if len(list_data)>9:
            shutil.move(data_path+"\\"+list_data[0],des+"\\testing"+"_"+str(lastl)+"\\"+author)
            shutil.move(data_path+"\\"+list_data[1],des+"\\testing"+"_"+str(lastl)+"\\"+author)
            shutil.move(data_path+"\\"+list_data[3],des+"\\testing"+"_"+str(lastl)+"\\"+author)
