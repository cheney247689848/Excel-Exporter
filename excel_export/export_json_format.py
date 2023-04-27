# encoding : utf-8      #设置编码方式
import xlrd
import os

def transfor(_str_type, _value):
    """转换类型"""
    temp_value = _value
    if _str_type == "string":
        #temp_value = "\"" + temp_value.encode('utf-8') + "\""
        temp_value = '\"%s\"'%(temp_value)
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
            temp_value = "null"
    else:
        return None
    return temp_value

def exporttable(_table, _table_name):
    """输出表内容"""
    ncols = _table.ncols
    nrows = _table.nrows
    print ("输出 : %s      ncols = %d, nrows = %d" % (_table_name, ncols, nrows))
    strkey = _table.cell_value(0,0)
    strInfo = ""
    errorInfo = "错误导出信息:\n"
    if strkey == "key2":
        #双键
        strInfo = "{\r\n"
        for i in range(5,nrows):
            
            strInfo = strInfo + '    [{0}][{1}] = '.format(transfor(_table.cell_value(1,1), _table.cell_value(i,1)) , transfor(_table.cell_value(1,2), _table.cell_value(i,2))) #key
            strInfo = strInfo + '{'
            for j in range(3 , ncols):
                t = _table.cell_value(1, j)
                n = _table.cell_value(3, j)
                v = _table.cell_value(i, j)
                s = '{0} = {1}'.format(n, transfor(t, v))
                if j == ncols - 1:
                    strInfo = strInfo + s
                else:
                    strInfo = strInfo + s + ","
            strInfo = strInfo + "},\r\n"
        strInfo = strInfo + "}"
        print (strInfo)
    else:
        #单键
        strInfo = "{\r\n"
        strInfo += '    "data":[\n'
        for i in range(5, nrows):
            
            #strInfo = strInfo + '[{0}] = '.format(transfor(_table.cell_value(1, 1), _table.cell_value(i, 1)))
            strInfo = strInfo + '      {'
            for j in range(1, ncols):
                t = _table.cell_value(1, j)
                n = _table.cell_value(3, j)
                v = _table.cell_value(i, j)
                try:
                    s = '"{0}":{1}'.format(n, transfor(t, v))
                    if j == ncols - 1:
                        strInfo = strInfo + s
                    else:
                        strInfo = strInfo + s + ","
                except:
                    errorInfo = errorInfo + '行:%d , 列:%d\n'%(i + 1 , j + 1)
            if i == nrows - 1:
                strInfo = strInfo + "}\r\n"
            else:
                strInfo = strInfo + "},\r\n"
        strInfo = strInfo + "   ]\n}"
        print (strInfo)
    return strInfo
