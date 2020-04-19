import errno
import os
import shutil
from datetime import datetime


mydir = os.path.join(os.getcwd(),datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
try:
    os.makedirs(mydir)
except OSError as e:
    if e.errno != errno.EEXIST:
          raise 
curent_path=os.getcwd()
print(mydir)

for file in os.listdir(curent_path):
    if file.endswith('xlsx'):
        source=os.path.join(curent_path,file)
        print(shutil.move(source, mydir))