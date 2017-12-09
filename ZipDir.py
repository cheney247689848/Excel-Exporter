#coding=utf-8
import os
import zipfile
import tarfile

#压缩文件或文件夹为zip
def zip_dir(srcpath, dstname):
    """zip the srcpath in to dstname ."""
    ziphandle = zipfile.ZipFile(dstname, 'w', zipfile.ZIP_DEFLATED)
    for dirpath , dirs , files in os.walk(srcpath):
        for filename in files:
            ziphandle.write(os.path.join(dirpath, filename)) #必须拼接完整文件名，这样保持目录层级
            print filename + " zip succeeded"
    ziphandle.close()

#解压zip文件
def unzip_dir(srcname, dstpath):
    """unzip the srcpath in to dstname ."""
    zip_handle = zipfile.ZipFile(srcname, "r")
    for filename in zip_handle.namelist():
        print filename
    zip_handle.extractall(dstpath) #解压到指定目录
    zip_handle.close()

    #压缩文件夹尾tar.gz
def tar_dir(srcpath, dstname):
    """tar the srcpath in to dstname ."""
    tarhandle = tarfile.open(dstname, "w:gz")
    for dirpath , dirs , files in os.walk(srcpath):
        for filename in files:
            tarhandle.add(os.path.join(dirpath, filename))
            print filename+" tar succeeded"
    tarhandle.close()

#解压tar.gz文件到文件夹
def untar_dir(srcname, dstpath):
    """untar the srcpath in to dstname ."""
    tarhandle = tarfile.open(srcname, "r:gz")
    for filename in tarhandle.getnames():
        print filename
    tarhandle.extractall(dstpath)
    tarhandle.close()

if __name__ == "__main__":
    
    untar_dir("./Victorian.tar.gz","./")
    #zip_dir("./Victorian","./dstdir/Victorian.zip") #可以用绝对或者相对路径的文件名或文件夹名
    #unzip_dir("./Victorian.zip",".")
    #tar_dir("./Victorian","./dstdir/Victorian.tar.gz")