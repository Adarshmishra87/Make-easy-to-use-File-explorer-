import os
def create_file():
    folder_name=input("Enter the name of folder you wanted to create.\n")
    location=os.getcwd()
    folder_path=os.path.join(location,folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' has been already created here at this location {folder_path}")
    else:
        print(f"Folder {folder_name} already exists here at {folder_path}")

if __name__ == "__main__":
    create_file()