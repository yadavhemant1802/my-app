
import os
import sys
from datetime import datetime
path=os.getcwd()
print(path)
File_move = sys.argv[1]
for dir_name in os.listdir():
    if dir_name=="target":
        absolute_path=os.path.join(path,dir_name)
        print(absolute_path)
        #path1=os.chdir(absolute_path)
        for file in os.listdir(absolute_path):
            if file.endswith('xlsx'):
                file_name,file_ext= os.path.splitext(file)
                timestamp = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
                Package =('{}_{}'.format(file_name,timestamp))
                packagewithtimestamp = Package+".xlsx"
                if os.path.exists(File_move):
                    os.rename(absolute_path,File_move)
                else:
                    print("Path to move jar file not found")
               
        break
    else:
        print("No directory found")