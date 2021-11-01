import time
import os
import shutil

def main():
    deletedFolderCount = 0
    deletedFileCount = 0
    path = "folder_a"
    days = 0
    seconds = time.time() -(days*24*60*60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders: 
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount += 1        

            

                
                for file in files: 
                    file_path = os.path.join(root_folder, file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFileCount += 1                
    
    else: 
        if seconds >= get_file_or_folder_age(path):
            remove_file(path)
            deletedFileCount += 1
    print(f"totalFoldersDeleted : {deletedFolderCount}")
    print(f"totalFilesDeleted : {deletedFileCount}")


def remove_folder(path):
    if not shutil.rmtree(path): 
        print(f"{path}is removed")
    else: print(f"unable to delete the{path}")
    

def remove_file(path):    
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else: print(f"unable to delete the {path}")


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime
if __name__ =='__main__':
    main()
