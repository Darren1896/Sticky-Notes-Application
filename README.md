# Sticky Notes Application

## Overview
The Sticky Notes Application allows users to create, view, edit, and delete digital sticky notes. The application is built using Django and follows the CRUD (Create, Read, Update, Delete) model.

---

## Prerequisites

Before running the application, ensure the following are installed:

- Python 3.13.13
- Django
- Git (optional)
- VS Code or another code editor

---

## Installation Steps

### Step 1: Clone or Download the Project

If using Git:

```bash
git clone <repository-url>
cd sticky_notes
```

Or download and extract the project folder manually.

---

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install django
```

Or if a requirements file exists:

```bash
pip install -r requirements.txt
```

---

### Step 4: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

---

### Step 6: Open the Application

Open a web browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## How to Use the Application

### Create a Note

1. Click the **Create Note** button.
2. Enter the note title.
3. Enter the note content.
4. Click **Create Note**.

### View Notes

1. Open the homepage.
2. All saved notes will be displayed under My Notes

### Edit a Note

1. Select a note.
2. Click **Edit Note**.
3. Modify the information.
4. Click **Update Note**.

### Delete a Note

1. Select a note.
2. Click **Delete Note**.

---

## Project Structure

```text
sticky_notes/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── sticky_notes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── notes/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   └── notes/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
```

---

## Features

- Create notes
- View notes
- Edit notes
- Delete notes
- Simple user-friendly interface
- Data stored in SQLite database
