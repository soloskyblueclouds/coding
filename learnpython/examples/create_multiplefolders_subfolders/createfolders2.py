#!/usr/local/bin/python3

import os
root_path =r"/Users/ninjawarrior/Google Drive/Augumented_Intelligence/6.Github/coding_adventure/learnpython/create_multiplefolders_subfolders"
sub_folders = ['Map1, Map2, Map3, Map4']
folders = []
for path in os.listdir(root_path):
   folders.append(os.path.join(root_path, path))
   print (folders)

for f in folders:
    os.makedirs(os.path.join(f, folders))

for f in folders:
    os.chdir(f)
    for sub_folder in sub_folders:
        os.mkdir(sub_folder)
