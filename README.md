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
