# Learning Log

A full-stack learning journal web application built with Django. Learning Log allows users to create accounts, organise their learning into topics, and record and edit entries as they develop their knowledge.

## Live Demo

**Live application:** https://main-bvxea6i-rfrkpa32eadtq.us-3.platformsh.site/

**GitHub repository:** https://github.com/Tunic202/learning_log

## Features

- User registration, login and logout
- Create and manage personal learning topics
- Add learning entries to topics
- Edit existing entries
- User-owned content
- Form validation
- Responsive Bootstrap-based interface
- PostgreSQL database in production
- HTTPS-enabled production deployment
- Custom 404 and 500 error pages
- Production security configuration
- Automated Django testing

## Technologies

- Python
- Django
- django-bootstrap5
- PostgreSQL
- HTML5
- CSS3
- Bootstrap
- Gunicorn
- Upsun
- Git and GitHub

## Application Screenshots

Screenshots can be added here to showcase the application interface and key user workflows.

## Project Structure

```text
learning_log/
├── accounts/
│   ├── views.py
│   └── urls.py
├── learning_logs/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── ll_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
├── .upsun/
├── .gitignore
├── manage.py
├── requirements.txt
└── requirements_remote.txt
