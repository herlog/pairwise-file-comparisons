#https://www.herlog.com/two-ways-to-get-started-with-diff-for-bioinformatics-using-python-and-excel-to-output-a-shell-script-with-pairwise-comparisons/

import os

# Function to grep string s given list l, outputs a list
def grep(l, s):
    return [i for i in l if s in i]

# Returns the paths of all *.txt files in a given directory path
def get_filepaths_from_directory(loc_dir):
    paths = []
    #Find all *txt in all subdirectories
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))
                s = os.path.join(root, file)
                paths.append(s)
    return paths

loc_dirA = r'/Users/user/Documents/herlog/Directory_A'
path_dirA = loc_dirA
files_dirA = os.listdir(path_dirA)
paths_dirA = []

loc_dirB = r'/Users/user/Documents/herlog/Directory_B'
path_dirB = loc_dirB
files_dirB = os.listdir(path_dirB)
paths_dirB = []

paths_dirA = get_filepaths_from_directory(path_dirA)
paths_dirB = get_filepaths_from_directory(path_dirB)

print("#!/bin/bash")

for j, fileA in enumerate(files_dirA):
    fileA_without_extension = fileA.split(".")[0]
    found_dirA_full_path = grep(paths_dirA, fileA) #
    found_dirB_file = grep(files_dirB, fileA_without_extension)[0]
    #fileB_without_extension = found_dirB_file.split(".")[0]
    found_dirB_full_path = grep(paths_dirB, found_dirB_file)
    print("diff ", found_dirA_full_path[0], " ", found_dirB_full_path[0], " > ", fileA, "_", found_dirB_file, "_$(date +%Y%m%d).txt", sep = "")
