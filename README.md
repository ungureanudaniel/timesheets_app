# Django Timesheets App == underconstruction ==

This repository contains a Django web application for managing timesheets in a company or anyhow you want. It includes features for user registration, profile management, timesheet submission, and reporting.

## Features

- **User Registration and Authentication**:
  - Users can register with username, email, and password.
  - New registrations are pending approval by administrators.
  
- **User Profile**:
  - Profile page displays user information and account status.
  - Only approved users can access full app functionalities.

- **Timesheets**:
  - Users can submit weekly or monthly working hours.
  - Supervisors can generate reports based on timesheet data.
  
- **Internationalization (i18n)**:
  - Ready for setting up translations in any language.
  
- **Async Tasks and Caching**:
  - Plan to utilize Celery for async task management.
  - Plan to utilize Redis for caching.

- **REST API**:
  - Will have Integration with external systems via RESTful APIs.

- **CONTAINERIZATION**:
  - Docker containerization will be done

## Project Structure

The project follows a standard Django application structure:

timesheets/
├── accounts/ # App for user authentication and profiles
├── timesheets/ # App for timesheet management
├── static/ # Static files (CSS, JS, etc.)
├── templates/ # HTML templates
├── manage.py # Django management script
└── requirements.txt # Python dependencies

## Setup Instructions

### Prerequisites

- Python 3.10.8
- Django 3.2
- Redis (for caching, still under implementation)
- Celery (for async tasks, still under implementation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ungureanudaniel/timesheets.git
   cd timesheets
2. Create and activate a virtual environment:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate # to ativate the environment in linux
   ./myvenv/Scripts/activate` # to activate the environment in windows, although PowerShell can give you a headache. I recommend though the terminal in Visual Studio Code if windows is not avoidable

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
   ```bash
   python manage.py migrate
5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
6. Run the development server:
   ```bash
   python manage.py runserver
7. Access the application at http://localhost:8000