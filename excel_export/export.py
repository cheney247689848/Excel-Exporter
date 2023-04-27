# encoding : utf-8      #设置编码方式
import sys
import xlrd
import os

import export_lua_format as luaf
import export_json_format as jsonf
   
def main():
    print("参数:" , sys.argv)
    if len(sys.argv) != 4:
        print("参数长度错误")
        return
    output_type = sys.argv[1]
    excel_path = sys.argv[2]
    output_path = sys.argv[3]
      
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for dirpath, dirs, files in os.walk(excel_path):
        for filename in files:  
            # print "file : " + filename
            if filename.find("~$") == -1: #排除缓存文件
                excel = xlrd.open_workbook(excel_path + "/" +  filename)
                for i in range(len(excel.sheets())):
                    table = excel.sheets()[i]
                    if table.name.find("Sheet") == -1: #排除无用表
                        if output_type.find("lua") != -1:
                            strInfo = luaf.exporttable(table, table.name)
                            #表导出 ----------------------------------------------------
                            lua_name = output_path + "\\"+ table.name + ".lua"
                            fo = open(lua_name, "wb")
                            fo.write(strInfo.encode('utf-8'))
                            fo.close(); 
                            print ("export  " + lua_name + "  finsh......")
                        else:
                            strInfo = jsonf.exporttable(table, table.name)
                            #表导出 ----------------------------------------------------
                            lua_name = output_path + "\\"+ table.name + ".json"
                            fo = open(lua_name, "wb")
                            fo.write(strInfo.encode('utf-8'))
                            fo.close(); 
                            print ("export  " + lua_name + "  finsh......")

if __name__ == "__main__":
    main()
    os.system("pause")

