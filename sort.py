import os
import shutil
path = input(" Enter Path Direcrtory ")
lis1 = os.listdir(path)
for fil in lis1:
    name, extn = os.path.splitext(fil)
    extn = extn[1:]
    if extn == '':
        continue
    if os.path.exists(path + '/' + extn):
        shutil.move(path + '/' + fil, path + '/' + extn + '/' + fil)
    else:
        os.makedirs(path + '/' + extn)
        shutil.move(path + '/' + fil, path + '/' + extn + '/' + fil)
