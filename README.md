# Bruteforce_Pdf_Password

# Simple PDF Password Recovery

A lightweight, Python-based tool to recover lost passwords for PDF files using a dictionary attack (wordlist) method. This script utilizes the `pikepdf` library for high-speed processing.

## ⚠️ Disclaimer

**Educational Use Only.**
This script is intended to help you recover passwords for files **you own** or have explicit permission to audit. Do not use this tool for unauthorized access to protected files. The author is not responsible for any misuse of this code.

## 🚀 Features

* **Fast Processing:** Built on `pikepdf` (backed by QPDF and C++), making it significantly faster than pure Python libraries like PyPDF2.
* **Progress Tracking:** Displays real-time progress updates and percentage completion in the terminal.
* **Error Handling:** Gracefully handles incorrect passwords and file errors.
* **Simple Configuration:** Easy to modify for different target files.

## 📋 Prerequisites

You need Python 3.x installed on your system.

### Install Dependencies

This script requires the `pikepdf` library. Install it via pip:

```bash
pip install pikepdf

## 🛠️ Usage

1.  **Clone the repository** (or download the script).
2.  **Prepare your files:**
    * Place your locked PDF file in the same folder as the script.
    * Place your wordlist (text file with potential passwords) in the same folder.
3.  **Configure the script:**
    Open `run.py` in a text editor and modify the bottom section to match your filenames:

    ```python
    if __name__ == "__main__":
        # CHANGE THESE FILENAMES TO MATCH YOUR FILES
        target_pdf = "your_locked_file.pdf"  # Replace "a.pdf"
        wordlist = "passwords.txt"           # Replace "1.txt"
        
        recover_pdf_password(target_pdf, wordlist)
    ```
4.  **Run the script:**

    ```bash
    python run.py
    ```

## 📝 Example Output

```text
Starting recovery for: secure_doc.pdf
Using wordlist: rockyou.txt
Loaded 14344392 passwords to test...
Testing... 5000/14344392 (0.1%)
========================================
 SUCCESS! Password found: 123456
========================================
