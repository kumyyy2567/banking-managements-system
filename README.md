# Project112 - Student Account Management System

[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)

A Django web application for managing student accounts and transactions. Allows users to create accounts, perform transactions, view history and reports.

## Features
- **Account Management**: Create, view, update, and delete student accounts.
- **Transactions**: Add transactions, view history, generate reports.
- **Responsive Templates**: HTML templates for home, details, create/update forms, transaction pages.
- **Django Admin**: Full admin interface for data management.

## Tech Stack
- Backend: Django 4+
- Database: SQLite (default)
- Frontend: HTML/CSS/JS (Bootstrap if styled)
- Forms: Django Forms for validation

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Navigate to project:
   ```
   cd project112
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   venv\\Scripts\\activate  # Windows
   ```

3. Install Django:
   ```
   pip install django
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run server:
   ```
   python manage.py runserver
   ```
   Open http://127.0.0.1:8000/

## Project Structure
```
project112/
├── manage.py
├── project112/          # Main settings
│   ├── settings.py
│   └── urls.py
├── testapp3/            # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
└── templets/            # Templates
    ├── Base.html
    ├── home.html
    ├── create_acc.html
    └── ... (transaction templates)
```

## App Details
See [testapp3_README.md](testapp3_README.md) for testapp3 specifics.

## Screenshots
(Add screenshots of home, account create, transaction history)

## Run in Production
```
pip install gunicorn
gunicorn project112.wsgi
```

## Contributing
Fork, create branch, PR.

## License
MIT

# banking-project-
