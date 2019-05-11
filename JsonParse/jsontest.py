import json
print("hello world!")
f = open("json/lan.json", encoding='utf-8')
jsondata = json.load(f)
ss = ''
for key in jsondata['data']:

    # ss = ss + "area" + str(key['id']) + "=" + str(key['name_zh']) + '\n'
    # ss = ss + "area" + str(key['id']) + "=" + str(key['name_en']) + '\n'
    ss = ss + str(key['nId']) + "=" + str(key['sName']) + '\n'
print(ss)
