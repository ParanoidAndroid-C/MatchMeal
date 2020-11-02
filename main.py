import importlib
#Generate Data
modname_generate = "generatedata"
module_generate = importlib.import_module(modname_generate)


modname_read = "readdata"
funcname = "readData"
module_read = importlib.import_module(modname_read)
func = getattr(module_read, funcname)
myData = func('data.txt')
cnt = 0
for i in myData:
    for j in range(0, len(myData[i]['restaurant_menu'])):
        cnt += 1

print(cnt)        