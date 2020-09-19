import os
import shutil

folder = "/Queues"
path = "C:/Users/username/Desktop/simple projects"
for file in os.listdir(path):
    # get all but the last 8 characters to remove
    # the index number and extension
    if "queue" in file:
        dir_path = path + folder
        print(f'dir_path: {dir_path}')
    
    # check if directory exists or not yet
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if os.path.exists(dir_path):
            file_path = dir + file
            print(f'file_path: {file_path}')
        
        # move files into created directory
        shutil.move(file_path, dir_path)