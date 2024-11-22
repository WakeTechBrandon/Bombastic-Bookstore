# CSC289 Programming Capstone Project

## Project Name: Bombastic Bookstore
- **Team Number**: 2  
- **Team Project Manager**: Brandon Biggs  
- **Team Members**: Ryan Burres, Jaylan Chavis, James Dove, Joshua Macy, Julia McDonald  

---

## Software Installation Guide: Bombastic Bookstore

### **Introduction**
Bombastic is a locally hosted inventory management tool for bookstores. This guide will detail how to install and run the application.  

---

### **System Requirements**
- **Python**: Version 3.8 or higher  
- **Pip**: Installed alongside Python  
- **Supported Operating Systems**:  
  - Windows  
  - Linux  
  - macOS  

---

### **Downloading the Installer**
Download `BombasticBookstore.zip` and unpack it in the directory of your choice.

---

### **Installing the Software**
1. **Verify Python and Pip Installation:** Ensure you have **Python 3.8** and **Pip** installed.  
   To verify, open a terminal or command prompt and type:  
   ```bash
   python --version
   pip --version

2. **Navigate to the Extracted Directory**: Once Python and Pip are confirmed to be installed and updated, navigate to the directory where you extracted the .zip file. 
3. **Run the Setup Script:** Open a terminal in the directory and run:
- Linux/MacOS: `chmod +x setup_local.sh`
        `./setup_local.sh`
- Windows: `setup_local.bat` (alternatively you could double click on the setup_local.bat file)

---

### **Launching the Software**

Once the above is complete, open a browser of your choice and navigate to:
`http:127.0.0.1:8000`

The homepage of Bommbastic should be visible.

### **Uninstalling the Software**

To uninstall: 
1. Stop the server (if running).
2. Delete the Bombastic Bookstore directory.


### **Troubleshooting**

**Common Issues and Solutions:**
- **Python or Pip Not Recognized:**
    - Ensure Python is added to your system's PATH. Reinstall Python if necessary.
- **Setup Script Errors:**
    - Confirm you are running the correct script for your operating system. On Linux/macOS, ensure the script is executable by running:
    ```bash
        chmod +x setup_local.sh
- **Server Not Running:**
    - If the browser cannot access `http://127.0.0.1:8000`, check the terminal to confirm Django's development server is running. Restart the setup script if necessary. 

 

### **Support and Contact Information**

For assistance, please contact the **Bombastic Bookstore Support Team:**
- Jaylan Chavis: `jmchavis3@my.waketech.edu`
- Ryan Burres: `rsburres@my.waketech.edu`
- Brandon Biggs: `bmbiggs@my.waketech.edu`
- James Dove: `jedove@my.waketech.edu`
- Joshua Macy: `jmacy@my.waketech.edu`
- Julia McDonald: `jfmcdonald@my.waketech.edu`
