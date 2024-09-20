# Django Timesheets App == Under Construction ==

This repository contains a Django web application for managing timesheets in a company or for personal use. It includes features for user registration, profile management, timesheet submission, and reporting.

## Features

- **User Registration and Authentication**:
  - Users can register with a username, email, and password.
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
  - Will have integration with external systems via RESTful APIs.

- **Containerization**:
  - Docker containerization will be handled with Docker Compose.

## Project Structure

The project follows a standard Django application structure:

timesheets/ ├── accounts/ # App for user authentication and profiles ├── timesheets/ # App for timesheet management ├── static/ # Static files (CSS, JS, etc.) ├── templates/ # HTML templates ├── manage.py # Django management script └── requirements.txt # Python dependencies


## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Installation and Running with Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ungureanudaniel/timesheets.git
   cd timesheets

2. **Build and start the containers**:
  ```bash 
   docker-compose up --build

2. **Create the superuser (admin):**:
  ```bash 
   docker-compose exec web python manage.py createsuperuser

2. **Access the application**:

Open your web browser and go to http://localhost:8000.

2. **Clone the repository**:
  ```bash 
   docker-compose down

### Additional Notes

Ensure that Docker and Docker Compose are properly installed on your system.
The application will run in development mode, and additional configuration may be necessary for production use.
For any issues or contributions, feel free to open an issue or pull request in the repository.

