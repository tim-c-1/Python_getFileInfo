am
import os
from datetime import datetime

home_folder = "C:/Users/username/Documents/"
src_folder = input("Filepath:")


if __name__ == "__main__":
   
    # Starting block of the script
    names_dict = dict()
    # Iterate through all files under source folder
    for path, dirs, files in os.walk(src_folder):
        
        for file_name in files:
            names_dict[file_name]= file_name
            names_dict[file_name]= os.path.getmtime(src_folder + '/' + file_name)
    print(names_dict)
    with open(os.path.join(home_folder, "fnames.txt"), "w") as f:
        f.write("{}\n".format(src_folder))
        for name, times in names_dict.items():
            f.write("{} : {}\n".format(name, datetime.utcfromtimestamp(times).strftime('%D')))
            print("{} : {}".format(name, datetime.utcfromtimestamp(times).strftime('%D')))
