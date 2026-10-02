# Student Management System

A Python-based application designed to manage student records efficiently. The system maintains persistent records using a local database backend and offers two distinct interaction interfaces: a Command-Line/Console User Interface (CUI) and a Graphical User Interface (GUI).

## 📁 Repository Overview

* **`manaswarke.db`** – SQLite database file handling persistent storage for student profiles, courses, and management records.
* **`sms_gui.py`** – Graphical User Interface built with a Python windowing framework (like Tkinter) for visual form entry and interactive management.
* **`sms_cui.py`** – Console/Command-Line User Interface providing structured, terminal-based navigation loops for lower-overhead management.

## 🚀 Key Architectural Features

* **Dual-Interface Design:** Users can select between a lightweight terminal-driven interface (CUI) or an intuitive graphical window layout (GUI).
* **Database Persistence:** Built-in structured queries safely commit, read, update, and remove system entities directly inside the relational database.
* **CRUD Functionality:** Full capabilities to Create, Read, Update, and Delete student tracking information.

## 💻 How to Run the Project

1. Verify that Python and its standard database utilities are configured on your local computer.
2. Open your system terminal or command prompt inside this repository's root directory.
3. Launch your preferred runtime layout choice:

   **For the Graphical Visual Application:**
   ```bash
   python sms_gui.py
   ```

   **For the Terminal Console Interface:**
   ```bash
   python sms_cui.py
