import os

cur_path = '/Users/shobhit/Desktop/qualcomm/noon/day3'
for path, dir_names, filenames in os.walk(cur_path):
    print(path)
    print(dir_names)
    print(filenames)
