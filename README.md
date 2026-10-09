# Student Management System (SMS)

A Python-based application designed to manage student records efficiently. The project features a dual-interface system, allowing users to interact via a command-line interface or a graphical desktop application, both powered by a persistent SQLite database backend.

## 📁 Repository Structure

| File | Description |
| :--- | :--- |
| `sms_gui.py` | Graphical User Interface (GUI) application built with Python. |
| `sms_cui.py` | Console User Interface (CUI) application for terminal-based operation. |
| `manaswarke.db` | SQLite database file storing persistent student records and logs. |

## ✨ Features

- **Dual Interface:** Choose between a user-friendly Graphical Interface (`sms_gui.py`) or a lightweight Terminal Console (`sms_cui.py`).
- **Persistent Storage:** Fully integrated with an SQLite database (`manaswarke.db`) to securely retain data across sessions.
- **Core CRUD Operations:** Complete capabilities to Add, View, Update, and Delete data records seamlessly.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your machine. No heavy external installations are required as SQLite comes bundled natively with Python.

### How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **To run the Graphical Desktop Application:**
   ```bash
   python sms_gui.py
   ```

3. **To run the Command Line Terminal Application:**
   ```bash
   python sms_cui.py
   ```

## 🛠️ Tech Stack
- **Language:** Python 3
- **Database:** SQLite 3
