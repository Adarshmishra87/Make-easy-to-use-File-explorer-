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


# 1. Ask for folder name
# The script asks for the name of the folder to create.

# 2. Get current directory
# It checks the current directory with os.getcwd().

# 3. Create full folder path
# Combines the folder name with the current directory.

# 4. Check if folder exists
# Checks if the folder already exists with os.path.exists().

# 5. Create folder if it doesn't exist
# If not, it creates the folder using os.makedirs().

# 6. Display success message
# Confirms folder creation or informs the user it already exists.
