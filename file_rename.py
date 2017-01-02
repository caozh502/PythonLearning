import os
def file_rename():
    file_list = os.listdir(r"E:\CODE\TEST1\test1")
    print (file_list)
    saved_path=os.getcwd()
    print ("CWD is "+saved_path)
    os.chdir(r"E:\CODE\TEST1\test1")

    for file_name in file_list:
        print ("Old name - "+file_name)
        print ("New name - "+file_name.translate(None,"12"))
        os.rename(file_name,file_name.translate(None,"12"))
    os.chdir(saved_path)
file_rename()