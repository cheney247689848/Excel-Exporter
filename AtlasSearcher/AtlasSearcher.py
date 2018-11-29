#coding=utf-8
import os
import shutil
import re


#读取atlas文件
def read_Atals(context):
    regex = re.compile("[a-zA-Z1-9_-]+\.png")
    # print (context)
    print (regex.findall(context))
    return regex.findall(context)

#copy 文件
def copy_file(old_name , new_name):
    shutil.copyfile(old_name,new_name)

#查找复制texture文件
def search_info(name_arr , src_oldpath , src_newpath):
    for item in name_arr:
        find_num = 0
        for dirpath,dirs,files in os.walk(src_oldpath):
            if len(files) > 0:
                for f in files:
                    if str(f) == str(item):
                        old_path = os.path.join(dirpath,f)
                        new_path = os.path.join(src_newpath,f)
                        # if find_num > 0:
                        ver = "    -   " + str(find_num) + "   ("+ old_path.replace("/", "-").replace("\\", "-").replace(".png", "").replace(":", "") + ")"
                        new_path = new_path.replace("." , ver + ".")
                        find_num += 1
                        # print (old_path)
                        print (new_path)
                        copy_file(str(old_path),str(new_path))
        if find_num == 0:
            print ("no find the sprite name - " + str(item))

if __name__ == "__main__":

    flie_object = open("public2.txt")
    file_context = flie_object.read()
    arr = read_Atals(file_context)
    search_info(arr , "F:/COMPANY+/MJ/art/badawan_a/" , "F:/COMPANY+/MJ/abc/")
    print ("search finsh")