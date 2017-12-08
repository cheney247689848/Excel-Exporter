
#1 表示字符串
#2 表示数字(整型)
#3 浮点型
#4 表
def Transfor(v , t , n):

    mv = v;
    if t == 1:
          mv = "\"" + mv +"\"";
          
    if t == 2:
          if mv != "":
              mv = int(mv);
          else:
              #print("xls error cellvalue is null");
              mv = 0;

    if t == 3:
          if mv != "":
              mv = float(mv);
          else:
              #print("xls error cellvalue is null");
              mv = 0;
            
    if t == 4:
          if mv != "":
              mv = mv;
          else:
              mv = "nil"

    #print(n + " [=] " + str(mv))
    return n + " = " + str(mv)

url = input();
url = u'导表模板.xlsx';
url.replace('\\','/');
print(url);input();
import xlrd
import os

thedir = os.getcwd();

# 要转的文件名 关卡表
excel_name = url;
#excel_name = u'导表模板.xlsx';
# 要转的工作簿名称
sheet_name = "Sheet1";
bk = xlrd.open_workbook(excel_name);
shxrange = range(bk.nsheets);
try:
    sh = bk.sheet_by_name(sheet_name);
except:
    print("no sheet in %s named skill" % fname);

nrows = sh.nrows;
ncols = sh.ncols;
print("nrows %d, ncols %d" % (nrows, ncols));

key = 2 #默认健位
table_name = sh.cell_value(0,0); # 读取lua table 的名称  默认 A1

#服务器导出 ----------------------------------------------------
lua_name = "lua\\服务器\\s"+ table_name + ".lua";
fo = open(lua_name, "wb");

strInfo = "s" + table_name + " = {\r\n\n";
if key == 1:

    for i in range(5,nrows):
        #键位设定
        cType = sh.cell_value(1,1);
        cValue = sh.cell_value(i,1);
        strKey0 = None;
        if cType == 2:

            strKey0 = int(cValue);
        else:
            strKey0 = "\"" + str(cValue) +"\"";
        strInfo = strInfo + "   [" + str(strKey0) + "] = {" ;

        for j in range(1 + key , ncols):
          #print(i , j);
          cValue = sh.cell_value(i,j);
          cType = sh.cell_value(1,j);
          cSerName = sh.cell_value(2,j);
          
          if cSerName != "" and cValue != "":

             vStr = Transfor(cValue, cType ,cSerName);
             if j != 1 + key:

                strInfo = strInfo + "," + vStr;
             else:
                
                strInfo = strInfo + vStr;
             
             #strInfo = strInfo + vStr +",";            
          else:
             #print("")
             empty = None

        if i != nrows - 1:
            strInfo = strInfo + "},\r\n";
        else:
            strInfo = strInfo + "}\r\n";
            
    print(strInfo);
    strInfo = strInfo + "};";
    fo.write(strInfo.encode());
    fo.close();    

else:
    #双健值
    curKey = None;
    #遍历表
    for i in range(5,nrows):

        cType = sh.cell_value(1,1);
        cValue = sh.cell_value(i,1);
        strKey0 = None;
        #key0
        if cType == 2:

           strKey0 = int(cValue);
        else:
           strKey0 = "\"" + str(cValue) +"\"";
        #key1
        cType = sh.cell_value(1,2);
        cValue = sh.cell_value(i,2);
        strKey1 = None;
        if cType == 2:

           strKey1 = int(cValue);
        else:
           strKey1 = "\"" + str(cValue) +"\"";

        if i == 5:

            curKey = strKey0;
            strInfo = strInfo + "   [" + str(strKey0) + "] = {\n" ;
            strInfo = strInfo + "       [" + str(strKey1) + "] = {" ;
        else:

            if curKey != strKey0:
                
                strInfo = strInfo + "   }\n   [" + str(strKey0) + "] = {\n" ;
                
            curKey = strKey0;
            strInfo = strInfo + "       [" + str(strKey1) + "] = {" ;

        for j in range(3 , ncols):
          print(i , j);
          cValue = sh.cell_value(i,j);
          cType = sh.cell_value(1,j);
          cSerName = sh.cell_value(2,j);
          
          if cSerName != "" and cValue != "":

             vStr = Transfor(cValue, cType ,cSerName);
             if j != 1 + key:

                strInfo = strInfo + "," + vStr;
             else:
                
                strInfo = strInfo + vStr;
             
             #strInfo = strInfo + vStr +",";            
          else:
             #print("")
             empty = None

        strInfo = strInfo + "},\r\n";

    print(strInfo);
    strInfo = strInfo + "   }; \n}";
    fo.write(strInfo.encode());
    fo.close();   
print("完成");
input();















