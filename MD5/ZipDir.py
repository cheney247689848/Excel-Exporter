#coding=utf-8
import os
import zipfile
import tarfile
import hashlib

#压缩文件或文件夹为zip
def zip_dir(srcPath , zipName):

    zipHandle=zipfile.ZipFile(zipName,'w',zipfile.ZIP_DEFLATED)
    for dirpath,dirs,files in os.walk(srcPath):
        for filename in files:
            #print (os.path.join(dirpath,filename))
            zipHandle.write(os.path.join(dirpath,filename) , filename) #必须拼接完整文件名，这样保持目录层级
            print ("   " + filename +" zip succeeded")

    zipHandle.close
    #contain = CreatMd5(os.path.abspath(dstname))
    #CreatTxt(os.path.abspath(txt) , contain)

#解压zip文件
def unzip_dir(srcname,dstPath):
    zipHandle=zipfile.ZipFile(srcname,"r")
    for filename in zipHandle.namelist():
        print (filename)
    zipHandle.extractall(dstPath) #解压到指定目录
    zipHandle.close()
    

    #压缩文件夹尾tar.gz
def tar_dir(srcPath,dstname):
    tarHandle=tarfile.open(dstname,"w:gz")
    for dirpath,dirs,files in os.walk(srcPath):
        for filename in files:
            tarHandle.add(os.path.join(dirpath,filename))
            print (filename+" tar succeeded")
            
    tarHandle.close()

#解压tar.gz文件到文件夹
def untar_dir(srcname,dstPath):
    tarHandle=tarfile.open(srcname,"r:gz")
    for filename in tarHandle.getnames():
        print (filename)
    tarHandle.extractall(dstPath)
    tarHandle.close()


def CreatMd5(file):
    md5file=open(file,'rb')
    md5 = hashlib.md5(md5file.read()).hexdigest()
    md5file.close()
    return md5


def CreatTxt(file , contain):

    fobj=open(file,'w')
    fobj.write(contain)   #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    fobj.close()          #   特别注意文件操作完毕后要close

def zip_allDir(srcPath):
    for dirpath,dirs,files in os.walk(srcPath):

            if len(files) > 0:
                print(dirpath)
                arr = dirpath.split('\\')
                zipFileName = arr[len(arr) - 1]
                zipName = zipFileName + ".zip"
                zip_dir(dirpath , zipName)
                md5 = CreatMd5(os.path.abspath(zipName))
                bytelen = os.path.getsize(zipName)
                txt = zipFileName + "|" + md5 + "|" + str(bytelen)
                print(txt)
                CreatTxt(zipFileName + ".txt" , txt)
    print("zip complete")


if __name__ == "__main__":
    
    #zip_dir("./Victorian","./dstdir/Victorian.zip") #可以用绝对或者相对路径的文件名或文件夹名
    #unzip_dir("./Victorian.zip",".")
    #tar_dir("./Victorian","./dstdir/Victorian.tar.gz")
    #untar_dir("./Victorian.tar.gz","./")

    #zip_dir("ResUpdate_Main","ResUpdate_Main.zip" , "ResUpdate_Main.txt")
    zip_allDir("ResUpdate")

    if os.path.exists('files.txt'):
        os.remove('files.txt')
    
    if os.path.exists('Android.txt'):
        os.rename('Android.txt','files.txt')

    if os.path.exists('IOS.txt'):
        os.rename('IOS.txt','files.txt')
