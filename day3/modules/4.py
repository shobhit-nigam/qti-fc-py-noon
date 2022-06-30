import os
from datetime import datetime

objd = os.path.getatime('1.py')

print(datetime.fromtimestamp(objd).strftime('%Y %m %d %H:%M:%S'))
