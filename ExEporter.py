
import xlrd
import os

def Transforkey(_str_type, _value):
    """转换key类型"""
    temp_value = _value
    if _str_type == "string":
          temp_value = "" + temp_value.encode('utf-8')
    elif _str_type == "int":
          if temp_value != "":
              temp_value = int(temp_value)
          else:
              temp_value = 0
    elif _str_type == "float":
          if temp_value != "":
              temp_value = float(temp_value)
          else:
              temp_value = 0   
    elif _str_type == "table":
          if temp_value != "":
              temp_value = temp_value
          else:
              temp_value = "nil"
    else:
        return None
    return '    [{0}] = '.format(temp_value)
    #[][]
def Transfor(_str_type, _value):
    """转换类型"""
    temp_value = _value
    if _str_type == "string":
        temp_value = "" + temp_value.encode('utf-8')
    elif _str_type == "int":
        if temp_value != "":
            temp_value = int(temp_value)
        else:
            temp_value = 0
    elif _str_type == "float":
        if temp_value != "":
            temp_value = float(temp_value)
        else:
            temp_value = 0   
    elif _str_type == "table":
        if temp_value != "":
            temp_value = temp_value
        else:
            temp_value = "nil"
    else:
        return None
    return temp_value
    # if _iskey:
    #     return '    [{0}] = '.format(temp_value)
    # else:
    #     return '{0} = {1}'.format(_name, temp_value)

# def CombinKey(_str_type, _name, _value, _iskey = False):
    

def ExPortTable(_table, _table_name):
    """输出表内容"""
    ncols = _table.ncols
    nrows = _table.nrows
    print "输出 : %s      ncols = %d, nrows = %d" % (_table_name, ncols, nrows)
    strkey = _table.cell_value(0,0)
    if strkey == "key2":
        #双键
        strInfo = _table_name + "{\r\n"
        for i in range(5,nrows):
            
            for j in range(1 , ncols):
                
                t1 = _table.cell_value(1,j)
                t2 = _table.cell_value(1,j)
                n = _table.cell_value(3,j)
                v1 = _table.cell_value(i,j)
                v2 = _table.cell_value(i,j)
                if j == 1:
                    s = '    [{0}][{1}] = '.format(Transfor(t1, v1) , Transfor(t2, v2)) #key
                else:
                    s = '{0} = {1}'.format(n, Transfor(t1, v1))
                if j != 1:
                    strInfo = strInfo + s + ","
                elif j == ncols:
                    strInfo = strInfo + s
                else:
                    strInfo = strInfo + s + "{"
            strInfo = strInfo + "},\r\n"
        strInfo = strInfo + "}"
        print(strInfo)
    else:
        #单键
        strInfo = _table_name + "{\r\n"
        for i in range(5,nrows):
            
            for j in range(1 , ncols):
                
                t = _table.cell_value(1,j)
                n = _table.cell_value(3,j)
                v = _table.cell_value(i,j)
                if j == 1:
                    s = '    [{0}] = '.format(Transfor(t, v)) #key
                else:
                    s = '{0} = {1}'.format(n, Transfor(t, v))
                if j != 1:
                    strInfo = strInfo + s + ","
                elif j == ncols:
                    strInfo = strInfo + s
                else:
                    strInfo = strInfo + s + "{"
            strInfo = strInfo + "},\r\n"
        strInfo = strInfo + "}"
        print(strInfo)


          















    # fo.write(strInfo.encode());
    # fo.close();  


    return 0

excel_path = "./Excel"
for dirpath, dirs, files in os.walk(excel_path):
    for filename in files:  
        # print "file : " + filename
        if filename.find("~$") == -1:
            excel = xlrd.open_workbook(excel_path + "/" +  filename)
            for i in range(len(excel.sheets())):
                table = excel.sheets()[i]
                if table.name.find("Sheet") == -1:
                    ExPortTable(table, str(table.name))
             



url = input();
url = input();
url = input();
url = input();
url = input();
url = u'导表模板.xlsx';
url.replace('\\','/');
print(url);input();


# thedir = os.getcwd();

# # 要转的文件名 关卡表
# excel_name = url;
# #excel_name = u'导表模板.xlsx';
# # 要转的工作簿名称
# sheet_name = "Sheet1";
# bk = xlrd.open_workbook(excel_name);
# shxrange = range(bk.nsheets);
# try:
#     sh = bk.sheet_by_name(sheet_name);
# except:
#     print("no sheet in %s named skill" % fname);

# nrows = sh.nrows;
# ncols = sh.ncols;
# print("nrows %d, ncols %d" % (nrows, ncols));

# key = 2 #默认健位
# table_name = sh.cell_value(0,0); # 读取lua table 的名称  默认 A1

# #服务器导出 ----------------------------------------------------
# lua_name = "lua\\服务器\\s"+ table_name + ".lua";
# fo = open(lua_name, "wb");

# strInfo = "s" + table_name + " = {\r\n\n";
# if key == 1:

#     for i in range(5,nrows):
#         #键位设定
#         cType = sh.cell_value(1,1);
#         cValue = sh.cell_value(i,1);
#         strKey0 = None;
#         if cType == 2:

#             strKey0 = int(cValue);
#         else:
#             strKey0 = "\"" + str(cValue) +"\"";
#         strInfo = strInfo + "   [" + str(strKey0) + "] = {" ;

#         for j in range(1 + key , ncols):
#           #print(i , j);
#           cValue = sh.cell_value(i,j);
#           cType = sh.cell_value(1,j);
#           cSerName = sh.cell_value(2,j);
          
#           if cSerName != "" and cValue != "":

#              vStr = Transfor(cValue, cType ,cSerName);
#              if j != 1 + key:

#                 strInfo = strInfo + "," + vStr;
#              else:
                
#                 strInfo = strInfo + vStr;
             
#              #strInfo = strInfo + vStr +",";            
#           else:
#              #print("")
#              empty = None

#         if i != nrows - 1:
#             strInfo = strInfo + "},\r\n";
#         else:
#             strInfo = strInfo + "}\r\n";
            
#     print(strInfo);
#     strInfo = strInfo + "};";
#     fo.write(strInfo.encode());
#     fo.close();    

# else:
#     #双健值
#     curKey = None;
#     #遍历表
#     for i in range(5,nrows):

#         cType = sh.cell_value(1,1);
#         cValue = sh.cell_value(i,1);
#         strKey0 = None;
#         #key0
#         if cType == 2:

#            strKey0 = int(cValue);
#         else:
#            strKey0 = "\"" + str(cValue) +"\"";
#         #key1
#         cType = sh.cell_value(1,2);
#         cValue = sh.cell_value(i,2);
#         strKey1 = None;
#         if cType == 2:

#            strKey1 = int(cValue);
#         else:
#            strKey1 = "\"" + str(cValue) +"\"";

#         if i == 5:

#             curKey = strKey0;
#             strInfo = strInfo + "   [" + str(strKey0) + "] = {\n" ;
#             strInfo = strInfo + "       [" + str(strKey1) + "] = {" ;
#         else:

#             if curKey != strKey0:
                
#                 strInfo = strInfo + "   }\n   [" + str(strKey0) + "] = {\n" ;
                
#             curKey = strKey0;
#             strInfo = strInfo + "       [" + str(strKey1) + "] = {" ;

#         for j in range(3 , ncols):
#           print(i , j);
#           cValue = sh.cell_value(i,j);
#           cType = sh.cell_value(1,j);
#           cSerName = sh.cell_value(2,j);
          
#           if cSerName != "" and cValue != "":

#              vStr = Transfor(cValue, cType ,cSerName);
#              if j != 1 + key:

#                 strInfo = strInfo + "," + vStr;
#              else:
                
#                 strInfo = strInfo + vStr;
             
#              #strInfo = strInfo + vStr +",";            
#           else:
#              #print("")
#              empty = None

#         strInfo = strInfo + "},\r\n";

#     print(strInfo);
#     strInfo = strInfo + "   }; \n}";
#     fo.write(strInfo.encode());
#     fo.close();   
# print("完成");
# input();















