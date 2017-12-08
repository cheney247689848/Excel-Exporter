#coding=utf-8
import os
import zipfile
import tarfile

#压缩文件或文件夹为zip
def zip_dir(srcPath,dstname):
    zipHandle=zipfile.ZipFile(dstname,'w',zipfile.ZIP_DEFLATED)

    for dirpath,dirs,files in os.walk(srcPath):
        for filename in files:
            zipHandle.write(os.path.join(dirpath,filename)) #必须拼接完整文件名，这样保持目录层级
            print filename +" zip succeeded"

    zipHandle.close

#解压zip文件
def unzip_dir(srcname,dstPath):
    zipHandle=zipfile.ZipFile(srcname,"r")
    for filename in zipHandle.namelist():
        print filename
    zipHandle.extractall(dstPath) #解压到指定目录
    
    zipHandle.close()
    

    #压缩文件夹尾tar.gz
def tar_dir(srcPath,dstname):
    tarHandle=tarfile.open(dstname,"w:gz")
    for dirpath,dirs,files in os.walk(srcPath):
        for filename in files:
            tarHandle.add(os.path.join(dirpath,filename))
            print filename+" tar succeeded"
            
    tarHandle.close()

#解压tar.gz文件到文件夹
def untar_dir(srcname,dstPath):
    tarHandle=tarfile.open(srcname,"r:gz")
    for filename in tarHandle.getnames():
        print filename
    tarHandle.extractall(dstPath)
    tarHandle.close()

if __name__ == "__main__":
    
    #zip_dir("./Victorian","./dstdir/Victorian.zip") #可以用绝对或者相对路径的文件名或文件夹名
    #unzip_dir("./Victorian.zip",".")
    #tar_dir("./Victorian","./dstdir/Victorian.tar.gz")
    untar_dir("./Victorian.tar.gz","./")
