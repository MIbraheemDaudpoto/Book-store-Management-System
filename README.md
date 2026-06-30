# 📚 Book Store Management System

A beginner-friendly **Book Store Management System** built using **Python**, **Flask**, **SQLAlchemy**, and **SQLite**. This project was developed as part of the **Code With Ahsan (CWA) Monthly Learning Challenge – June 2026**, focusing on Object-Oriented Programming (OOP) and Database Management.

---

## 🚀 Features

- 📖 View all books
- ➕ Add new books
- ✏️ Update existing books
- 🗑️ Delete books
- 💾 Persistent SQLite database
- 🏗️ Object-Oriented Programming (OOP)
- 🌐 Responsive web interface using Bootstrap

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- Bootstrap 5

---

## 📂 Project Structure

```
Book-Store-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── BooksDataBase.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_book.html
│   └── edit_book.html
│
└── static/
    ├── css/
    └── images/
```

---

## 🗄️ Database Schema

### Book Table

| Field | Type |
|-------|------|
| id | Integer (Primary Key) |
| title | String |
| author | String |
| category | String |
| price | Integer |
| quantity | Integer |

---

## 📸 Application Features

- Home page displaying all books
- Add Book form
- Edit Book page
- Delete Book functionality
- SQLite database integration
- Flask routing and templates

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
https://github.com/MIbraheemDaudpoto/Book-store-Management-System.git
```

## 2️⃣ Move into the Project Folder

```bash
cd book-store-management-system
```

## 3️⃣ Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install Flask Flask-SQLAlchemy
```

---

## 5️⃣ Run the Application

```bash
python app.py
```

---

## 6️⃣ Open in Browser

Visit:

```
http://127.0.0.1:5000
```

---

# 📦 Requirements

Create a file named **requirements.txt** containing:

```text
Flask
Flask-SQLAlchemy
```

Or generate it automatically:

```bash
pip freeze > requirements.txt
```

---

# 🧠 OOP Concepts Used

This project follows Object-Oriented Programming principles.

### Class

```python
class Book(db.Model):
```

The `Book` class represents a book entity in the database.

Each object stores:

- Title
- Author
- Category
- Price
- Quantity

SQLAlchemy maps this Python class to a SQLite database table.

---

# 📚 CRUD Operations

- ✅ Create Book
- ✅ Read Books
- ✅ Update Book
- ✅ Delete Book

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Flask Fundamentals
- Flask Routing
- HTML Templates (Jinja2)
- SQLAlchemy ORM
- SQLite Database
- CRUD Operations
- Object-Oriented Programming
- Database Modeling
- Form Handling
- Git & GitHub

---

# 🌟 Future Improvements

- Search Books
- Book Sales Module
- Purchase Module
- Customer Management
- Dashboard Analytics
- User Authentication
- Inventory Reports
- AI-based Book Recommendations

---

# 👨‍💻 Developed By

**Muhammad Ibraheem**

- Python Developer
- Flask Developer
- AI Enthusiast
- Campus Ambassador

---

# 📌 Challenge

This project was developed for:

**Code With Ahsan (CWA) Monthly Learning Challenge — June 2026**

Theme:

> **Object-Oriented Programming (OOP) & Databases**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is for educational purposes and is open for learning and improvement.
