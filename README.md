# 📂 Folder Creation Script

A simple Python script to create folders directly in the current working directory. Save time and avoid manual folder creation with this quick and efficient solution!

---

## 🚀 Features

- 🖋 **Interactive Input**: Enter the folder name via the terminal.  
- 📁 **Smart Check**: Ensures no duplicate folders are created by checking if a folder already exists.  
- ✅ **User-Friendly**: Provides clear feedback on whether a folder was created or already exists.  
- 💻 **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.  

---

## 🛠 How It Works

1. **Input Folder Name**:  
   Prompts the user to enter the desired folder name.  
2. **Locate Current Directory**:  
   Fetches the current working directory using `os.getcwd()`.  
3. **Generate Path**:  
   Combines the folder name with the directory path.  
4. **Check Existence**:  
   Verifies if the folder already exists using `os.path.exists()`.  
5. **Create Folder**:  
   If the folder doesn’t exist, it is created using `os.makedirs()`.  
6. **User Feedback**:  
   Displays a success or informative message about folder creation.

---

## 🖥 Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/folder-creation-script.git
   ```

2. Navigate to the folder:
   ```bash
   cd folder-creation-script
   ```

3. Run the script:
   ```bash
   python Start_One.py
   ```

4. Follow the on-screen instructions to create your folder.

---

## 💡 Example

### Input:
```plaintext
Enter the name of the folder you want to create:
MyNewFolder
```

### Output (if the folder doesn't exist):
```plaintext
Folder 'MyNewFolder' has been created at this location: /current/directory/MyNewFolder
```

### Output (if the folder already exists):
```plaintext
Folder 'MyNewFolder' already exists at this location: /current/directory/MyNewFolder
```

---

## 📦 Requirements

- Python 3.6 or higher  

To check your Python version:
```bash
python --version
```

---

## ✨ Customization

You can modify the script to:
- Create folders in a custom directory instead of the current working directory.  
- Add the ability to create nested folders.  
- Include file creation within the folder.

---

## 👨‍💻 Contributing

Feel free to fork the repository and submit a pull request if you have suggestions or improvements.

---

## 🌟 Acknowledgements

- Inspired by the need for automation in day-to-day tasks.
- Built with ❤️ by [Adarsh Mishra](https://github.com/Adarshmishra87).

---
