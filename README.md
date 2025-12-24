HEER — Women’s Clothing Brand Website (Django)

HEER is a modern, elegant women’s clothing brand website built with Django.
The brand is based in Hyderabad, Pakistan, specializing in women’s fashion with strong roots in City Market retail culture.

✨ Features

Responsive Home, Shop, About Us, and Contact pages

Reusable base template (index.html) using Django template inheritance

Modern UI with Bootstrap 4

Image galleries using Django static files

Functional Contact Form with database storage

Django messages framework for success alerts

Clean URL routing and view separation

🛠 Tech Stack

Backend: Django 5.x

Frontend: HTML5, CSS3, Bootstrap 4

Database: SQLite3

Python: 3.11

Version Control: Git

📁 Project Structure
django/
│── home/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/
│       ├── index.html
│       ├── main.html
│       ├── shop.html
│       ├── about.html
│       └── contact.html
│
│── static/
│   └── images/
│
│── myproject/
│   ├── settings.py
│   └── urls.py
│
│── manage.py

🚀 How to Run Locally
# activate virtual environment
venv\Scripts\activate

# run migrations
python manage.py migrate

# start server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

📸 Static Files

All images are stored in:

static/images/


Use in templates:

{% load static %}
<img src="{% static 'images/example.webp' %}">

📬 Contact Form

Stores messages in database

Shows dismissible success alerts

Uses Django messages framework
